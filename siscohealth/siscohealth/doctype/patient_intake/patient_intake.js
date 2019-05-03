// Copyright (c) 2019, navdeepghai1@gmail.com and contributors
// For license information, please see license.txt

frappe.provide("hcservice.patient_intake");
hcservice.patient_intake.PatientIntake  = Class.extend({
	init: function(args){
		$.extend(this, args)
	},
	refresh: function(doc){
		var me = this;
		this.make_patient_encounter();
		var args = {
			"frm": me.frm
		};
		new siscohealth.patient_encounter.PatientEncounter(args);
	},
	check_medicare_id: function(doc){

	},
	make_patient_encounter: function(){
		var me = this;
		this.frm.add_custom_button(__("Patient Encounter"), function(){
			frappe.model.open_mapped_doc({
				frm: me.frm,
				method: "siscohealth.siscohealth.doctype.patient_intake.patient_intake.make_patient_encounter",	
			});			
	
		}, __("Make")).addClass("btn-secondary");
	
	},
});
$.extend(cur_frm.cscript, new hcservice.patient_intake.PatientIntake({frm: cur_frm}));

frappe.provide("siscohealth.patient_encounter");
siscohealth.patient_encounter.PatientEncounter = Class.extend({

	init: function(args){
		$.extend(this, args);
		this.make();
	},
	make: function(){
		this.make_create_button();
	},
	make_create_button: function(){
		var me = this;
		this.frm.add_custom_button("Create PE", function(){
			me.make_dialog();

		});	
	},
	make_dialog: function(){
		var fields = [];
		frappe.call({
			"method": "frappe.desk.form.load.getdoctype",
			"args": {
				"doctype": "Patient Encounter",
			},
			"callback": function(res){
				if(res && res.message){
					frappe.model.sync(res.message);
					docfields = frappe.meta.get_docfields("Patient Encounter");
					console.log(docfields);
					var dialog = new frappe.ui.Dialog({
						"title": __("Patient Encounter"),
						"fields":docfields
					});
					dialog.show();
				}
			}
		});
	}
})
