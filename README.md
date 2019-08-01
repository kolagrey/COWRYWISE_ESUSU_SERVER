# ESUSU CONFAM SERVER (BUILT WITH PYTHON 3)

## How to setup the servers
1. python3 -m venv env
2. source env/bin/activate
3. python3 manage.py makemigrations
4. python3 manage.py migrate
5. python3 manage.py runserver

There are three different servers running the following services

### 1. Authentication Services, AUTH-SERVER
This service is reponsible for handing user authentication, password reset, and password update request

###2. Data Services, DATA-SERVER
This service is reponsible for handing user | group | contributions | Payout information resource access and management request

###3. Identity Services, ID-SERVER
This service is reponsible for handing user registration and verification request

## How to setup the website (Demo Esusu Platform using the services above)
The demo website, built with VueJS, ca


