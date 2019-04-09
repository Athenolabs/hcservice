require.config({
	paths: {
		'prismjs': 'assets/hcservice/js/libs/plugins/prismjs/js/prism.pack',
	},
	shim: {
		prism: {
			exports: "Prism"
		}
	}
});

require(['prismjs', 'jquery'], function(prismjs, $){
    $(document).ready(function(){
		console.log(this);
        // $('[class^="language-"]').each(function(i, block) {
	     //    Prism.highlightElement(block);
        // });
    });
});
