# Development

In order to develop, you basically need 

1) The codebase open in your IDE of choice
2) A Vagrant VM running
3) One or more terminal sessions open into your Vagrant VM
4) A web server running, hosted by your VM
5) An active HashiCorp share to allow round trips between your local app and GitHub
6) A standard web browser to hit the app and test your code changes

### (1) Making code changes

Open/edit the project source files at `<project-root>/alliance-community` in your IDE of choice. Edits will be immediately visible in your browser, possibly requiring a browser refresh (<Ctrl-R>)

### (2-4) Starting the web application server

```
cd <project-root>/alliance-community
vagrant up
vagrant ssh
runserver
```

### (5-6) Setting up a new HashiCorp share and hitting the application in a browser

This process must be done whenever you are starting a new development session or when your HashiCorp share expires for some reason (indicated by a message like this in your browser window: `Tunnel 5f115852.ngrok.io not found`)

With your web application server running, open a new terminal session and navigate to `<project-root>/alliance-community`

The execute, in the second terminal session,

```
vagrant login
vagrant share
```

Finally, update your Authorization callback field at Github using the share URL that is printed. Also, use that share URL to formulate your browser request to the application. (This will leave you with two running processes in two different terminal sessions.)

This is more fully documented in Steps 13) and 14) in the Installation procedures. https://github.com/NorthBridge/alliance-community/blob/master/docs/install.md

### Stop the web application server

```
Ctrl-c
```
### End your VM terminal session

```
exit
```

### Stop your VM

If for some reason you are working with multiple application environments, you will want to stop a VM before switching over to a different environment. This will avoid port conflicts.

```
vagrant halt
```

### Making database queries or changes, from inside vm session

Usually this is done by opening a new VM (vagrant) terminal session, then invoking the `psql` utility, which is postgresql command line utility.

In your new terminal session, navigate to `<project-root>/alliance-community`, then execute

```
vagrant ssh
sudo -u postgres psql -d northbr6_devwaterwheel
```

### View application logs.

In your IDE, load up `<project-root>/alliance-community/logs/alliance.log`. Hopefully you editor will refresh the file as it changes.

Alternatively, you can tail this log at the command line, either in a native terminal session or in a vm (vagrant) terminal session.

### View vm Apache logs. Do similar for anything needing vm root access.

In a vm (vagrant) terminal session

```
sudo su
tail -f /var/log/apache2/error.log
``` 

### Reprovision your vagrant vm, possibly done in order to update static data or other Vagrantfile provisioning changes

1. `git pull` to update your local code (likely bringing in Vagrantfile changes, static data changes, requirements change, etc.)
2. open a terminal session  
3. navigate to `<project-root>/alliance-community`  
4. `vagrant reload --provision` (This will re-run Vagrantfile as if you were provisioning your VM for the first time)
5. Start up your app, hit it in the browser. Changes should be visible.
