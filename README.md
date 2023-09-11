## ABOUT THE APP.

The App is a flask Application with context revolving around the English Premier League for Season 2023/2024. It contains a carousel of the all the Logos of the 20 participating Teams in the 2023/2024 Season.

## WSGI WEBSERVER.

This App contains a WSGI Server which converts Python's single-threaded apps such a Flask to a multi-thread one, to handle concurrency. It also binds the app to a listening port or socket. The WSGI Server used for this Application is Gunicorn.

## REVERSE PROXY SERVER:

Nginx is used as a reverse proxy server, it acts as an intermediary between the enduser and the app, the doubles as both a reverse proxy server and a Load Balancer. This reverse proxy server listens on the a defined endpoint to the exposed port or unix port.

![EPLStatusReport](https://github.com/nugowe/Flask-EPLStatusReport/assets/25004712/bd537abe-815b-4d1c-9dfc-f995b63294d3)




