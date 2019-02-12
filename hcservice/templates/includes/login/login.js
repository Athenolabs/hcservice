/*
	Developer Navdeep Ghai
	Email navdeepghai1@gmail.com
*/

requirejs(["jquery", "frappe"], function($){
	
	$("#signin_form").on("submit", function(event){
		event.preventDefault();
		var username = $("#login_email").val();
		var password = $("#password").val();
		if(!username || password){
			frappe.msgprint(__("Please enter username and password"));
			return false;
		}
		frappe.call({
			"method": "login",
			"args": {
				"usr": $("#login_email").val(),
				"pwd": $("#password").val()
			},
			"callback": function(res){
				
			}
		});
		return false;
	});
});
