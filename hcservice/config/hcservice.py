
import frappe
from frappe import _

def get_data():

	return [
			{
			"label": _("Patient Intake"),
			"items": [
					{
					"label": _("Patient Intake"),
					"type": "doctype",
					"name": "Patient Intake",
					"description": _("Patient Intake form"),
				},
			]
		}
	]
