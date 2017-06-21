# Development

### Making code changes

Open/edit the project source files at `<project-root>/alliance-community` in your IDE of choice. Edits will be immediately visible in your browser, possibly requiring a browser refresh (<Ctrl-R>)

### Starting the web application server

```
cd <project-root>/alliance-community
vagrant up
vagrant ssh
runserver
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

### Setting up Vagrant share, GitHub round trip.

After (and while) your local server is running, open new terminal window
```
cd <project-root>/alliance-community
vagrant login
vagrant share
```

Run Step 13) from the Installation instructions at https://github.com/NorthBridge/alliance-community/blob/master/docs/install.md 
