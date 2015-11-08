# Deployment

## Production deploy

### Prerequisites:  
* Heroku toolbelt installed
    https://devcenter.heroku.com/articles/getting-started-with-python#set-up

### Steps

1. After code complete, pull from alliance-community to alliance-ship

2. On local machine, execute

    `git clone <alliance-ship>` or `git pull <alliance-ship>`
    
    `cd alliance-ship`
    
    `git remote add heroku git@heroku.com:alliance-dev.git`
    
    `heroku login`
    
    `heroku keys:add`
    
    `git push heroku`

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
