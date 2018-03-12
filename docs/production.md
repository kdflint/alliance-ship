# Production Tasks

## Production Deploy

### Automated Deploy Steps

1. Currently, pushing to code branch master in private repository `kdflint/alliance-ship` will cause Heroku to trigger a deployment automatically. Visit the Heroku [application dashboard](https://dashboard.heroku.com/apps/alliance-dev/deploy/github) for further details and options.

### Manual Deploy Steps

These are for reference only. 

1. After code complete, pull from `NorthBridge/alliance-community` to `kdflint/alliance-ship`

2. On local machine, execute

    If necessary: `git clone https://github.com/kdflint/alliance-ship.git` 
    
    Else: `git pull <alliance-ship>`
    
    `cd alliance-ship`
    
    If necessary: `git remote add heroku git@heroku.com:alliance-dev.git`
    
    `heroku login`
    
    If necessary: `heroku keys:add`
    
    `git push heroku` (This will invoke the actual deployment.)

3. Smoketest the app at https://alliance-dev.herokuapp.com/alliance/apps/backlog

Sample output from a code push (which invokes a deployment automatically)

```
remote: Compressing source files... done.  
remote: Building source:  
remote:   
remote: -----> Using set buildpack heroku/python  
remote: -----> Python app detected  
remote: -----> Installing dependencies with pip  
remote:   
remote: -----> Preparing static assets  
remote:        Collectstatic configuration error. To debug, run:  
remote:        $ heroku run python alliance/manage.py collectstatic --noinput  
remote:   
remote:   
remote: -----> Discovering process types  
remote:        Procfile declares types -> web  
remote:   
remote: -----> Compressing... done, 44.2MB  
remote: -----> Launching... done, v106  
remote:        https://alliance-dev.herokuapp.com/ deployed to Heroku  
remote:   
remote: Verifying deploy.... done.  
```

## Production Support Notes

### Prerequisites:  
* Heroku toolbelt installed
    https://devcenter.heroku.com/articles/getting-started-with-python#set-up

To tail server logs, from local terminal, project root
```
heroku logs --tail
```

To browse database, from local terminal, project root
```
heroku pg:psql
```

To start a shell session and view application logs
```
heroku run bash
```

To view application logs, in heroku shell
```
view ~/logs/alliance.log
```

To migrate, in heroku shell
```
python ~/alliance/manage.py migrate
```

To view django settings, in heroku shell
```
python ~/alliance/manage.py diffsettings
```

[Heroku environment documentation](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)
