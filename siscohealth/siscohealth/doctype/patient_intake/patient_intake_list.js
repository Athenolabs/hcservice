frappe.listview_settings["Patient Intake"] = {
	"fields": ["patient_first_name"],
	"onload": function(listview){
		console.log(listview);
	},
	"filters": [
			{
			"fieldname": "patient_first_name",
			"fieldtype": "Data",
		}

	]
}
