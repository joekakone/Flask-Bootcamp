#!/usr/bin/env python
# coding : utf-8

"""
    Flask CHallenge #01 : URL Shortner
"""

import datetime
import urllib

from flask import Flask, render_template, request, url_for, redirect

from app import app, db, hashids
from app.models import Url

def transform_url(hashids, input_url):
    return urllib.parse.urljoin(app.config["BASE_URL"], hashids.encode(input_url))

@app.route("/")
def index():
    urls = Url.query.all()
    return render_template('index.html', urls=urls)

# Create
@app.route("/url/create", methods=['GET', 'POST'])
def create_url():
    if request.method == "POST":
        name = request.form.get('name')
        input_url = request.form.get('url')

        # Create URL item in database
        url = Url(name=name,
                  long_url=input_url,
                  created_date=datetime.datetime.now())
        db.session.add(url)
        db.session.commit()

        # Create the short URL
        output_url = transform_url(hashids, url.id)
        url.short_url = output_url
        db.session.commit()

        return redirect(url_for('view_url', id=url.id))

    return render_template('create_url.html')

# Read
@app.route("/url/<int:id>/details", methods=['GET'])
def view_url(id):
    url = Url.query.get_or_404(id)

    return render_template('view_url.html', url=url)

# Update
@app.route("/url/<int:id>/update", methods=['GET', 'POST'])
def update_url(id):
    url = Url.query.get_or_404(id)

    if request.method == "POST":
        url.long_url = request.form.get("url")
        db.session.commit()

        return redirect(url_for('view_url', id=url.id))

    return render_template('update_url.html', url=url)

# Delete
@app.route("/url/<int:id>/delete", methods=['GET', 'POST'])
def delete_url(id):
    url = Url.query.get_or_404(id)
    db.session.delete(url)
    db.session.commit()

    return redirect(url_for('index'))
