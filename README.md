Project Vote: I Vote Lincoln!
-----------------------------
<p>
  <img align="middle" width=200 src="assets/splash_1.png">
  <img align="middle" width=200 src="assets/splash_2.png">
  <img align="middle" width=200 src="assets/main_1.png">
  <img align="middle" width=200 src="assets/main_2.png">
</p>


Project Vote is a web application written in Django that was used as the 
realtime Q&A tool for a company wide event named "Town Hall". This
event took place on 16th December 2018 and with an audience of 3,000 people.
See the [Key Features](#Key-Features) section below for an overview.


Prerequisites
-------------
- Python 3+ (see requirements.txt file)
- Django 2.1.4+
- Gunicorn 19.9.0 (only for deployment)
- Nginx 1.14.2+ (only for deployment)


How to Run
----------
1. Install all the dependencies (e.g. `pip install -r requirements.txt`).
2. Run the django test server via invoking `python manage.py runserver`.
3. Launch a browser and connect to the server (e.g. 127.0.0.1:8000/admin).


Key Features
------------
- Authentication: Splash page requires a session ID
- Q&A: Allows posting and viewing of moderated questions.
- Moderation: Questions posted are sent to backend for moderation approval.
- Capacity: ~2,000 clients. 

Note: The bottleneck of the web application is the authentication page which 
can only support 2,000 HTTP requests within 1 minute (tested with Gunicorn
and Nginx). Other pages support more than 10,000 HTTP requests per minute.

As a reference, the django development server can support around 1500 clients 
(though it is ill advised to use the development server for production! Use 
Nginx with Gunicorn instead).


Authors
-------
- Othman Alikhan
- See About page for more details.
