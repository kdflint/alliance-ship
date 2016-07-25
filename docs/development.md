# Development

Making code changes


Starting a shell session

Making database queries or changes, from inside vm session
```
sudo -u postgres psql -d northbr6_devwaterwheel
```

View vm Apache logs or anything else that needs root privilege
```
sudo su
tail -f /var/log/apache2/error.log
``` 

Starting the server
```
cd <project-root>
vagrant up
vagrant ssh
run
```

Setting up Vagrant share, GitHub round trip.
After (and while) your local server is running, open new terminal window
```
cd <project-root>
vagrant login
vagrant share
```
Copy the url given by the share to both GitHub OAuth callback field. Use this domain to access the site running on your local system, for example:
```
http://<vagrant_share_domain>/login
```
