Local Setup (1-1.5 hours)
============

These instructions will build a development environment from scratch. If you already have a working environment and want to duplicate it, or start over for some reason, jump to Step 5.

### 1) Install Vagrant (10 minutes)

Follow instructions at https://www.vagrantup.com/docs/installation/

Vagrant is a command line utility for managing the lifecycle of virtual machines. The Vagrant installation will 1) create a directory named /vagrant that contains the Vagrant binaries, and 2) create a directory named /.vagrant.d that contains yet-to-be-created user data. For example, every Vagrant "box" you create will be stored in /.vagrant.d along with it's state, etc.

Confirm this step is successful by executing this command at your command line: `vagrant --version`

You should get a response something like `Vagrant 1.8.3`

### 2) Install VirtualBox (10 minutes)

Follow instructions at https://www.virtualbox.org/wiki/Downloads

VirtualBox is an open source, general-purpose virtualizer for x86 hardware, targeted at server, desktop and embedded use. It allows you to run multiple operating system "boxes" within a single host.

Vagrant works with VirtualBox to provide the virtual machine that will host Alliance on your local computer.

Confirm this step is successful by locating the folder `VirtualBox VMs` inside your home directory or other default installation directory

### 3) Create a GitHub test application configuration (10 minutes)

#### 3a) Create OAuth test application

Login to your GitHub account at https://github.com (Register for an account if you do not yet have one.)

In Settings, select `OAuth applications` from the Developer section of the navigation menu.

Click the `Register a New Application` button and enter these values:

    Application name = 'Alliance'
    Homepage URL = 'http://northbridgetech.org'
    Application Description = 'This is a local testing installation of the Northbridge Alliance application'
    Authorization callback URL: Leave empty for now
    
Click `Register Application` to save these settings. Leave this browser tab open because you will return to this screen in a later step in order to insert the newly generated Client ID and Client Secret values into your local configuration.

#### 3b) Create Personal Access token (for Webhooks)

In Settings, select `Personal access tokens` from the Developer section of the navigation menu.

Click the `Generate New Token` button and enter these settings:

    Token description = 'Alliance webhooks'
    Select scopes: Select all of the components in the 'Repo' and 'User' sections of the table

Note your personal access token for use later.

[TODO - Where do we plug this value in?]

### 4) Create a HashiCorp Account (5 minutes)

HashiCorp (makers of Vagrant) provides a developers service that lets you make your local development server available to the public. We will use this to enable GitHub callbacks (which cannot reach a local private server by default)

Create a (free) account with HashiCorp at https://atlas.hashicorp.com/account/new. Note your username and password for later use.

### 5) Get the Alliance source code (5 minutes)

Create or locate the directory within which you want to host the Alliance source code. In this documentation, we'll call this directory `<project-root>`

Navigate to that directory, and execute this command to pull the source code to your local machine.

```
git clone https://github.com/NorthBridge/alliance-community.git
```

Confirm this step is successful by confirming that a directory was created inside `<project-root>` named `alliance-community`. Also confirm that inside `<project-root>/alliance-community` is a file named `Vagrantfile`
   
### 6) Create the Vagrant Virtual Machine (VM) (Up to 30 minutes if slow connectivity)

Navigate to the Alliance source code root directory `<project-root>/alliance-community`. Execute this command in order to create a Vagrant virtual machine

```
vagrant up
```
    
For a fresh installation this will take several minutes--even up to an hour--depending on your connection speed. Vagrant is downloading an entire machine image (Vagrant calls them boxes) for the virtual machine. Future `vagrant up` commands won't require this lengthy step. Watch the progress reporting to understand where the process is at. Avoid interupting the process.

Don't be alarmed if the process seems to hang for a few minutes with this repeated output. Typically this will clear in about one minute.

```
default: Warning: Remote connection disconnect. Retrying...
```

Note: This one command does a lot of things! After the virtual machine image is downloaded, your local Alliance project will be configured using a standard Python virtual environment that resides on the Vagrant virtual machine. All Alliance project dependencies (libraries) are installed in the context of this Python virtual envirnment. Also, the postgresql database is created and initialized with static data. `Vagrantfile` holds the configuration instructions for this entire process.

[TODO - Describe the possibility of port conflict error and how to remedy.]

Confirm this step is successful by noting a `Successfully installed...` message after the process is over. Also, you can compare your entire command output to this output. It should be similar. https://github.com/NorthBridge/alliance-community/wiki/Installation-resources

### 7) Open your Vagrant session (2 minutes)

From your Alliance source code root directory `<project-root>/alliance-community`, configure and then open a virtual machine session by executing

```
cp /vagrant/alliance/config/.bash_aliases ~/.bash_aliases
vagrant ssh
```

[TODO - Can we figure out how to write the .bash_aliases file creation within Vagrantfile. Line 53 is not working - wy?]

Confirm this step is successful by noticing command output that consists of several lines starting with a `Welcome to Ubuntu 14.04.5` message. Your command prompt should open to something like

`vagrant@vagrant-ubuntu-trusty-32`

Also,confirm that when you execute the command `pwd` your result is `/home/vagrant`

Refer footnote a) for possible Windows error. [TODO - Is this footnote still relevant?]

### 8) Migrate the Django-synchronized database (2 minutes)

From within your virtual machine session that you established in Step 7, execute

```
python /vagrant/alliance/manage.py migrate
```

See footnote b) for possible Windows error  [TODO - Is this footnote still relevant?]
    
Note: Any time there is a schema change with new migration files, you'll need to repeat this step.

Confirm this step is successful by comparing your command output to this output. It should be similar. https://github.com/NorthBridge/alliance-community/wiki/%60manage.py-migrate%60-sample-output

### 9) Run the tests (2 minutes)

From within your virtual machine session that you established in Step 7, execute

```
python /vagrant/alliance/manage.py test
```

Confirm this step is successful by comparing your command output to this output. It should be similar. https://github.com/NorthBridge/alliance-community/wiki/%60manage.py-test%60-sample-output

### 10) Create django superuser (2 minutes)

From within your virtual machine session that you established in Step 7, execute

```
python /vagrant/alliance/manage.py createsuperuser
```

The rest of these instructions assume that you enter `superuser` at the Username prompt. The email can be real or fake. Note the password that you select.

Confirm this step is successful by comparing your command output to this output. It should be similar. https://github.com/NorthBridge/alliance-community/wiki/%60manage.py-createsuperuser%60-sample-output

### 11) Update local OAuth configuration settings (5 minutes)

In your development IDE (or just a plain text editor), open the project source code file `<project-root>/alliance-community/alliance/config/local_settings.py`

Edit the values for `SOCIAL_AUTH_GITHUB_KEY` and `SOCIAL_AUTH_GITHUB_SECRET` so that these values match the values that were generated by GitHub after you executed Step 3a.

### 12) Start the Django development webserver (2 minutes)

From within your virtual machine session that you established in Step 7, execute

```
runserver
```

This command is an alias whose resolution can be viewed by `cat ~/.bash_aliases` from your Vagrant session. By default, the ip address 0.0.0.0 is the ip address of the host and port 9001 is specified in the `Vagrantfile` as a forwarded port.This way you can open a browser on your host machine using one port (say, 9091) and the guest machine (the vm) will forward the request to guest maching port 9001.

If you change the port on step 3 due to a local port conflict you should update the alias. 

Confirm this step is successful by comparing your command output to this output. It should be similar. https://github.com/NorthBridge/alliance-community/wiki/%60manage.py-runserver%60-sample-output

### 13) Share your local server (to enable GitHub test callbacks) (5 minutes)

With your development server is running, open a new command line terminal session. Execute the following three commands

   ```
   cd <project-root>/alliance-community
   vagrant login
   vagrant share
   ```
   
A string will be printed on your console, looking something like `frosty-armon-6109` We will call this string `<share-string>`

Specifically, the output from the vagrant share command will look like 

```
==> default: Creating Vagrant Share session...
    default: Share will be at: frosty-armon-6109
==> default: Your Vagrant Share is running! Name: frosty-armon-6109
==> default: URL: http://frosty-armon-6109.vagrantshare.com
```

Navigate to your GitHub profile. Use `<share-string>` to create a fully qualified URL in the Authorization callback field of your OAuth application settings (the field we left empty in step 3a).

The format of this URL is 'http://<share-string>.vagrantshare.com/complete/github`

Example: `http://frosty-armon-6109.vagrantshare.com/complete/github`

Click on `Update Application` to save

Note: Periodically these shares expire, and they always expire when you stop your Development server. If you get notice that the share is expired simply repeat the above steps, making sure to hit the updated URL in your browser. This is a pain at times, but you'll get speedy at it!

### 14) Open the app in a local browser. (2 minutes)

In a browser, navigate to `http://<share-string>.vagrantshare.com/accounts/login`

Example: `http://frosty-armon-6109.vagrantshare.com/accounts/login`

[TODO - Update the admin site access instructions below. They are not accurate.]

Admin: [http://localhost:9091/admin](http://localhost:9091/admin)

User == superuser

### 15) Now you are ready to rock and roll!

To make code changes, see https://github.com/NorthBridge/alliance-community/blob/master/docs/development.md

=====================================

### Footnotes

[TODO - These footnotes may no longer be relevant.]

a) If the error "`ssh` executable not found in any directories in the %PATH%
variable" appear set a new enviroment variable for Bin folder for Git and
try the vagrant ssh command again.

    set PATH=%PATH%;C:\Path to Git Folder\Git\bin

(Windows instruction) If the error persist modify ssh.rb file inside the
vragrant lib folder C:\vagrant\vagrant\embedded\lib\ruby\gems\1.9.1\gems\
vagrant-1.0.3\lib\vagrant\ssh.rb to comment out the faulty Windows check 
and add a real SSH check and try the vagrant ssh command again.

```
'# if Util::Platform.windows?
  # raise Errors::SSHUnavailableWindows, :host => ssh_info[:host],
                                       # :port => ssh_info[:port],
                                       # :username => ssh_info[:username],
                                       # :key_path => ssh_info[:private_key_path]
'# end

which = Util::Platform.windows? ? "where ssh >NUL 2>&1" : "which ssh >/dev/null 2>&1"
raise Errors::SSHUnavailable if !Kernel.system(which)
```

b) If the message persist, the django-admin script should be on your system path
if you installed Django via its setup.py utility. If it’s not on your path, you
can find it in site-packages/django/bin within your Python installation.
Consider symlinking it from some place on your path, such as /usr/local/bin.

For Windows users, who do not have symlinking functionality available, you
can copy django-admin.exe to a location on your existing path or edit the
PATH settings (under Settings - Control Panel - System - Advanced - 
Environment...) to point to its installed location.


