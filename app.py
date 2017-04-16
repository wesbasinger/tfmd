#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import environ as env
from sys import argv
from urllib2 import urlopen

import bottle
from bottle import default_app, request, route, response, get

import utils

bottle.debug(True)

@get('/api/parse-url')
def parse_url():

    url = request.query.url

    response = urlopen(url)

    raw = response.read()

    parsed_dict = utils.parse_markdown(raw)

    return parsed_dict


bottle.run(host='0.0.0.0', port=argv[1])
