$(document).ready(function() {
	$('#search').search();
	$('#navigation a').click(function() {
		$('#search').search('option', 'type', this.id);
		return false;
	});
});