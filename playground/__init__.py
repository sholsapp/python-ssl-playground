import logging

from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/')
def index():
  print 'GOOD'
  return 'GOOD'


@app.route('/debug')
def debug():
    s = request.environ['gunicorn.socket']
    print 'Is secure: %s' % request.is_secure
    print 'Cert reqs: %s' % s.cert_reqs
    print 'SSL version: %s' % s.ssl_version
    print 'Cert file: %s' % s.certfile
    print 'Cert key: %s' % s.keyfile
    print 'Peer cert: %s' % s.getpeercert()
    return jsonify({
      'peer': s.getpeercert(),
    })


if __name__ == '__main__':
  logging.info('Starting the server!')
  app.run()
