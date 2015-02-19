# -*- coding: utf-8 -*-
__author__ = 'boqingfu'

from mcc_app import create_app

app = create_app('development')


if __name__ == '__main__':
    app.run(port=app.config.get('PORT'), host=app.config.get('HOST'))