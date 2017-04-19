#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import environ as env
from sys import argv
from urllib2 import urlopen

import bottle
from bottle import default_app, request, route, response, get

from json import dumps

import utils
import db

bottle.debug(True)

@get('/api/parse-url')
def parse_url():

    url = request.query.url

    response = urlopen(url)

    raw = response.read()

    parsed_dict = utils.parse_markdown(raw)

    return parsed_dict

@get('/api/search')
def search():

    query_string = request.query.text

    results = db.text_search(query_string)

    response.content_type = 'application/json'

    return dumps(results)


bottle.run(host='0.0.0.0', port=argv[1])
