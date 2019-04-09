# -*- coding: utf-8 -*-
# Copyright (c) 2019, navdeepghai1@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class PatientIntake(Document):
	
	def validate(self):
		self.validate_scheduling()
		self.validate_patient_contact()
		self.validate_patient_background_info()
		self.validate_comments()
		self.validate_exam_declined()
		self.make_or_update_patient()
		self.make_or_update_insurances()

	def validate_scheduling(self):
		pass

	def validate_patient_contact(self):
		pass
	
	def validate_patient_background_info(self):
		pass

	def validate_comments(self):
		pass
	
	def validate_exam_declined(self):
		pass



	def make_or_update_patient(self):
		patient = None
		if(self.patient and frappe.db.exists("Patient", self.patient)):
			patient = frappe.get_doc("Patient", self.patient)
		else:
			patient = frappe.new_doc("Patient")	
		patient.update({
			"patient_name": "%s %s"%(self.patient_first_name, self.patient_last_name),
			"mobile": self.pc_cell_phone, "dob": self.date_of_birth,
			"sex": self.gender, "email": self.pc_email,
			"phone": self.patient_home_phone, "marital_status": self.marital_status
		})
		patient.save(ignore_permissions=True)
		self.patient = patient.name
	

	# Medicare Insurance
	def make_or_update_medicare_insurance(self):
		if(self.m_insurance_no):
			insurance = frappe._dict({
				"insurance_no": self.m_insurance_no,
				"insurance_provider": "Medicare Insurance",
				"insurance": self.m_insurance,
				"insurance_name": self.m_insurance or self.m_other_insurance_name,
				"insurance_type": self.m_insurance_type,
				"plan_no": self.m_plan_no, "patient_intake": self.name,
				"phone_no":self.m_phone_no, "patient_id": self.patient,
				"is_primary": self.m_is_primary
			})
			insurance = self.get_insurance_doc(self.medicare_insurance_link,
								insurance)
			insurance.save(ignore_permissions=True)
			self.medicare_insurance_link = insurance.name
				
	# PART D Insurance
	def make_or_update_part_d_insurance(self):
		if(self.pd_insurance):
			insurance = frappe._dict({
				"insurance_provider": "PART D Insurance",
				"insurnace": self.pd_insurance,
				"insurance_name": self.pd_insurance or self.pd_other_insurance_name,
				"plan_no": self.pd_plan_no, "insurance_type": "Other",
				"phone_no":self.pd_phone_no,"group_no": self.pd_group_no,
				"bin_no": self.pd_bin_no, "pcn_no": self.pd_pcn_no,
				"patient_id": self.patient, "patient_intake": self.name
			})
			insurance = self.get_insurance_doc(self.part_d_insurance_link,
								insurance)
			insurance.save(ignore_permissions=True)
			self.part_d_insurance_link = insurance.name
	
	# Medicaid Insurance
	def make_or_update_medicaid_insurance(self):
		if(self.md_insurance_no):
			insurance = frappe._dict({
				"insurance_name": "Medicaid Insurance", "plan_name": self.md_plan_name,
				"insurance_provider": "Medicaid Insurance",
				"insurance_no": self.md_insurance_no,
				"insurance_type": self.md_insurance_type,
				"bin_no": self.md_is_primary, "patient_id": self.patient,
				"patient_intake": self.name
			})
			insurance = self.get_insurance_doc(self.medicaid_insurance_link,
								insurance)
			insurance.save(ignore_permissions=True)
			self.medicaid_insurance_link = insurance.name	

	# Private Insurance/ Can be any Insurance Provide	
	def make_or_update_private_insurance(self):
		if(self.pr_insurance):
			insurance = frappe._dict({
				"insurance": self.pr_insurance,
				"insurance_provider": "Private Insurance",
				"is_primary": self.pr_is_primary,
				"include_rx_converage": self.pr_is_include_rx_coverage,
				"insurance_type": self.pr_insurance_type,
				"bin_no": self.md_is_primary,
				"phone_no": self.pr_phone_no,
				"group_no": self.pr_group_no,
				"bin_no": self.pr_group_no, "patient_intake": self.name,
				"pcn_no": self.pr_pcn_no, "patien_id": self.patient,
			})
			
			insurance = self.get_insurance_doc(self.private_insurance_link,
								insurance)
			insurance.save(ignore_permissions=True)
			self.private_insurance_link = insurance.name	

	def make_or_update_insurances(self):
		insurances = []
		self.make_or_update_medicare_insurance()
		self.make_or_update_part_d_insurance()
		self.make_or_update_medicaid_insurance()
		self.make_or_update_private_insurance()
		
	def get_insurance_doc(self, insurance, _dict):
		
		insurance_doc = None
		if(insurance and frappe.db.exists("Insurance", insurance)):
			insurance_doc = frappe.get_doc("Insurance", insurance)
		else:
			insurance_doc = frappe.new_doc("Insurance")
		_dict.update({"patient_id": self.patient,"patient_intake": self.name})
		insurance_doc.update(_dict)
		return insurance_doc


@frappe.whitelist()
def make_patient_encounter(source_name, target_doc=None):
	
	def post_update(source_doc, target_doc):
		target_doc.patient_sex = source_doc.gender

	doc = get_mapped_doc("Patient Intake", source_name, {
			"Patient Intake": {
				"doctype": "Patient Encounter",
				"gender": "patient_sex",
			},
		},
		target_doc, post_update)
	return doc
