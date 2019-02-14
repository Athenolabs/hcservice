

import frappe

def validate_session_user():
	if frappe.session.user == "Guest":
		frappe.local.flags.redirect_location = "/login"
		raise frappe.Redirect	
