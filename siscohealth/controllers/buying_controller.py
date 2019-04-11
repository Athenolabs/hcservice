'''
	Developer Navdeep
	Email navdeepghai1@gmail.com
'''
import frappe
from frappe import _, msgprint, throw
from frappe.utils import cint, flt
from siscohealth.controllers.stock_controller import StockController

class BuyingController(StockController):
	
	def validate(self):
		# call super class StockController validate
		super(BuyingController, self).validate()
		print("Buying Controller triggered: validate")

	def on_submit(self):
		# call super class StockController on_submit
		super(BuyingController, self).on_submit()
		print("Buying Controller triggered: on_submit")

	def on_cancel(self):
		# call super class StockController on_cancel
		super(BuyingController, self).on_cancel()
		print("Buying Controller triggered: on_cancel");

