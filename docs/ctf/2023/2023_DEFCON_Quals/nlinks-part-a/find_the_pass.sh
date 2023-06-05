#!/usr/bin/expect -f

set password [lindex $argv 0]

spawn ./634
expect "Passphrase:"
send $password+"\r"
expect ""
