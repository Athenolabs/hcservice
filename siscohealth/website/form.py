'''
	Developer Navdeep
	Email navdeepghai1@gmail.com
'''

import frappe

@frappe.whitelist()
def get_form_fields(doctype=None, fields=[]):
	data = []
	if doctype and frappe.db.exists("DocType", doctype):
		doc = frappe.get_doc("DocType", doctype)
		if fields:
			for field in doc.fields:
				if field.fieldname in fields:
					data.append(field)						
	return data
