'''
	Developer Navdeep
	Email navdeepghai1@gmail.com
'''

import frappe
from frappe import _, msgprint
from frappe.utils import cint, flt
from siscohealth.controllers.base_controller import BaseController

class AccountsController(BaseController):
	
	def validate(self):
		# call super class BaseController validate
		super(AccountsController, self).validate()
		print("Account Controller triggered: validate")

	def on_submit(self):
		# call super class BaseController on_submit
		super(AccountsController, self).on_submit()
		print("Account Controller triggered: on_submit")

	def on_cancel(self):
		# call super class BaseController on_cancel
		super(AccountsController, self).on_cancel()
		print("Account Controller triggered: on_cancel");

