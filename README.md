# Basic scrappping with django, requests library and beautifulsoup

## Intro
A default user is also provided for token based authorization using django-rest-framework present in the
   "user_app" app. So instead of usign django's default User class we will use this ApiUser class.


Default url for login is which uses a default POST request which you are free to override:

    /api/login/

which returns the username and token for the user.

Once we have the token we can add the following header to requests to auth:

    Authorization: "token {newly_generated_token}"

Replace the newly_generated_token with your token


### Running the project


Copy the .env.example file as .env and fill the secret token there.

Run this command

```
./setup.bash
```
If successfull, you can run a django local server by using this command:

```
python manage.py runserver
```

Running this command will run a server at localhost:8000/127.0.0.1:8000.

The setup.bash command requires pip3 command be available if your system has a different name for python 3 pip please change it in the script.
