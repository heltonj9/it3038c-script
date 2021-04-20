var fs = require("fs");

fs.readFile('./node/public/my-file.txt', 'utf8', function(err, data) {
    if (err) throw err;
    console.log(data);
})