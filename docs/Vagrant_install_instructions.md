Installation
============

###1) Install Vagrant
https://www.vagrantup.com/docs/installation/

###2) Install VirtualBox
https://www.virtualbox.org/wiki/Downloads

[Add: what this puts on your computer]

###3) Get the alliance code
Go to your project directory and clone the alliance repo:

    git clone https://github.com/NorthBridge/alliance-community.git
    
###4) Create the VM
Change to the directory with the file `VagrantFile` and start the vagrant vm [add path]

    vagrant up
    
The first time you run this it will take a while as it has to download a
machine image (vagrant calls them boxes) for the vm. Future `vagrant up`
commands won't require this lengthy step.

`vagrant up` installs all the necessary packages in the vagrant vm
* python, python-dev
* postgres, libpq-dev
* pip
* virtualenvwrapper
creates a virtualenv for the project and installs the project dependencies
in that virtualenv.

If show up a message that the port is already being used, open the VagrantFile
and change host number in the following lines:
    config.vm.network :forwarded_port, guest: 8000, host:8000
    config.vm.network :forwarded_port, guest: 9001, host:9001

###5) Migrate the database
Open a vm session by executing

    vagrant ssh

If the error "`ssh` executable not found in any directories in the %PATH%
variable" appear set a new enviroment variable for Bin folder for Git and
try the vagrant ssh command again.

    set PATH=%PATH%;C:\Path to Git Folder\Git\bin

(Windows instruction) If the error persist modify ssh.rb file inside the
vragrant lib folder C:\vagrant\vagrant\embedded\lib\ruby\gems\1.9.1\gems\
vagrant-1.0.3\lib\vagrant\ssh.rb to comment out the faulty Windows check 
and add a real SSH check and try the vagrant ssh command again.

'# if Util::Platform.windows?
  # raise Errors::SSHUnavailableWindows, :host => ssh_info[:host],
                                       # :port => ssh_info[:port],
                                       # :username => ssh_info[:username],
                                       # :key_path => ssh_info[:private_key_path]
'# end

which = Util::Platform.windows? ? "where ssh >NUL 2>&1" : "which ssh >/dev/null 2>&1"
raise Errors::SSHUnavailable if !Kernel.system(which)


Inside the vm the directory `/vagrant` is shared with the project directory
where the `VagrantFile` lives. Below that is the alliance directory. Change
to that directory and migrate the db:

    cd /vagrant/alliance
    ./manage.py migrate

If it not recognize the command ./manage.py try change it for manage.py or
python manage.py.

If the message persist, the django-admin script should be on your system path
if you installed Django via its setup.py utility. If it’s not on your path, you
can find it in site-packages/django/bin within your Python installation.
Consider symlinking it from some place on your path, such as /usr/local/bin.

For Windows users, who do not have symlinking functionality available, you
can copy django-admin.exe to a location on your existing path or edit the
PATH settings (under Settings - Control Panel - System - Advanced - 
Environment...) to point to its installed location.
    
Any time there is a schema change with new migration files, you'll need to
repeat this step.

###6) Start the webserver
We can use the django development server for our local dev environment

    ./manage.py runserver 0.0.0.0:9001
    
The ip address 0.0.0.0 is the ip address of the host and port 9001 is
specified in the `VagrantFile` as a forwarded port. If you change the port
on step 3 you should use the same number here. This way you can open a
browser on your host machine (not the vm) and http://127.0.0.1:9001 will
retrieve the page served by the vm.

[add the full url to the app]

[add login creds - need to import static data somehow]

###7) Run the tests
The tests have to be run in the vm since that is where the database lives.

   ./manage.py test
   
###8) (Optional) Share your local server
HashiCorp (makers of vagrant) provider a service that lets you make your
local development server available to the public. You have to create
a (free) account with HashiCorp (https://atlas.hashicorp.com/) and then
while your development server is running, use the following commands in the
host machine

   vagrant login
   vagrant share
   
A public facing url will be printed on your console. You can use this for
github webhooks.

###9) To make code changes
Open the project files in your editor on your local host. You will see your changes reflected in your local running installation. Commit to git in the usual fashion. [confirm this]


