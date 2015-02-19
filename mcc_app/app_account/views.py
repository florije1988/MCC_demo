# -*- coding: utf-8 -*-
__author__ = 'boqingfu'

from flask import request
from flask.ext.restful import reqparse

from ..basic_handler import BaseHandler
from ..custom_exception import InvalidAPIUsage


class HelloHandler(BaseHandler):
    def get(self):
        return self.json_output({'hello': 'fuboqing'})