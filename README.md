[![Build Status](https://travis-ci.org/ffabiorj/codenation_logs.svg?branch=master)](https://travis-ci.org/ffabiorj/codenation_logs)

[![codecov](https://codecov.io/gh/ffabiorj/codenation_logs/branch/master/graph/badge.svg)](https://codecov.io/gh/ffabiorj/codenation_logs)


# CODENATION LOGS API
I developed this project to stored logs in a database.

### Documentation of API
[Link](https://app.swaggerhub.com/apis-docs/ffabiorj/logs/1.0.0-oas3) 


## Tools
* Django
* Django Rest FrameWork
* JWT
* Postgres
* Heroku (Cloud)

## Production
[link](https://codenation-logs.herokuapp.com/api/v1/logs/)

To test de api
```
username: teste password: teste
```

## How to run locally.

1. Clone the repository.
2. Enter the folder
3. Create an enviroment with python 3.8.
4. Active the enviroment.
5. Install the dependencies.
6. Rename the file env_exemplo
7. Run migrations
8. Create an user
9. Run the project
10. Create a token
11. Access the link


```
- git clone git@github.com:ffabiorj/codenation_logs.git
- cd codenation_logs
- python3 -m venv .venv
- sourch .venv/bin/activate
- pip install -r requirements-dev.txt
- mv .env_exemplo .env
- python manage.py migrate
- python manage.py shell
  from django.contrib.auth.models import User
  user = User.objects.create_user(username=<yourname>', password='<password>')
  user.save()
- python manage.py runserver
- http://127.0.0.1:8000/api/v1/token/ username=<user> password=<password>
- http://127.0.0.1:8000/api/v1/logs/

```

##
Endpoints of api
- http://127.0.0.1:8000/api/v1/token/ # pass an username and password.
- http://127.0.0.1:8000/api/v1/token/refresh/ # refresh token
- http://127.0.0.1:8000/api/v1/logs/ # search ou return all logs if does not match.
- http://127.0.0.1:8000/api/v1/log/ # return all logs.
- http://127.0.0.1:8000/api/v1/log/<id>/ # return one log if exists.


### Run tests
```
pytest
```

### Links for tools
[Django](https://docs.djangoproject.com/)

[Django Rest Framework](https://www.django-rest-framework.org/)

[Codecov](https://codecov.io/)

[Travis](https://travis-ci.com/)

[Heroku](https://dashboard.heroku.com/)