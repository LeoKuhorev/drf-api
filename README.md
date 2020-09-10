# Lab-30 DRF-API

## Feature Tasks and Requirements

-   Rebuild a custom version of Blog API demo project from scratch.
    -   Replace Blog and Post with your own application and model.
    -   Your model must have at least as many fields as demo’s model.
    -   Your model must have one field that is a foreign key to user.

## AUTHORS

[_Leo Kukharau_](https://github.com/LeoKuhorev)

## GETTING STARTED:

-   `poetry shell` to start your virtual environment
-   `poetry install` to install dependencies
-   create .env file with listed <a href="#env">below</a> variables and save it into 'server' directory
-   `python manage.py makemigrations` - to generate DB schema
-   `python manage.py migrate` - to create DB schema
-   `python manage.py createsuperuser` - to create user with admin access

-   `python manage.py runserver` - to run server
    or
-   `docker-compose up` - to run server

## API:

`/` - landing page;
`api/v1/` - API endpoint;

### Dependency:

asgiref==3.2.10
autopep8==1.5.4
Django==3.1.1
djangorestframework==3.11.1  
pycodestyle==2.6.0
pytz==2020.1
sqlparse==0.3.1
toml==0.10.1

[Link to PR](https://github.com/LeoKuhorev/drf-api/pull/2)
