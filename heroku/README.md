# Heroku Deployment
Heroku PaaS was used to deploy these apps. <i>Heroku CLI</i> provides the option to directly push the repo aur app to heroku to be deployed. The OS in use is Ubuntu.
## Blog post with more details:
Deploying ML Apps on Heroku
## Installing Heroku CLI : 
```$ sudo snap install --classic heroku```

## Creating a Heroku app :
``` $ heroku create appname. ```
### Deploying the Backend of the server:
While Deploying the backend sever make sure to include the <b>Procfile</b> in your git repository which tells the heroku from where to start the <i>web app</i>. Contents of <i>Procfile - </i><br>
``` 
web: gunicorn main:app
```
Open the terminal in the server folder and follow the following steps
``` 
$ git init
$ heroku git:remote -a appname
$ git add .
$ git commit -m “your message”
$ git push heroku master 
```
The link for the server is created. Update the server link in the config.js inside <i><b>frontend/src</b></i>
### Deploying the frontend:
After the link is created and updated inside config.js in the src folder follow the following steps to <b>deploy frontend</b>. Create another app using <br>
``` $ heroku create complete_app.```<br><br>
Open the terminal in the frontend folder and follow the following steps.
```$ git init
$ heroku git:remote -a appname
$ git add .
$ git commit -m “your message”
$ git push heroku master 
```
<b>NOTE : </b> While Deploying the given codebase in <b><i>frontend</b></i> make sure to remove the <i>'-p 8000'</i> which is the local port from <i>scripts</i> in <i><b>package.json</i></b> located in <b><i>frontend/package.json</b></i><br>
The final app link will be generated which can be used for the purpose.<br>
The same method above can be used to deploy the <i><b>streamlit app<i><b>
