----All_New_Colors__Mutliuser_FLask_Blog----

Full-stack multiuser flask blog with SQLAlchemy database.

--Getting Started--

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

1) Assumes you have python3 and pip already installed on your machine.

) Clone repository to desired location

	git clone 

) Setup virtual environment

I use virtualenv to create an isolated project environment. Use whatever virtual environment you prefer. For virtualenv, you may use the series of commands below on mac and linux in the top level of your application directory.

	pip install virtualenv
	virualenv "env"
	source env/bin/activate

) Install dependencies 

	pip3 install -r requirements.txt
    pip freeze > requirements.txt

This version uses environment variables as assignments in config.py. These will need to be set appropriate to your application. 
-Set a secret key using the method of your choice and either add to config.py or set as environment variable. 
-Within your application create a new instance of an SQLAlchemy database (see my top-level __init__.py) and add the URI in config.py.
-For password recovery email workflow configure the mail server accordingly in config.py. This example uses gmail smtp (see config.py).

