'''
	Developer Navdeep
	Email navdeepghai1@gmail.com
'''
import frappe
from frappe import _, msgprint, throw
from frappe.utils import cint, flt
from siscohealth.controllers.stock_controller import StockController
from siscohealth.document_controllers.patient_encounter import PatientEncounter

class HealthcareController(StockController, PatientEncounter):
	
	def validate(self):
		# call super class StockController validate
		super(HealthcareController, self).validate()
		print("Healthcare Controller triggered: validate")
		if self.doctype == "Patient Encounter":
			self.validate_patient_encounter()

	def on_submit(self):
		# call super class StockController on_submit
		super(HealthcareController, self).on_submit()
		print("Healthcare Controller triggered: on_submit")

	def on_cancel(self):
		# call super class StockController on_cancel
		super(HealthcareController, self).on_cancel()
		print("Healthcare Controller triggered: on_cancel");

