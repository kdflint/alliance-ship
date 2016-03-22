Installation
============

###1) Install Vagrant
https://www.vagrantup.com/docs/installation/

###2) Get the alliance code
Go to your project directory and clone the alliance repo:

    git clone https://github.com/NorthBridge/alliance-community.git
    
###3) Create the VM
Change to the directory with the file `VagrantFile` and start the vagrant vm

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

###4) Migrate the database
The vm is available via ssh:

    vagrant ssh
    
Inside the vm the directory `/vagrant` is shared with the project directory
where the `VagrantFile` lives. Below that is the alliance directory. Change
to that directory and migrate the db:

    cd /vagrant/alliance
    ./manage.py migrate
    
Any time there is a schema change with new migration files, you'll need to
repeat this step.

###5) Start the webserver
We can use the django development server for our local dev environment

    ./manage.py runserver 0.0.0.0:9001
    
The ip address 0.0.0.0 is the ip address of the host and port 9001 is
specified in the `VagrantFile` as a forwarded port. This way you can open
a browser on your host machine (not the vm) and http://127.0.0.1:9001 will
retrieve the page served by the vm.

###6) Run the tests
The tests have to be run in the vm since that is where the database lives.

   ./manage.py test
   
###7) Share your local server
HashiCorp (makers of vagrant) provider a service that lets you make your
local development server available to the public. You have to create
a (free) account with HashiCorp (https://atlas.hashicorp.com/) and then
while your development server is running, use the following commands in the
host machine

   vagrant login
   vagrant share
   
A public facing url will be printed on your console. You can use this for
github webhooks.