/*
	Developer Navdeep Ghai
	Email navdeepghai1@gmail.com
*/

requirejs(["jquery", "frappe", "hcservice"], function($, fr, hcservice){
	
	$("#sign_in").on("click", function(event){
		event.preventDefault();
		hcservice.hide("login-validation");
		var username = $("#login_email").val();
		var password = $("#password").val();
		
		if(!username || !password){
			hcservice.show_alert("login-validation", "Mandatory email and password");
			return false;
		}
		
		frappe.call({
			"method": "login",
			"args": {
				"usr": $("#login_email").val(),
				"pwd": $("#password").val()
			},
			"callback": function(res){
				if(res && res.message =="Logged In"){
					window.location.href = "/dashboard?username="+res.full_name;
				}
				else{
					
					return false;
				}	
			}
		});
		return false;
	});
});
