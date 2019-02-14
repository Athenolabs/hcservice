/*
	Developer Navdeep
	Email navdeepghai1@gmail.com
*/

require(["jquery", "frappe", "hcservice"], function($, fr, hcservice){

	$("#password_reset").on("submit", function(event){
		event.preventDefault();
	
		var email = $("#reset_email").val();
		if(!email){
			hcservice.show_alert("reset-validation", "Please enter valid email");
			return false;
		}
		console.log(email);
		frappe.call({

			"method": "hcservice.www.password_reset.reset_password",
			"args": {
				"email": email
			},
			"callback": function(res){
				hcservice.show_alert("reset-validation", res.message); 
			}
		});	
	});
});
