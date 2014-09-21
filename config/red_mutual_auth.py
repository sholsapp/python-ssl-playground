import ssl

from playground.data import get_data_file


workers = 1


keyfile = get_data_file('RED-ROOT.key')
certfile = get_data_file('RED-ROOT.cert')
ca_certs = get_data_file('RED-ca-bundle.crt')
cert_reqs = ssl.CERT_NONE
ssl_version = ssl.PROTOCOL_SSLv3
do_handshake_on_connect = True
