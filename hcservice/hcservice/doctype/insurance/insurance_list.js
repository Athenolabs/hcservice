
frappe.listview_settings["Insurance"] = {
	"add_field": ["patient_id", "name"],
	"custom_filter_configs": [
			{
			"fieldname": "patient_id",
			"label": "Patient ID",
			"fieldtype": "Link",
			"options": "Patient",
		}
	],
	"onload": function(listview){
		console.log(listview);
	},	
	"filters": [
			{
			"fieldname": "patient_id",
			"label": "Patient ID",
			"fieldtype": "Link",
			"options": "Patient",
		}
	],
}
