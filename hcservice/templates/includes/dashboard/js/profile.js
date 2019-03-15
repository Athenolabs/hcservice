/*
	Developer Navdeep
	Email navdeepghai1@gmail.com
*/
require(["jquery", "hcservice"], function($, hcservice){

	frappe.provide("profile");
	profile.ProfileController = hcservice.Form.extend({

		init: function(args){
			this._super(args);
		}
	});
	var args = {};
	$.extend(args, {
		"doctype": "User",
		"wrapper": "register_form",
		"fields":[
			"first_name", "last_name", "email",
			"gender",
		]
	});
	new profile.ProfileController(args)

});
