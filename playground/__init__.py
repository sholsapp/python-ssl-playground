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
  print 'flask.request.is_secure = [%s]' % request.is_secure
  print 'flask.request.environ["gunicorn.socket"].cert_reqs = [%s]' % s.cert_reqs
  print 'flask.request.environ["gunicorn.socket"].ssl_version = [%s]' % s.ssl_version
  print 'flask.request.environ["gunicorn.socket"].certfile = [%s]' % s.certfile
  print 'flask.request.environ["gunicorn.socket"].keyfile = [%s]' % s.keyfile
  print 'flask.request.environ["gunicorn.socket"].getpeercert() = [%s]' % s.getpeercert()
  return jsonify({
    'peer': s.getpeercert(),
  })


if __name__ == '__main__':
  logging.info('Starting the server!')
  app.run()
