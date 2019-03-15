requirejs.config({
	'shim':{
		"flatpicker": []
	},
	'paths': {
		'flatpicker': '/assets/hcservice/js/libs/flatpickr/js/flatpickr.min'
	}
});

require(["flatpicker"]);
