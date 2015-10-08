
Installation
============

Notes on notation:
* Anything following '$' are commands to enter in a Terminal shell
* Anything following '=#' are commands to enter in a Postgres shell
* Otherwise, a file should be modified or the terminal is echoing back information
* \<project directory> is the path to your project files

###0) Install Xcode & Homebrew

Get [Xcode](https://itunes.apple.com/us/app/xcode/id497799835?mt=12) from the Mac App Store.

Install Xcode Command Line Tools. Open a Terminal and type

	$ xcode-select --install
	
Install Homebrew

	$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Add Homebrew to your path. Open or create your `~/.bash_profile` and add the line
```bash
export PATH=/usr/local/bin:$PATH
```
	
	$ source ~/.bash_profile

###1) Install python (2.7 or higher) and development packages

Homebrew installs Python 2.7 with Setuptools and pip
	
	$ brew install python

Add the new Python to your `~/.bash_profile`.
```bash
export PATH=/usr/local/share/python:$PATH
```

	$ source ~/.bash_profile

You can check if you are using the Homebrew python with

	$ which python
	/usr/local/bin/python

###2) Install PostgreSQL and related packages

Currently 9.4 is the most current release of postgres. Download Postgres.app from [http://postgresapp.com/](http://postgresapp.com/)

Move the app to `/Applications` and add the path to your `~/.bash_profile`.
```bash
export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/9.4/bin
```

	$ source ~/.bash_profile

You can verify the path with
	
	$ which psql
	/usr/local/bin/psql

###3) Get the project code

From the directory where you want your project to reside. We will call this the "project directory."

	$ git clone https://github.com/NorthBridge/alliance-community.git

Then instruct git to disregard your local changes to indexed settings files

	$ git update-index --assume-unchanged alliance/settings.py
	$ git update-index --assume-unchanged alliance/config/settings/dev.py
	$ git update-index --assume-unchanged bin/seed/static_inserts.sql
	$ git update-index --assume-unchanged alliance/email_settings.py
	$ git update-index --assume-unchanged alliance/backlog/github_settings.py

###4) Install project dependencies.

Use a virtual environment:

If you haven't already, install pip

	$ sudo easy_install pip

Install virtualenv using pip

	$ pip install virtualenvwrapper

Add the following two lines to your `~/.bash_profile`:

```bash
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```

	$ source ~/.bash_profile

Go to the project directory: Make sure you are in the directory alliance-community (if you do "ls" in your command line you will find there is another folder called alliance. Don't go in there. Stay here.)

	$ mkvirtualenv alliance

The next command is only necessary if you are not already using the created virtualenv

	$ workon alliance

*to get out of the virtual environment type in:
	
	$ deactivate
For more commands, see the [virtualenvwrapper command reference](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html)

Install python dependencies (while in virtual environment aka (alliance)):

	$ pip install -r requirements.txt

*Running this installs the following packages to your virtual environment (only in alliance):

```python
	Django==1.8.2
	ipaddress==1.0.7
	psycopg2==2.6.1
	pygithub3==0.5.1
	requests==2.7.0
```

###4) Update your database connection settings using your database admin user

The database settings are located in the `alliance/settings.py` file and must be updated to represent your local environment. 

Example:
```python
	DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'northbr6_devwaterwheel',
    'USER': 'postgres',
    'PASSWORD': 'postgres',
    'HOST': '127.0.0.1',
    'PORT': '5432',
    	}
	}
```
In this guide, we assume that that you are using user 'postgres' with password 'postgres', port '5432' and database 'northbr6_devwaterwheel'. However, you can use whatever you like so long as you update the same settings in `alliance/config/settings/dev.py`.
 
Create a new super user and database by opening the app and selecting 'Open psql'. Enter the following psql commands:
	
	=# CREATE USER postgres WITH SUPERUSER CREATEROLE CREATEDB;
	=# CREAT DATABASE northbr6_devwaterwheel OWNER postgres;

You can check if you successfully created a new superuser and database by further interacting with the psql shell.
To see the list of all users and their permissions:

	=# \du

To see the list of all databases and owners:

	=# \l

To exit psql:

	=# \q

So long as the app is still running, you can re-enter psql from a Terminal shell with
	
	$ psql

###5) Configure Django

Run Django migration scripts (only AFTER database is setup/configured):

	$ cd <project-directory>/alliance

	$ python manage.py makemigrations
	$ python manage.py migrate

Create a superuser (you will be prompted to type in a username, email and password):

	$ python manage.py createsuperuser

Use the bin/seed/static_inserts.sql file to populate the database with useful testing information:

Open the file (bin/seed/static_inserts.sql) and update the lines below with your information:

```SQL
	\set email '\'' '\<The email you used to create the django superuser account>' '\''
	\set fname '\'' '\<your first name>' '\''
	\set lname '\'' '\<your last name>' '\''
	\set github_repo '\'' '<github test repo>' '\''
```

For example:

```SQL
	\set email '\'' 'johndoe@gmail.com' '\''
	\set fname '\'' 'John' '\''
	\set lname '\'' 'Doe' '\''
	\set github_repo '\'' 'https://github.com/myorg/githubtest' '\''
```

After that, run the following command to import the data (you must be logged as a user that has privileges to access/update the database or provide user/password information to psql):

	$ psql -U postgres northbr6_devwaterwheel < <project directory>/bin/seed/static_insterts.sql

	
We also must create a trigger that will be responsible for update the backlog.update\_dttm field. This trigger will be fired on a row update event. The `postgres\_update_trigger.sql` script is located under the db folder.

	$ psql -U postgres northbr6_devwaterwheel < <project directory>/

There are also two other files that must be updated: `alliance/email_settings.py` (information concerning email service) and `alliance/backlog/github_settings.py` (information used to interact with the github API).

The system can notify users through email when an error on modules import/export occurs. Configuration can be done in the file email_settings.py. As an example, to send the emails using gmail service, one could configure the file as shown below:

```python
# Email configuration
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'exampleName@gmail.com'
EMAIL_HOST_PASSWORD = 'myPassword'
EMAIL_PORT = 587
EMAIL_RECIPIENT_LIST = ['exampleName2@gmail.com']
```

The main functionality of the system is the integration with the GitHub API. In order to put this integration to work there are some pre-requirements that must be met:

- You must have a GitHub Organization
- The GitHub repositories must be inside this organization. Of course, a repository must exist before the system can interact with it.
- You must create a "Personal access token":
- Click on your GitHub profile picture and select "Settings"
- Chose "Personal access tokens" on the left menu
- Chose a description for the token
- Select the scopes: repo, public_repo, user, gist
- Click "Generate token"
- Copy the generated token as we will use it later (warning: You cannot access the generated token after leaving the page so be careful to store it elsewhere)

- You must configure a GitHub webhook inside the Organization:

*Helpful link: https://developer.github.com/webhooks/creating/

To set up a repository webhook on GitHub, head over to the Settings page of your repository, and click on Webhooks & services. After that, click on Add webhook.

Payload URL = the server endpoint that will receive the webhook payload.

The Payload URL must point to: 
-If you are running over HTTP (for example, through manage.py script):
  	
  	http://\<host\>:\<port\>/alliance/backlog/githubimport

install ngrok: https://ngrok.com/download
-first download and then unzip
-you can extract it in your downloads folder and then run it:

	$ ~/Downloads/ngrok http 8000


Something like this will pop up:
	
	ngrok by @inconshreveable                                       (Ctrl+C to quit)
	                                                                                
	Tunnel Status                 online                                            
	Version                       2.0.19/2.0.19                                     
	Web Interface                 http://127.0.0.1:4040                             
	Forwarding                    http://389c1340.ngrok.io -> localhost:8000        
	Forwarding                    https://389c1340.ngrok.io -> localhost:8000       
	                                                                                
	Connections                   ttl     opn     rt1     rt5     p50     p90       
	                              0       0       0.00    0.00    0.00    0.00  
	
	http://389c1340.ngrok.io/alliance/backlog/githubimport
	
^This become the payload url. note that http://389c1340.ngrok.io/ points to localhost:8000 (the default)

- If you want to use HTTPS (the HTTP server must be configured):
    - https://\<host\>:\<port\>/alliance/backlog/githubimport
    - Remember to "Disable SSL verification" if you have a self signed certificate
- Content type: application/json
- Secret: chose a strong secret
- Which events would you like to trigger this webhook?
  - Choose "Let me select individual events" and check the "Issues" event.

Now we can configure the `alliance\backlog\github_settings.py` file (copy the name of the organization, your token, and your secret):

```python
GITHUB_OWNER = "\<GitHub Organization\>"
GITHUB_TOKEN = "\<GitHub generated token\>"
GITHUB_WEBHOOK_SECRET = "\<The secret you created on GitHub\>"
```

Running
=======

From the project directory:
	$ python ./alliance/manage.py runserver [host:port]

Example (add the same info you added when creating the webhook aka the same host and port):
	
	$ python manage.py runserver 

Now you can go to \<host\>:\<port\>/admin and login using the user created above. 

Example: Open a browser and type into the web url:

	localhost:8000/admin


You can create groups and regular users that will be used to login into the alliance application (\<host\>:\<port\>/alliance).

Example: Open a browser and type into the web url:

	localhost:8000/alliance/apps/backlog


###Let's Get Started!

After logging into the admin interface, create a new user, using the same email you specified when running the static_inserts.sql file. The email field will be the link between the django auth user and the NorthBridge volunteer. Add the "Volunteers" group to the "Chosen groups" field of the user.

Creating User:

Go to [localhost:8000/admin](http://127.0.0.1:8000/admin) (still have the runserver running on the terminal).
Under the Authentication and Authorization administration tab click on "Users". Add a new user example: newuser and give a password (i.e. password); type it 2x and click save!

Congrats! you just created your first user! (well other than the user you created while in the terminal--that createsuperuser command) So what can this user do?!

You should have been directed to a new page where you can fill out neat stuff about your user. Do whatever you like!

Example:
	
	Personal Info:
	first name: new
	last name: user
	email: newuser@newuser.gq
	
	Permissions: Active
	Groups: Volunteer (add-- click the arrow)
	User Permissions: admin | log entry | can change log entry (add-- click the arrow)
	Date joined: today & now
	click SAVE!

####Remember creating your superuser in the terminal?
while still in the admin page under "Core" click on Volunteers. Recognize someone? there you are!

Now you are ready to logout from admin account and access the application using the regular user you have created above.

####To the Alliance!

Go to [localhost:8000/alliance/apps/backlog](http://127.0.0.1:8000/alliance/apps/backlog)

A main restriction is that the user's email must match the volunteer's email. It is through this relation that we can link a django user and the volunteer's informations. For now there is no database constraint ensuring this.
