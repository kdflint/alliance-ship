# Development

In order to develop, you basically need 

1) The codebase open in your IDE of choice
2) A Vagrant VM running
3) One or more terminal sessions open into your Vagrant VM
4) A web server running, hosted by your VM
5) An active HashiCorp share to allow round trips between your local app and GitHub
6) A standard web browser to hit the app and test your code changes

### Making code changes (1)

Open/edit the project source files at `<project-root>/alliance-community` in your IDE of choice. Edits will be immediately visible in your browser, possibly requiring a browser refresh (<Ctrl-R>)

### Starting the web application server (2-4)

```
cd <project-root>/alliance-community
vagrant up
vagrant ssh
runserver
```

### Setting up a HashiCorp share and hitting the application in a browser (5-6)

Refer to Steps 13) and 14) in the Installation procedures. https://github.com/NorthBridge/alliance-community/blob/master/docs/install.md

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

```
sudo -u postgres psql -d northbr6_devwaterwheel
```

### View vm Apache logs. Do similar for anything needing vm root access.

```
sudo su
tail -f /var/log/apache2/error.log
``` 
