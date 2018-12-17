Project Vote: I Vote Lincoln!
-----------------------------
<p>
  <img align="middle" width=200 src="assets/splash_1.png">
  <img align="middle" width=200 src="assets/splash_2.png">
  <img align="middle" width=200 src="assets/main_1.png">
  <img align="middle" width=200 src="assets/main_2.png">
</p>

Project Vote is a web application written in Django that is intended to act as 
the conference management tool for the Town Hall event (to be held on 16th
 December 2018 inshAllah). See the *Key Features* section below for an overview.


Prerequisites
-------------
- Python 3+ (see requirements.txt file)


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
- Capacity: Django development server can support around 1500 clients (though
 it is ill advised to use the development server for production! Use Nginx 
 with Gunicorn instead).


Authors
-------
- Othman Alikhan
- See About page for more details


TODO_Critical
-------------
- Stress test remote development server
- Deploy Django App on a production web server (do not use manage.py!)

TODO_Regular
------------
- Improve security on production server
- Get an SSL certificate

TODO
----
- Test bootstrap being blocked internally Aramco LAN

