var fs = require("fs");
var http = require("http");
var os = require("os");
var ip = require("ip");
const { time } = require("console");

var server = http.createServer(function (req, res) {
    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function (err, body) {
            res.writeHead(200, { "Content-Type": "text/html" })
            res.end(body)
        })
    }

    else if (req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        totalMem=[(os.totalmem() / 1024) + " mB"];
        freeMem=[(os.freemem() / 1024) + " mB"];
        numberCPU=os.cpus().length;

        String.prototype.toHHMMSS = function () {
            var sec_num = parseInt(this, 10);
            var hours = Math.floor(sec_num / 3600);
            var minutes = Math.floor((sec_num - (hours * 3600)) / 60);
            var seconds = sec_num - (hours * 3600) - (minutes * 60);

            if (hours < 10) {hours = "0 " + hours}
            if (minutes < 10) {minutes = "0 " + minutes}
            if (seconds < 10) {seconds = "0 " + seconds};
            return time;
        }
        var time = process.uptime();
        var uptime = [(time + "").toHHMMSS() + " seconds"];

        

        html = `
        <!DOCTYPE html>

        <head>
            <title>System Info</title>
        </head>

        <body>
            <h1>Hello! Welcome to my Node Site!</h1>
            <p>Hostname: ${myHostName} </p>
            <p>IP: ${ip.address()}</p>
            <p>Total Memory: ${totalMem}</p>
            <p>Free Memory: ${freeMem}</p>
            <p>Number of CPUs: ${numberCPU}</p>
            <p>Server Uptime: ${uptime}</p>
        </body>

        </html>
        `
        res.writeHead(200, {"Content-Type" : "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, { "Content-Type": "text/plain" });
        res.end(`404 File Not Found at ${req.url}`);
    }

});

server.listen(3000);
console.log("Server listening on port 3000");