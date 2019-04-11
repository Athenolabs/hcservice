'''
	Developer Navdeep
	Email navdeepghai1@gmail.com
'''
import frappe
from frappe import _, msgprint, throw
from frappe.utils import cint, flt
from siscohealth.controllers.accounts_controller import AccountsController

class StockController(AccountsController):
	
	def validate(self):
		# call super class AccountsController validate
		super(StockController, self).validate()
		print("Stock Controller triggered: validate")

	def on_submit(self):
		# call super class AccountsController on_submit
		super(StockController, self).on_submit()
		print("Stock Controller triggered: on_submit")

	def on_cancel(self):
		# call super class AccountsController on_cancel
		super(StockController, self).on_cancel()
		print("Stock Controller triggered: on_cancel");

