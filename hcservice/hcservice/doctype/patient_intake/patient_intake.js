// Copyright (c) 2019, navdeepghai1@gmail.com and contributors
// For license information, please see license.txt

frappe.provide("hcservice.patient_intake");
hcservice.patient_intake.PatientIntake  = Class.extend({
	init: function(args){
		$.extend(this, args)
	},
	refresh: function(doc){
		this.make_patient_encounter();
	},
	check_medicare_id: function(doc){

	},
	make_patient_encounter: function(){
		var me = this;
		this.frm.add_custom_button(__("Patient Encounter"), function(){
			frappe.model.open_mapped_doc({
				frm: me.frm,
				method: "hcservice.hcservice.doctype.patient_intake.patient_intake.make_patient_encounter",	
			});			
	
		}, __("Make")).addClass("btn-secondary");
	
	}
});

$.extend(cur_frm.cscript, new hcservice.patient_intake.PatientIntake({frm: cur_frm}));
