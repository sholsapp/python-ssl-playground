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

The following is a survey of several common tools used to interact with systems
that use TLS/SSL regarding how they fair when using gunicorn as the TLS/SSL
termination point.

## openssl

```bash
openssl s_client \
  -connect 0.0.0.0:8000 \
  -cert playground/data/RED-INTERMEDIATE_ALPHA-CLIENT.cert \
  -key playground/data/RED-INTERMEDIATE_ALPHA-CLIENT.key
  -CAfile playground/data/RED-ca-bundle.crt \
```

### problems 

- Doesn't appear that client certificate is asked for from server even when run
  with CERTS_REQUIRED.

## wget

```bash
wget \
  --certificate playground/data/RED-INTERMEDIATE_ALPHA-CLIENT.cert \
  --private-key playground/data/RED-INTERMEDIATE_ALPHA-CLIENT.key \
  --ca-certificate playground/data/RED-ca-bundle.crt \
  --no-check-certificate \
  https://0.0.0.0:8000/debug
```

### problems

- Current certificates do not pass `wget` validation.

## curl

```curl
curl \
  --cacert playground/data/RED-ca-bundle.crt \
  --cert playground/data/RED-INTERMEDIATE_ALPHA-CLIENT.cert \
  --key playground/data/RED-INTERMEDIATE_ALPHA-CLIENT.key \
  https://0.0.0.0:8000/debug
```

### problems

- Current certificates do not pass `curl` validation.
