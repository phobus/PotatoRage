$(document).ready(function() {
	'use strict';
	$('#search').search();
	$('#show-movie').movie();

	$('#navigation a').click(function() {
		$('#section').text(this.text);
		$('#search').search('clear');
		$('#show-movie').movie('clear');

		if (this.id == 'home') {

		} else if (this.id == 'movie') {
			$('#search').search('option', 'type', this.id).show();
		} else if (this.id == 'serie') {
			$('#search').search('option', 'type', this.id).show();
		} else if (this.id == 'config') {
			
		}

		return false;
	});

	$('#search').search({
		selectedMedia : function(event, data) {
			$('#show-movie').movie('option', 'id', data.id);
			$('#search').hide();
		}
	});

	$('#home').click();
});