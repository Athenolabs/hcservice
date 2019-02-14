

import frappe

no_cache = True
def get_context(context):
	print(context)



@frappe.whitelist(allow_guest=True)
def register_user(args):
	return {}
