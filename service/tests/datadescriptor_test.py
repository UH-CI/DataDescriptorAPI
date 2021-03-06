# A suite of tests for the DataDescriptor API.
# Before you start you will need to add the following to the config-local.json file for the tests
# with working username & password for the tenant you are testing against for the other services(sk,meta,abaco etc)
#  "test_tenant_id" : "dev",
#  "test_username" :"testusername",
#  "test_password" :"testpassword"
# Build the tapis/streams-api docker container:  docker build -t tapis/streams-api:latest .
# Build the test docker image: docker build -t tapis/streams-tests -f Dockerfile-tests .
# Run these tests using the built docker image: docker run -it --rm --name=streams-test -p 5000:5000 tapis/streams-tests

# Standard library imports...
from unittest.mock import Mock, patch
# Third-party imports...
import pytest
import datetime
import json
from base64 import b64encode
# Local imports...
from service import models
from service import errors
from service import models
from service.api import app
from common.config import conf

@pytest.fixture
def client():
    app.debug = True
    return app.test_client()

def get_token_header():
    from tapipy.tapis import Tapis
    #Create python Tapis client for user
    test_tapis_client = Tapis(base_url= conf.tapis_base_url,
                             username= conf.test_username,
                             password=conf.test_password,
                             account_type='user',
                             tenant_id= conf.test_tenant_id)
    test_tapis_client.get_tokens()
    return {'X-Tapis-Token': test_tapis_client.access_token.access_token}

def test_listing_projects(client):
        with client:
            response = client.get(
                "http://localhost:5000/v3/streams/projects",
                content_type='application/json',
                headers=get_token_header()
            )
            print(f"response.data: {response.data}")
            assert response.status_code == 200
