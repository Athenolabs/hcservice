'''
	Developer Navdeep
	Email navdeepghai1@gmail.com
'''
import frappe
from frappe import _, msgprint
from frappe.utils import (cint, flt, cstr, getdate, nowdate,
		add_to_date)
from frappe.model.mapper import get_mapped_doc
from siscohealth.controllers.healthcare_controller import HealthcareController

class PatientEncounter(HealthcareController):
	
	def validate(self):
		if self.doc.is_new():
			return
		super(PatientEncounter, self).validate()
		print("Patient Encounter on validate")
		self.update_diagnosis()
 
	def on_cancel(self):
		super(PatientEncounter, self).on_cancel()
		print("Patient Encounter on cancel")


	def on_submit(self):
		super(PatientEncounter, self).on_submit()
		print("Patient Encounter on submit")

	def update_diagnosis(self):
		self.patient_intake = frappe.get_doc("Patient Intake", self.doc.patient_intake)	
		self.update_osteoarthritis_diagnosis_code()
		self.update_neuropathy_diagnosis_code()
		self.update_arthritis_diagnosis_code()
		self.update_alergies_diagnosis_code()


	def update_osteoarthritis_diagnosis_code(self):
		if(self.patient_intake.neuropathy):
			codes = []

	def update_neuropathy_diagnosis_code(self):
		if(self.patient_intake.arthritis):
			pass

	def update_arthritis_diagnosis_code(self):
		if(self.patient_intake.osteoarthritis):
			pass

	def update_alergies_diagnosis_code(self):
		if(self.patient_intake.allergies):
			pass
	
@frappe.whitelist()
def make_invoice(source_name, target_name=None):
	
	def update_post_process(source_doc, target_doc):
		print(source_doc)
		print(target_doc)
		pass

	mapped_doc = get_mapped_doc("Patient Encounter", source_name,{
			"Patient Encounter": {
				"doctype": "Sales Invoice",
			},
			"Sales Invoice Item": {
				"doctype": "Drug Prescription"
			}
		}, target_name, update_post_process)
	
	
