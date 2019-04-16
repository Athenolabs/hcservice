'''
	Developer Navdeep
	Email navdeepghai1@gmail.com
'''

class PatientEncounter(object):
	
	def validate_patient_encounter(self):
		print("Patient controller")
		print(self.doc.as_dict())

	def update_diagnosis(self):
		self.patient_intake = frappe.get_doc("Patient Intake", self.doc.patient_intake)
		self.update_osteoarthritis()
		self.update_neuropathy()
		self.update_arthritis()
		self.update_alergies()	
