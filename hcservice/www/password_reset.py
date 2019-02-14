
import frappe

def get_context(context):
	print("Context Page")


@frappe.whitelist(allow_guest=True)
def reset_password(email=None):
	msg = "Please check your email  for update passsword instruction"
	if not(email):
		msg = "Please enter email"
	return msg
