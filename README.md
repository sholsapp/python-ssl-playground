python-ssl-playground
=====================

A packaging of ssl-enabled gunicorn+flask server and various HTTP requests libraries for integration and stress testing.

1) Run the gunicorn server with:

  $ gunicorn --debug --log-file gunicorn.log -c gunicorn.cfg hello:app

