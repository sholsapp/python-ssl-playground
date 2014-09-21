#!/usr/bin/env python

import logging

from flask.ext.script import Manager, Command, Option

from playground import app


logging.basicConfig(level=logging.INFO)


class GunicornServer(Command):
  """Run the webserver in gunicorn."""
  def get_options(self):
    from gunicorn.config import make_settings
    settings = make_settings()
    options = (
      Option(*klass.cli, action=klass.action)
      for setting, klass in settings.iteritems() if klass.cli
    )
    return options

  def run(self, *args, **kwargs):
    from gunicorn.app.wsgiapp import WSGIApplication
    app = WSGIApplication()
    app.app_uri = 'manage:app'
    return app.run()


manager = Manager(app)
manager.add_command("gunicorn", GunicornServer())


@manager.command
def runserver(*args, **kwargs):
  """Override default `runserver` to init webapp before running."""
  app = init_webapp()
  app.run(*args, **kwargs)


if __name__ == "__main__":
  manager.run()
