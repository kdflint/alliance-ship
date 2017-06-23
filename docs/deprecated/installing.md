# Installation

# Setup

To contribute, you'll need to fork this repository. Simply click on
*fork* in the [project's Github
page](https://github.com/NorthBridge/alliance-community).

You can either clone the forked repository via Github or via git.

To clone via Github:

Click on "Clone in Desktop" in order to have a copy of all of the files
on your Desktop (or wherever you choose to save and access the files).

To clone via Git, execute the following in the command line:

    git clone https://github.com/<your_username>/alliance-community

Now you should be ready to work on the project!

This guide assumse that you have the following installed:

- Python 2.7+ (not Python 3)
- Pip
- VirtualEnvWrapper
- PostgreSQL 9.4
- Django

For detailed installation instructions, check out these guides:

- [Installing in Windows](windows_install_instructions.md)
- [Installing in Mac OS X](mac_install_instructions.md)
- [Installing in Linux Ubuntu](ubuntu_install_instructions.md)

### Configure Django

If this is the first time installing the app, you'll need to have to
generate a `local.py` file within the `alliance/config/settings/` folder
to keep your secret API keys. You can do so by issuing the following
command in the command line:

    python bin/settings_builder.py

Run Django migration scripts:

    python manage.py makemigrations
    python manage.py migrate

Create a superuser (you will be prompted to type in a username, email
and password):

    python manage.py createsuperuser

Use the `bin/seed/static_inserts.sql` file to populate the database with
useful testing information:

Open the file and update the lines below with your information:

    \set email '\'' '\<The email you used to create the django account>' '\''
    \set fname '\'' '\<your first name>' '\''
    \set lname '\'' '\<your last name>' '\''

For example:

    \set email '\'' 'johndoe@gmail.com' '\''
    \set fname '\'' 'John' '\''
    \set lname '\'' 'Doe' '\''

After that, run the following command to import the data (you must be
logged as a user that has privileges to access/update the database or
provide user/password information to psql):

    psql devwaterwheel < /path/to/your/bin/seed/static_inserts.sql

We also must create a trigger that will be responsible for update the
`backlog.update_dttm` field. This trigger will be fired on a row update
event. The `Postgres_Update_Trigger.sql` script is located under the db
folder. If you have a test database, run the following command:

    psql devwaterwheel_test < bin/seed/postgres_update_trigger.sql

There is also two other sections within your `config/settings/local.py`
that must be updated:

- The email settings (can be seen within `config/settings/base.py`)
- The github settings (can also be seen within
  `config/settings/base.py`)

The system can notify users through email when an error on modules
import/export occurs. Configuration can be done in the file
`config/settings/local.py`. As an example, to send the emails using gmail
service, one could configure the file as shown below:

    # Email configuration
    EMAIL_USE_TLS = True
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'exampleName@gmail.com'
    EMAIL_HOST_PASSWORD = 'myPassword'
    EMAIL_PORT = 587
    EMAIL_RECIPIENT_LIST = ['exampleName2@gmail.com', 'exampleName3@yahoo.com']

The main functionality of the system is the integration with the GitHub
API. In order to put this integration to work there are some
pre-requirements that must be met:

  - You must have a GitHub Organization
  - The GitHub repositories must be inside this organization. Of course,
    a repository must exist before the system can interact with it.
  - You must create a "Personal access token":
    - Click on your GitHub profile picture and select "Settings"
    - Chose "Personal access tokens" on the left menu
    - Chose a description for the token
    - Select the scopes: `repo`, `public_repo`, `user`, `gist`
    - Click "Generate token"
    - Copy the generated token as we will use it later (warning: You
      cannot access the generated token after leaving the page so be
      careful to store it elsewhere)
  - You must configure a GitHub webhook inside the Organization:
    - The Payload URL must point to:
      - If you are running over HTTP (for example, through manage.py
        script):
        - `http://\<host\>:\<port\>/alliance/backlog/githubimport`
      - If you want to use HTTPS (the HTTP server must be configured):
        - `https://\<host\>:\<port\>/alliance/backlog/githubimport`
        - Remember to "Disable SSL verification" if you have a
          self-signed certificate
    - Content type: `application/json`
    - Secret: chose a strong secret
    - Which events would you like to trigger this webhook?
      - Choose "Let me select individual events" and check the "Issues"
        event.

Now we can configure the `github_settings.py` file:

    GITHUB_OWNER = "\<GitHub Organization\>"
    GITHUB_TOKEN = "\<GitHub generated token\>"
    GITHUB_WEBHOOK_SECRET = "\<The secret you created on GitHub\>"

## Running

    python manage.py runserver [host:port]

Now you can go to `\<host\>:\<port\>/admin` and login using the user
created above. You can create groups and regular users that will be used
to login into the alliance application (`\<host\>:\<port\>/alliance`).

After logging into the admin interface, create a new user, using the
same email you specified when running the `static_inserts.sql` file. The
email field will be the link between the django auth user and the
NorthBridge volunteer. Add the "Volunteers" group to the "Chosen groups"
field of the user.

Now you are ready to logout from admin account and access the
application using the regular user you have created above.

A main restriction is that the user's email must match the volunteer's
email. It is through this relation that we can link a django user and
the volunteer's informations. For now there is no database constraint
ensuring this.

