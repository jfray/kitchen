#!/usr/bin/env python
from flask import Flask
from flask_mongoengine import MongoEngine
 
app = Flask(__name__)
app.config.from_pyfile("/Users/josh/src/kitchen/flask/mongolab/kitchen.cfg")

db = MongoEngine(app)

def register_blueprints(app):
  from kitchen.views import posts
  app.register_blueprint(posts)
 
register_blueprints(app)
 
if __name__ == '__main__':
  app.run(debug=True)
