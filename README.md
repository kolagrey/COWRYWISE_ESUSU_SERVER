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

## Endpoints on AWS

### 1. User Registration

- http://ec2-35-180-234-171.eu-west-3.compute.amazonaws.com/v1/accounts/

#### Usage (POST)

```sh
# Body Parameters
firstname [REQUIRED][string]
​lastname [REQUIRED][string]
email [REQUIRED][string]
mobile [REQUIRED][string]
```

```sh
# Reponse
{
  "account_id": 1,
  "firstname": "Temi",
  "lastname": "Grey",
  "email": "temi@asheori.com",
  "mobile": "07033020200",
  "created": "2019-08-01T09:35:22.054841Z"
}
```


### 2. Group Registration

- http://ec2-35-180-234-171.eu-west-3.compute.amazonaws.com/v1/account/groups/

#### Usage (POST)

```sh
# Body Parameters
group_name [REQUIRED][string]
​group_description [OPTIONAL][string]
group_admin [REQUIRED][string][email]
maximum_capacity [REQUIRED][number]
contribution_amount [REQUIRED][number]
searchable [OPTIONAL][boolean][default=false]
```

```sh
# Reponse
{
  "group_id": 1,
  "group_name": "Google",
  "group_description": "For people contributing N50,000 per week",
  "group_admin": "admin@email.com",
  "maximum_capacity": 50,
  "contribution_amount": 50000,
  "group_code": "113537",
  "searchable": true,
  "created": "2019-08-02T11:55:33.650699Z"
}
```


### 3. Admin's Group

- http://ec2-35-180-234-171.eu-west-3.compute.amazonaws.com/v1/admin/group/

#### Usage (GET)

```sh
# URL Parameters
email=[admin email]
# Example
http://ec2-35-180-234-171.eu-west-3.compute.amazonaws.com/v1/admin/group?email=admin@email.com
```

```sh
# Reponse
{
  "group_id": 1,
  "group_name": "Google",
  "group_description": "For people contributing N50,000 per week",
  "group_admin": "admin@email.com",
  "maximum_capacity": 50,
  "contribution_amount": 50000,
  "group_code": "113537",
  "searchable": true,
  "created": "2019-08-02T11:55:33.650699Z"
}
```


### 3. Group Search

- http://ec2-35-180-234-171.eu-west-3.compute.amazonaws.com/v1/group/search/

#### Usage (GET)

```sh
# URL Parameters
search_params=[search text or phrase]
# Example
http://ec2-35-180-234-171.eu-west-3.compute.amazonaws.com/v1/group/search?search_params=admin@email.com
```

```sh
# Reponse
{
  "group_id": 1,
  "group_name": "Google",
  "group_description": "For people contributing N50,000 per week",
  "group_admin": "admin@email.com",
  "maximum_capacity": 50,
  "contribution_amount": 50000,
  "group_code": "113537",
  "searchable": true,
  "created": "2019-08-02T11:55:33.650699Z"
}
```


### 4. Group Search by Group Code

- http://ec2-35-180-234-171.eu-west-3.compute.amazonaws.com/v1/group/code/search/

#### Usage (GET)

```sh
# URL Parameters
code=[group code]
# Example
http://ec2-35-180-234-171.eu-west-3.compute.amazonaws.com/v1/group/code/search?code=113537
```

```sh
# Reponse
{
  "group_id": 1,
  "group_name": "Google",
  "group_description": "For people contributing N50,000 per week",
  "group_admin": "admin@email.com",
  "maximum_capacity": 50,
  "contribution_amount": 50000,
  "group_code": "113537",
  "searchable": true,
  "created": "2019-08-02T11:55:33.650699Z"
}
```


### 5. Group Contributions

- http://ec2-35-180-234-171.eu-west-3.compute.amazonaws.com/v1/group/contribution/

#### Usage (GET)

```sh
# URL Parameters
identifier=[group id]
# Example
http://ec2-35-180-234-171.eu-west-3.compute.amazonaws.com/v1/group/contribution?identifier=1
```

```sh
# Reponse
[
    {
        group: {
        "group_id": 1,
        "group_name": "Google",
        "group_description": "For people contributing N50,000 per week",
        "group_admin": "admin@email.com",
        "maximum_capacity": 50,
        "contribution_amount": 50000,
        "group_code": "113537",
        "searchable": true,
        "created": "2019-08-02T11:55:33.650699Z"
        }
        user: {
            "account_id": 1,
            "firstname": "Temi",
            "lastname": "Grey",
            "email": "temi@asheori.com",
            "mobile": "07033020200",
            "created": "2019-08-01T09:35:22.054841Z"
        }
        contribution_amount: 50000,
        contribution_date: "2019-08-02T12:45:20.190609Z"
    }
]
```



## Todos

 - Authentication
 - Cron Job for automatic billing and payout
 - Testing