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

### Prerequisites  

* Heroku CLI installed
    https://devcenter.heroku.com/articles/getting-started-with-python#set-up

### Commands

To tail server logs, from local terminal, project root
```
heroku logs --tail
```

To tail application logs
```
heroku logs --source app --tail
```

More about Heroku logging [here](https://devcenter.heroku.com/articles/logging#view-logs)

To browse database, from local terminal, project root
```
heroku pg:psql
```

To start a shell session and view application logs
```
heroku run bash
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

### Handy Queries

Retrieve story name, team, sprint and estimate
```
select t.name, e.estimate, b.story_title, b.sprint_id_fk from backlog b join team t on b.team_id_fk = t.id join estimate e on e.backlog_id_fk = b.id where b.id = 79;
```

