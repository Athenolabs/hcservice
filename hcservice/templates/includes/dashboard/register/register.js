/*
	Developer Navdeep
	Email navdeepghai1@gmail.com
*/

require(["jquery", "frappe", "hcservice"], function($, fr,  hcservice){
	console.log("Register Page");
	$("#register").on("submit", function(){
		hcservice.hide("email-validation");
		var email = $("#register_email").val();
		if(!email){
			hcservice.show_alert("email-validation", "Please enter corrent email", "");
			return false;	
		}
		var args = {};
		$.extend(args, {"email": email});
		frappe.call({
			"method": "hcservice.www.register.register_user",
			"args": {
				"args": args
			},
			"callback": function(res){
				console.log(res);
				hcservice.show_alert("email-validation", "User already exists.", "");	
			},
			"error": function(res){
				console.log(res);
			}
		});	
		return false;
	});
});
