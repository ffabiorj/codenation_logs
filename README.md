[![Build Status](https://travis-ci.org/ffabiorj/codenation_logs.svg?branch=master)](https://travis-ci.org/ffabiorj/codenation_logs)

[![codecov](https://codecov.io/gh/ffabiorj/codenation_logs/branch/master/graph/badge.svg)](https://codecov.io/gh/ffabiorj/codenation_logs)


# CODENATION LOGS API
I developed this project to stored logs in a database.

### Documentation of API
[Link](https://app.swaggerhub.com/apis-docs/ffabiorj/logs/1.0.0) 


## Tools
* Django
* Django Rest FrameWork
* Postgres
* Heroku (Cloud)

## How to run locally.

1. Clone the repository.
2. Enter the folder
3. Create an enviroment with python 3.8.
4. Active the enviroment.
5. Install the dependencies.
6. Rename the file env_exemplo
7. Run migrations
8. Create an user
9. Create a token
10. Run the project
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
  user = User.objects.create_user('yourname', password='your password')
  user.save()
- python manage.py drf_create_token <username>
- python manage.py runserver
- http://127.0.0.1:8000/api/v1/logs/
```

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
