from flask_migrate import Migrate

from common.utils import TapisApi, handle_error, flask_errors_dict

from service.auth import authn_and_authz
from service.controllers import HelloResource, DataDescriptorsResource, DataDescriptorResource
from service.models import app

from common.logs import get_logger
logger = get_logger(__name__)

# authentication and authorization ---
@app.before_request
def authnz_for_authenticator():
    authn_and_authz()
    logger.debug("Authorization complete")

# flask restful API object ----
api = TapisApi(app, errors=flask_errors_dict)

# Set up error handling
api.handle_error = handle_error
api.handle_exception = handle_error
api.handle_user_exception = handle_error

# Add resources
api.add_resource(HelloResource, '/hello')

api.add_resource(DataDescriptorsResource, '/dd')
api.add_resource(DataDescriptorResource, '/dd/<data_descriptor_id>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
