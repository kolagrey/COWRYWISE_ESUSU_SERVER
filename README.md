# ESUSU CONFAM SERVER (BUILT WITH PYTHON 3)

## How to setup the server locally

```sh
$ git clone https://github.com/kolagrey/COWRYWISE_ESUSU_SERVER.git
$ cd COWRYWISE_ESUSU_SERVER
$ python3 -m venv env
$ source env/bin/activate
$ pip install django && pip install djangorestframework
$ pip install django-cors-headers
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```

Verify the deployment by navigating to your server address in your preferred browser or REST api tool.

```sh
127.0.0.1:8000
```

Admin

```sh
127.0.0.1:8000/admin
```

API

```sh
127.0.0.1:8000/v1/
```

## Endpoints

### 1. User Registration

- http://ec2-35-180-234-171.eu-west-3.compute.amazonaws.com/v1/account/


### 2. Group Registration

- http://ec2-35-180-234-171.eu-west-3.compute.amazonaws.com/v1/account/group/


### 3. Admin's Group

- http://ec2-35-180-234-171.eu-west-3.compute.amazonaws.com/v1/admin/group/


### 3. Group Search

- http://ec2-35-180-234-171.eu-west-3.compute.amazonaws.com/v1/group/search/


### 4. Group Search by Group Code

- http://ec2-35-180-234-171.eu-west-3.compute.amazonaws.com/v1/group/code/search/


### 5. Group Contributions

- http://ec2-35-180-234-171.eu-west-3.compute.amazonaws.com/v1/group/contribution/


### 6. Group Search by Group Code

- http://ec2-35-180-234-171.eu-west-3.compute.amazonaws.com/v1/group/code/search/



### Todos

 - Authentication
 - Cron Job for automatic billing and payout
 - Testing