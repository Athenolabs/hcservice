'''
	Developer Navdeep
	Email navdeepghai1@gmail.com
'''
import frappe
from frappe import _, msgprint, throw, scrub
from frappe.utils import cint, flt
import sys
import os
import importlib

'''
	Make all standard module dynamical module
'''

def get_module_path(doctype):
	controller = scrub(doctype)
	
	controller_path = "%s.%s.%s"%("siscohealth", 
			"document_controllers", controller)
	controller = None
	try:
		controller = importlib.import_module(controller_path)
	except ImportError as e:
		frappe.msgprint("""Import Error while triggering 
			<b>%s</b> controller """%(doctype))
	return controller


'''
	Handler every doc events and execute relevent 
	controller from Document Controller
'''			
def handle_doc_event(doc, method):
	
	'''
		This function will be trigger on each docevents
		define in hooks.py under doc_events section
	'''
	doctype = doc.meta.name
	func = None
	if doctype == "Patient Encounter":
		controller = get_module_path(doctype)
		func = getattr(controller.PatientEncounter(doc, doctype, method), method, None)
	
	# Every controller should have one of following function
	# 1. Validate, 2. Submit, 3. On Cancel
	# for more info visit: https://frappe.io/docs/user/en/guides/basics/hooks
	if func:
		func()


'''
	Base Controller for all the controller
'''
class BaseController(object):

	def __init__(self, doc, doctype, method):
		self.doc = doc
		self.doctype = doctype
		self.method = method
		self.update_global_defaults_and_settings()

	def update_global_defaults_and_settings(self):
		self.setting = frappe.get_doc("Siscohealth Settings", "Siscohealth Settings")
			
	def validate(self):
		# validate function to validate while saving
		# the doctypes
		print("Base Controller Triggered: Validate")

	def on_submit(self):
		# on_submit function to validate the form
		# while submission of form
		print("Base Controller Triggered: On Submit")

	def on_cancel(self):
		# on_cancel function to validate the form
		# cancellation of form
		print("Base Controller Triggered: On Cancel")	
