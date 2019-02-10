/*
	Developer Navdeep Ghai
	Email navdeepghai1@gmail.com
*/

requirejs(["jquery", "frappe"], function($){
	
	$("#sign_in").on("click", function(event){
		event.preventDefault();
		console.log($("#login_email").val());
		console.log($("#password").val());
		
		frappe.call({
			"method": "login",
			"args": {
				"usr": $("#login_email").val(),
				"pwd": $("#password").val()
			},
			"callback": function(res){
				console.log(res);
			}
		});
		return false;
	});
});
