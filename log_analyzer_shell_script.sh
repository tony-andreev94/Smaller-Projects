#!/bin/bash

#Input the logname and print all warnings or not
echo "Type in logname"
read -r logName
echo "Do you want to print all warnings?(Y/N)"
read -r userResponse

#grep commands to search the file for the desired strings
#empty echo commands are used to generate new lines
echo
echo "System Information:"
grep 'Software revisio' /mnt/c/Users/andreeto/Desktop/Scripts/$logName
grep "Up Time" /mnt/c/Users/andreeto/Desktop/Scripts/$logName
echo
echo
echo "Errors:"
grep "Power Supply failure\|Fan Failure\|Other Fault\|Unrecoverable fault on PoE controller\|selftest failure\|self test failure" /mnt/c/Users/andreeto/Desktop/Scripts/$logName
grep "Other Fault" /mnt/c/Users/andreeto/Desktop/Scripts/$logName 
echo 
echo 

#If condition for printing additional warning messages
if [ "$userResponse" = "Y" ]; then
	echo "All warnings:"
	grep "W [0-9][0-9]" /mnt/c/Users/andreeto/Desktop/Scripts/$logName
elif [ "$userResponse" = 'N' ]; then
	echo "Warnings were not printed"
else echo "Invalid input"

fi	
