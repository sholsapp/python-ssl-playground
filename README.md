python-ssl-playground
=====================

A packaging of ssl-enabled gunicorn+flask server and various HTTP requests libraries for integration and stress testing.

1) Run the gunicorn server with:

  $ gunicorn --debug --log-file gunicorn.log -c gunicorn.cfg hello:app

2) Check that the certificate validation code is happenign as expected. Use
wget. You'll see in the logs that the client certificate was passed to the
Flask request context, where we can reason about it.

$ wget --certificate=../client.cert --private-key=../client.key --no-check-certificate --secure-protocol=SSLv3 https://127.0.0.1:8000/

{'ciphers': 'TLSv1', 'certfile': 'riddler.cert', 'suppress_ragged_eofs': True, 'do_handshake_on_connect': True, 'ssl_version': 2, 'cert_reqs': 1, 'ca_certs': 'root-ca.cert', 'keyfile': 'riddler.key'}
Is secure: True
Cert reqs: 1
SSL version: 2
Cert file: riddler.cert
Cert key: riddler.key
Peer cert: {'notAfter': 'Mar  5 21:45:26 2034 GMT', 'subject': ((('countryName', u'US'),), (('stateOrProvinceName', u'CA'),), (('organizationName', u'Tools'),), (('organizationalUnitName', u'Riddler Client'),), (('commonName', u'Riddler Client'),))}

3) Check that by passing no certificate, the request works, but doesn't
provide a client certificate. Again, we can reason about this in the Flask
request context.

$ wget --no-check-certificate --secure-protocol=SSLv3 https://127.0.0.1:8000/

{'ciphers': 'TLSv1', 'certfile': 'riddler.cert', 'suppress_ragged_eofs': True, 'do_handshake_on_connect': True, 'ssl_version': 2, 'cert_reqs': 1, 'ca_certs': 'root-ca.cert', 'keyfile': 'riddler.key'}
Is secure: True
Cert reqs: 1
SSL version: 2
Cert file: riddler.cert
Cert key: riddler.key
Peer cert: None
