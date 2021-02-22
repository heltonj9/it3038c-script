#Script runs using command ".\Diskspace.ps1"


Function Get-FreeDiskSpace($drive)
{
    #Script begins by asking which drive you want to check space on. (Usually C drive)
    $drive = Read-Host "Which drive to check space on?"
    #Script searches for both Free and Used separately to establish them as variables.
    $Free = Get-PSDrive $drive | Select-Object Free
    $Used = Get-PSDrive $drive | Select-Object Used
    #Script prints out to the user the remaining and used space in MegaBytes.
    "$drive has $Free MegaBytes left on it, and has used $Used MegaBytes so far."
}
Get-FreeDiskSpace


#This was the only source I used: 
#culterculter 4, et al. "How to Get Disk Capacity and Free Space of Remote Computer." Stack Overflow, 1 Aug. 1961, 
#stackoverflow.com/questions/12159341/how-to-get-disk-capacity-and-free-space-of-remote-computer.