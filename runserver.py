# -*- coding: utf-8 -*-
__author__ = 'boqingfu'

from mcc_app import create_app
from flask import current_app, request
from datetime import datetime

app = create_app('development')


@app.before_request
def log_request_data():
    current_app.logger.warning(
        "Req----Time:~~~%r --------> remote_addr = %s, url = %s, data = %r, args = %r, values = %r" %
        (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), request.remote_addr, request.url,
         request.data, request.args, request.values))


# @app.errorhandler(500)
# @app.errorhandler(404)
# def handle_error(error):
#     response = {
#         'code': 1000,
#         'msg': 'Server raise error: %s' % (error.message,),
#         'data': {}
#     }
#     current_app.logger.warning('Res----Time:~~~%r -------->  %r'
#                                % (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), response))
#     return response, 200


if __name__ == '__main__':
    app.run(port=app.config.get('PORT'), host=app.config.get('HOST'))