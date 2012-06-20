#!/usr/bin/env python

from flask import Flask, render_template, flash, request, redirect, url_for, Markup
from flaskext.couchdb import (CouchDBManager, Document, TextField, Mapping,
                              DateTimeField, ViewField, paginate, DictField)
from couchdb.client import Server
import os
import sys
import json
import datetime
import uuid
import requests
import random

app = Flask(__name__)

u,p = open('%s/.secure/kitchen/auth' % os.environ['HOME']).read().strip().split('::') 
COUCHDB_SERVER = "https://%s:%s@%s.cloudant.com/" % (u,p,u)
COUCHDB_DATABASE = 'kitchen'
SECRET_KEY = 'set this to something secret'
TYPO_URL="http://typograffit.com/rest_json/posts/generate/body:"

app.config.from_object(__name__)

class Signature(Document):
  message = TextField()
  author = TextField()
  time = DateTimeField(default=datetime.datetime.now())

  all = ViewField('guestbook', '''
          function (doc) {
            emit(doc.time, doc);
          }''', descending=True)

manager = CouchDBManager()
manager.add_document(Signature)
manager.setup(app)

@app.route('/')
def display():
  kitchen_ids = json.load(open('./pic_ids.json'))
  pic = random.choice(kitchen_ids)
  page = paginate(Signature.all(), 5, request.args.get('start'))
  return render_template('display.html', page=page, pic=pic)

@app.route('/', methods=['POST'])
def post():
  message = request.form.get('message')
  author = request.form.get('author')
  if not message or not author:
    flash('You must fill in both a message and an author')
  else:
    signature = Signature(message=message, author=author)
    signature.store()
    flash('Signature stored')
  return redirect(url_for('display'))

if __name__ == '__main__':
  app.run(debug=True)
