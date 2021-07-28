'use strict';
'require view';

return view.extend({
	render: function() {
		return E('h1', 'Page2: Hello world');
	},

	handleSaveApply:null,
	handleSave:null,
	handleReset:null
});
