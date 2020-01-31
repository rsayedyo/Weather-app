# Installation:
### prerequisites:
 * Python 3


### Install instructions:
Follow the installation instructions on https://docs.djangoproject.com/en/3.0/intro/install/.


#### Installing pip:
##### 1)download get-pip file by running:
`$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`

Now run this file to install pip:
`$ python3 get-pip.py`

If you run into a permission error in the previous step, use --user instead:

`$ Python3 get-pip.py --user`

##### 2)installing Django using pip:
`$ python3 -m pip3 install Django --user`

to check the version:

`$ python3 -m django --version`

# Create your project directory
Create a Django project, cd into your working directory and start your project: https://docs.djangoproject.com/en/3.0/intro/tutorial01/


```
$mkdir ~/djangoproject &&
$ django-admin startproject mysite
```

Change into the weatherApp directory that was created in the previous step (automatically using startproject)

# Errors running the server
Here's some of the error I encountered and how I troubleshooted them.


### Cannot import PATH
>Upgrading to Python3 to use the Django.import URLS package (which is only supported in verion 2.0 & < ) Python 2.x cannot update Django, so you'll need to upgrade python

1) Upgrade to python3 using brew

`$ brew install python3`


I ran into the following erorr on my mac machine running python 2.7:

>Error: The following formula
  python
cannot be installed as binary package and must be built from source.
Install the Command Line Tools: xcode-select --install

run:

`$ xcode-select --install`

Which promoted installing a developer tool software, retry installing Python3

`$ brew install python3`

2) Update Django using pip3

`$ pip3 install -U django`

3) Check the version of Django installed:

open a python3 shell and run, and make sure it's python3 not python2.X (both versions will co-exists)

```
$ import django
$ django.VERSION
```

### Cannot import requests
install the reqests module with pip3 not pipenv. (pipenv is a python2 venv; if you run it it will use python 2 modules and the other modules wont run (import path for example)

`$ pip3 install requests`

### Django: OperationalError No Such Table
`$ python3 manage.py && migrate --run-syncdb`
