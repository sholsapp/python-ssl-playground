import ssl

from playground.data import get_data_file


workers = 1


keyfile = get_data_file('RED-INTERMEDIATE_ALPHA-SERVER.key')
certfile = get_data_file('RED-INTERMEDIATE_ALPHA-SERVER.cert')
ca_certs = get_data_file('RED-ca-bundle.crt')
cert_reqs = ssl.CERT_OPTIONAL
ssl_version = 3
do_handshake_on_connect = True
