# django-animal-shelter
Django website template for animal shelters.

## what is it?
This is just a training/showcase dynamic website made in as the code I wrote in my previous positions belongs to my former employers and thus I can't easily share it.
Or at least without heavily pruning it. /!\ Obviously it is not ready for production at all /!\

## why spa as a project name?
It comes from the name of the main animal protection association in France, the "Société Protectrice des Animaux" 

## branches and evolution
This project will span over a couple of days (a week or so?) with an update at least once a day.
Master branch = stable version
Dev branch = most advanced but probably broken version

## how to test it?
Dev and test platform :
    - Ubuntu 15.04
    - make sur you have pip and virtualenv installed
    - create a new virtualenv and install the required librairies (pip -r < django-spa/requirements.txt)
    #- create a superuser "python manage.py createsuperuser", give it whatever name you want
    #- optional: you can pre-populate the database by applying a fixture "HOW TO"
    - cd to the main folder containing the manage.py and run "python manage.py runserver"
    - you should be able to access the website locally by following the URL : "http://127.0.0.1:8080"
    
## credits
Images, artwork etc :

Theme template:
html5up