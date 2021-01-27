#$hello = "Hello, Powershell!"
#Write-Host($hello)
#function getIP {
#    (get-netipaddress).ipv4address | Select-string "192*"
#}

#write-host(getIP)

#write-host("This machine's IP is $IP")
#write-host("This machine's IP is {0}" -f $IP)
#$body = "This machine's IP is $IP. User is $env:username. Hostname is $. Powershell Version $HOST.Version.Major. Today's date is $Date"
#Send-mailmessage -To "heltonj9@mail.uc.edu" -From "heltonj9@mail.uc.edu" -Subject "IT3038c Windows Sysinfo" -Body $body
#-SmtpServer smtp.google.com -port 587 -UseSSL -Credential (Get-Credential)

#Link to git repo, screenshot of the body is the submission.

$IP = (get-netipaddress).ipv4address | Select-string "192*"
$Date = Get-Date


$body = "This machine's IP is: $IP. User is: $env:username. Today's date is $Date. Hostname is: $host. "

write-host($body)

