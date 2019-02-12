/*
	Developer Navdeep
	Email navdeepghai1@gmail.com
*/

require(["jquery", "hcservice"], function($){

	var Dashboard = Class.extend({
		init: function(args){
			$.extend(this, args);
			this.make();
		},
		refresh: function(){
		},
		make: function(){
			console.log(frappe.user_id);
		},
	});
	new dashboard.Dashboard({});

});
