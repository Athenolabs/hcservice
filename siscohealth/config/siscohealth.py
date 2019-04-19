
import frappe
from frappe import _

def get_data():

	return [
			{
				"label": _("Patient Intake"),
				"items": [{
						"label": _("Patient Intake"),
						"type": "doctype",
						"name": "Patient Intake",
						"description": _("Patient Intake form"),
					},{
						"label": _("Patient Encounter"),
						"type": "doctype",
						"name": "Patient Encounter",
						"description": _("Patient Encounter Form")
					},	
				],
			},{
			"label": _("My Reports"),
			"items":[{
					"label": _("Marketing Sales Room Completed Orders Report"),
					"type": "report",
					"is_query_report": True,
					"name": "Sales Room Patient",
					"description": _("Marketing Sales Room Completed Orders Report"),
				},{
					"label": _("Marketing Sales Room Completed DME Orders Product Report"),
					"type": "report",
					"is_query_report": True,
					"name": "Sales Room Patient Order",
					"description": _("Marketing Sales Room Completed DME Orders Product Report")
				},{
					"label": _("Marketing Sales Room Completed Pharamcy Orders"),
					"type": "report",
					"is_query_report": True,
					"name": "Sales Room Rx Patient Order",
					"description": _("Marketing Sales Room Completed Pharamcy Orders"),
				},{
					"label":_("Marketer Payment"),
					"type": "report",
					"is_query_report": True,
					"name": "Marketer Payment",
					"description": _("Marketer Payment Report"),
				},{
					"label": _("Lead Provider Lead Stat Report"),
					"type": "report",
					"is_query_report": True,
					"name": "Lead Provider Lead Stat",
					"description": _("Lead Provider Lead Stat Report"),
				},{
					"label": "Lead Status Report",
					"type": "report",
					"is_query_report": True,
					"name": "Lead Status",
					"description": _("Lead Status Report"),
				}
			]

		}
	]
