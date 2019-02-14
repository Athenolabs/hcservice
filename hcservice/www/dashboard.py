

import frappe
from hcservice.website.website import validate_session_user

no_cache = True
def get_context(context):	
	validate_session_user()
