#All New Colors: Mutliuser Flask Blog
Full-stack multiuser flask blog with SQLAlchemy database.

##GETTING STARTED

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

This assumes you have python3 and pip already installed on your machine.

###Clone repository to desired location
'''
git clone https://github.com/jakemobley/allnewcolors.git
'''

###Setup virtual environment

I use virtualenv to create isolated project environments. Use whatever virtual environment you prefer. If using virtualenv, you may use the series of commands below on mac and linux in the top level of your application directory.
'''
pip install virtualenv
virualenv "env"
source env/bin/activate
'''

###Install dependencies 
'''
pip3 install -r requirements.txt
pip freeze > requirements.txt
'''

This version uses environment variables as assignments in config.py. These will need to be set appropriate to your application. 

-Set a secret key using the method of your choice and either add to config.py or set as environment variable. 

-Within your application create a new instance of an SQLAlchemy database (see my top-level __init__.py) and add the URI in config.py.

-For password recovery email workflow configure the mail server accordingly in config.py. This example uses gmail smtp (see config.py).

###Initialize Flask development server
'''
python run.py
'''

With your development server open you can now visit the landing page in your local browser.
'''
	localhost:5000/
'''

##CUSTOMIZE / ADDITIONAL

Image files have been excluded from this repo as they are copyrighted. Take a look at .html files in the templates directory or view source from your browser to find filepaths and add/edit as you wish.

Change/add routes and templates and customize to your heart's unbridled content.

Deployment should be fairly easy using the services of your choice. I tested deployments using App Engine on Google Cloud Platform and linux servers using nginx and gunicorn.

##FAQ / CONTACT / TROUBLESHOOT

Contact me with questions at jakemobley[at]gmail[dot]com and I will answer as best I can.

##ACKNOWLEDGEMENTS

This blog was created using frameworks outlined by Corey Schaefer the great python charmer: https://coreyms.com/

This project is licensed under the MIT License - see the LICENSE.md file for details.