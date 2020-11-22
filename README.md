News App

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Development environment setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  $ docker-compose build

  $ docker-compose up


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Migrations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


  $ docker-compose run --rm web python manage.py makemigrations

  $ docker-compose run --rm web python manage.py migrate


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Run shell
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  $ docker-compose run --rm web python manage.py shell
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Note: ".env" file is shared in email.
Please add email and password for sending emails.
Migrations will be executed initially and super user will be by default created from settings.base.ADMINS.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Thanks for Reading
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
