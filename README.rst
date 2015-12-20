SuperZapatos Django Services
==============================

SuperZapatos Web Services.
Using Django 1.9 and Django Rest Framework 3.3.2

Live DEMO
---------

http://ec2-52-89-15-237.us-west-2.compute.amazonaws.com/

Services
--------

    GET /services/stores/
    GET /services/stores/articles/
    GET /services/stores/articles/<id>


Running BDD tests
-----------------

Install tests requirements:

    $ pip install -r requirements/tests.txt


Run tests in Test Database mode:

    $ python manage.py harvest -T

This project uses `Lettuce <http://lettuce.it/>`_ for BDD testing. The current  
version does not work for Django 1.7+ This compatibility was fixed in the fork
https://github.com/andresgz/lettuce that is references in the requirements of 
this project.