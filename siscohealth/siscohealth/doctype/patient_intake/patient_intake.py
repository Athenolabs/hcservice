# -*- coding: utf-8 -*-
# Copyright (c) 2019, navdeepghai1@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from siscohealth.utils import get_age
from frappe.utils import cint, cstr, nowdate, nowtime

class PatientIntake(Document):
	
	def validate(self):
		self.validate_scheduling()
		self.validate_patient_contact()
		self.validate_patient_background_info()
		self.validate_comments()
		self.validate_exam_declined()
		self.make_or_update_patient()
		self.make_or_update_vital_signs()
		self.make_or_update_patient_encounter()
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


	'''
		Create Patient as standard workflow in ERP
		and link with patient intake form
	'''
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


	'''
		Make Vital Signs for Patient as a separate link
		Apply standard conversion factor
	'''
	def make_or_update_vital_signs(self):
		uom = 39.3700787
		vital_signs = None
		if(self.vital_signs and frappe.db.exists("Vital Signs", self.vital_signs)):
			vital_signs = frappe.get_doc("Vital Signs", self.vital_signs)
		else:
			vital_signs = frappe.new_doc("Vital Signs")	
			vital_signs.signs_date = nowdate()
			vital_signs.signs_time = nowtime()
		vital_signs.update({
			"patient": self.patient,
			"height": self.height/uom if self.height else 0.0,
			"weight": self.weight/2.205 if self.weight else 0.0
		})
		vital_signs.save(ignore_permissions=True)
		self.vital_signs = vital_signs.name

	'''
		Make Patient Encounter to automize the process
	'''
	def make_or_update_patient_encounter(self):
		patient_encounter = None
		if(self.patient_encounter and( 
			frappe.db.get_value("Patient Encounter", {
					"name": self.patient_encounter,
					"docstatus": 0}))):
			patient_encounter = frappe.get_doc("Patient Encounter", self.patient_encounter)
		else:
			patient_encounter = frappe.new_doc("Patient Encounter")	
			patient_encounter.encounter_date = nowdate()
			patient_encounter.encounter_time = nowtime()
			patient_encounter.practitioner = ""
			patient_encounter.update({
				"patient": self.patient,
				"patient_sex": self.gender,
				"patient_intake": self.name,
				"patient_age": get_age(self.date_of_birth),
			})
			patient_encounter.insert(ignore_permissions=True, ignore_mandatory=True)
			
		patient_encounter.update({
			"patient": self.patient,
			"patient_sex": self.gender,
			"patient_intake": self.name,
			"patient_age": get_age(self.date_of_birth),
		})
		patient_encounter.flags.ingore_mandatory = True
		patient_encounter.save(ignore_permissions=True)
		self.patient_encounter = patient_encounter.name


@frappe.whitelist()
def make_patient_encounter(source_name, target_doc=None):
	
	def post_update(source_doc, target_doc):
		diagnosis = []
		target_doc.patient_sex = source_doc.gender
		target_doc.patient_age = get_age(source_doc.date_of_birth)

	doc = get_mapped_doc("Patient Intake", source_name, {
			"Patient Intake": {
				"doctype": "Patient Encounter",
				"gender": "patient_sex",
				"field_map":{
					"name": "patient_intake"
				}
			},
		},
		target_doc, post_update)
	return doc

