'''
	Developer Navdeep
	Email navdeepghai1@gmail.com
'''
import frappe
from frappe import _, msgprint, throw
from frappe.utils import cint, flt
from siscohealth.controllers.stock_controller import StockController

class SellingController(StockController):
	
	def validate(self):
		# call super class StockController validate
		super(SellingController, self).validate()
		print("Selling Controller triggered: validate")

	def on_submit(self):
		# call super class StockController on_submit
		super(SellingController, self).on_submit()
		print("Selling Controller triggered: on_submit")

	def on_cancel(self):
		# call super class StockController on_cancel
		super(SellingController, self).on_cancel()
		print("Selling Controller triggered: on_cancel");

