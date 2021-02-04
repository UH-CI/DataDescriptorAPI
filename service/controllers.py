import datetime
from flask import g, request, make_response
from flask_restful import Resource
from openapi_core.shortcuts import RequestValidator
from openapi_core.wrappers.flask import FlaskOpenAPIRequest
# import psycopg2
#import sqlalchemy
#from service.models import ChordsSite, ChordsIntrument, ChordsVariable
from common import utils, errors
from common.config import conf
from requests.auth import HTTPBasicAuth
from common import errors as common_errors
from service import auth
from datetime import datetime

#from service.models import db, LDAPConnection, TenantOwner, Tenant

import requests
import json
import sys
# get the logger instance -
from common.logs import get_logger
logger = get_logger(__name__)

class HelloResource(Resource):
    def get(self):
        logger.debug('In hello resource')
        return utils.ok(result='',msg="Hello from DataDescriptorAPI")

class DataDescriptorsResource(Resource):
    def get(self):
        logger.debug('In DataDescriptors resource')
        return utils.ok(result='',msg="GET  DataDescriptors")

    def post(self):
        logger.debug('In DataDescriptors resource')
        return utils.ok(result='',msg="GET  DataDescriptors")

class DataDescriptorResource(Resource):
    def get(self, data_descriptor_id):
        logger.debug('In DataDescriptor resource. ID: '+data_descriptor_id)
        return utils.ok(result='',msg="GET  DataDescriptor")

    def put(self):
        logger.debug('In DataDescriptor resource')
        return utils.ok(result='',msg="GET  DataDescriptor")

    def delete(self):
        logger.debug('In DataDescriptor resource')
        return utils.ok(result='',msg="GET  DataDescriptor")
