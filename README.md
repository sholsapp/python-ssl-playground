python-ssl-playground
=====================

A packaging of ssl-enabled gunicorn+flask server and various HTTP requests
libraries for integration and stress testing.

# running the server

Start the server using Flask-Script and the custom `gunicorn` command. You'll
have to pick a gunicorn configuration to start the server with. Choose one from
those provided in the config directory or write your own by referring to the
[gunicorn guide](http://docs.gunicorn.org/en/latest/configure.html).

```bash
./manage.py gunicorn -c config/red_server_auth.py
```
# tests

```bash
wget \
  --certificate RED-INTERMEDIATE_ALPHA-CLIENT.cert \
  --private-key RED-INTERMEDIATE_ALPHA-CLIENT.key \
  --ca-certificate RED-ca-bundle.crt \
  --no-check-certificate \
  https://0.0.0.0:8000/debug
```

# todo

- Figure out why so many programs are failing to verify the certificates that
  the bin/generate-identites tool creates. They fail for very HTTP-centric
  reasons so far, viz., common name doesn't match host name.

