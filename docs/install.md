Installation
============

### 1) Install Vagrant

Follow instructions at https://www.vagrantup.com/docs/installation/

Vagrant is a command line utility for managing the lifecycle of virtual machines. The Vagrant installation will 1) create a directory named /vagrant that contains the Vagrant binaries, and 2) create a directory named /.vagrant.d that contains yet-to-be-created user data. For example, every Vagrant "box" you create will be stored in /.vagrant.d along with it's state, etc.

Confirm this step is successful by executing this command at your command line: `vagrant --version`

You should get a response something like `Vagrant 1.8.3`

### 2) Install VirtualBox

Follow instructions at https://www.virtualbox.org/wiki/Downloads

VirtualBox is an open source, general-purpose virtualizer for x86 hardware, targeted at server, desktop and embedded use. It allows you to run multiple operating system "boxes" within a single host.

Vagrant works with VirtualBox to provide the virtual machine that will host Alliance on your local computer.

Confirm this step is successful by locating the folder `VirtualBox VMs` inside your home directory or other default installation directory

### 3) Create a GitHub OAuth test application configuration

#### 3a)

Under your GitHub Public Profile, select `OAuth applications` from the Developer section of the navigation menu.

Click the `Register a New Application` button and enter these settings:

    Application name = `Alliance`
    Homepage URL = `http://northbridgetech.org`
    Application Description = `This is a local testing installation of the Northbridge Alliance application` 
    Authorization callback URL: Leave empty for now

#### 3b)

Under your GitHub Public Profile, select `Personal access tokens` from the Developer section of the navigation menu.

Click the `Generate New Token` button and enter these settings:

    Token description = Alliance webhooks
    Select scopes: Select all of the components in the 'Repo' and 'User' sections of the table

### 4) Get the alliance code

Create or locate the directory within which you want to host the Alliance source code. In this documentation, we'll call this directory `<project-root>`

Navigate to that directory, and execute this command to pull the source code to your local machine.

```
git clone https://github.com/NorthBridge/alliance-community.git
```

Confirm this step is successful by confirming that a directory was created inside `<project-root>` named `alliance-community`. 
    
### 5) Create the Vagrant Virtual Machine (VM)

Navigate to the Alliance source code root directory `<project-root>/alliance-community` and confirm that it contains a file named `Vagrantfile`. Execute this command in order to create a Vagrant virtual machine

    vagrant up
    
For a fresh install this it will take several minutes--even up to an hour--depending on your connection speed. Vagrant is downloading an entire machine image (Vagrant calls them boxes) for the virtual machine. Future `vagrant up` commands won't require this lengthy step. Watch the progress reporting to understand where the process is at. Avoid interupting the process. 

Note: This one command does a lot of things! After the virtual machine image is downloaded, your local Alliance project will be configured using a standard Python virtual environment that resides on the Vagrant virtual machine. All Alliance project dependencies (libraries) are installed in the context of this Python virtual envirnment. Also, the postgresql database is created and initialized with static data. `Vagrantfile` holds the configuration instructions for this entire process.

Confirm this step is successful by comparing your command output to this output. It should be similar. https://github.com/NorthBridge/alliance-community/wiki/Installation-resources

### 6) Open your Vagrant session

From your Alliance source code root directory `project-root>/alliance-community`, open a virtual machine session by executing

    vagrant ssh

Confirm this step is successful by noticing command output that consists of a `Welcome to Ubuntu 14.04.5` message of several lines. Your command prompt should open to something like

`vagrant@vagrant-ubuntu-trusty-32`

Also, from this command prompt, confirm that when you execute the command `pwd` your result is `/home/vagrant`

Refer footnote a) for possible Windows error. [TODO - Is this footnote still relevant?]

### 7) Migrate the Django-synchronized database

From within your virtual machine session that you established in Step 5, execute

```
python /vagrant/alliance/manage.py migrate
```

See footnote b) for possible Windows error  [TODO - Is this footnote still relevant?]
    
Note: Any time there is a schema change with new migration files, you'll need to repeat this step.

Confirm this step is successful by comparing your command output to this output. It should be similar. https://github.com/NorthBridge/alliance-community/wiki/%60manage.py-migrate%60-sample-output

### 8) Run the tests

From within your virtual machine session that you established in Step 5, execute

```
python /vagrant/alliance/manage.py test
```

Confirm this step is successful by comparing your command output to this output. It should be similar. https://github.com/NorthBridge/alliance-community/wiki/%60manage.py-test%60-sample-output

### 9) Create django superuser

From within your virtual machine session that you established in Step 5, execute

```
python /vagrant/alliance/manage.py createsuperuser
```
The rest of these instructions assume that you enter `superuser` at the Username prompt. The email can be real or fake. Remember the password that you select.

Confirm this step is successful by comparing your command output to this output. It should be similar. https://github.com/NorthBridge/alliance-community/wiki/%60manage.py-createsuperuser%60-sample-output

### 10) Share your local server (to enable Github test callbacks)

HashiCorp (makers of vagrant) provider a service that lets you make your local development server available to the public. You have to create a (free) account with HashiCorp (https://atlas.hashicorp.com/account/new) and then while your development server is running, use the following commands in the host machine

   vagrant login
   vagrant share
   
A public facing url will be printed on your console. You will use this for GitHub authentication and webhook callbacks.

### 11) Start the Django development webserver

From within your virtual machine session that you established in Step 5 execute

```
python /vagrant/alliance/manage.py runserver 0.0.0.0:9001
```

The ip address 0.0.0.0 is the ip address of the host and port 9001 is specified in the `Vagrantfile` as a forwarded port. If you change the port on step 3 you should use the same number here. This way you can open a browser on your host machine using one port (say, 9091) and the guest machine (the vm)) will forward the request to guest maching port 9001.

Confirm this step is successful by comparing your command output to this output. It should be similar. https://github.com/NorthBridge/alliance-community/wiki/%60manage.py-runserver%60-sample-output

### 12) Open the app in a local browser.

End User: [http://localhost:9091/accounts/login](http://localhost:9091/accounts/login)

Admin: [http://localhost:9091/admin](http://localhost:9091/admin)

User == superuser

### 13) To make code changes
Open the project files in your editor on your local host. You will see your changes reflected in your local running installation. Commit to git in the usual fashion. [confirm this]

### Footnotes

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


