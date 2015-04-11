$.ajaxSetup({
	cache : true,
	async : true,
	contentType : 'application/json; charset=utf-8',
	dataType : 'json',
	error : function(event, request, statusText) {
		alert(request + ': ' + statusText);
	}
});