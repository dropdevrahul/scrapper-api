# A sample template for starting a new django project along with docker files for the same with some sensible defaults.

## Intro
A default user is also provided for token based authorization using django-rest-framework present in the
   "user_app" app. So instead of usign django's default User class we will use this ApiUser class.


Default url for login is which uses a default POST request which you are free to override:

    /api/login/

which returns the username and token for the user.

Once we have the token we can add the following header to requests to auth:

    Authorization: "token newly_generated_token"

Replace the newly_generated_token with your token

## Docker image creation

Create Docker Image

    docker-compose up -d build

Find image name by running the following command and seeing the image name for the the running container

    docker container ls

Save the running container to an image

    docker save --output OUTPUT_FILEPATH.tar image_name

Load the saved image

    docker load < OUTPUT_FILEPATH.tar

Find the name of the image

    docker images

Run the command to run container:

    docker run -t -d -p 8080:8080 image_name

If your docker container uses environment variables use the --env-file option to add a file with all variables
in this format:

    VAR=VALUE

<b>Please note that environment variables have to de declared in the docker-compose file as well if you want to use the docker-compose up command</b>

Without any quotes for values

    docker run -t -d -p 8080:8080 --env-file filepath image_name




