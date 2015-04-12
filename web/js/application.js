$(document).ready(function() {
	'use strict';
	$('#search').search();
	$('#show-movie').showMedia();

	$('#navigation a').click(function() {
		$('#section').text(this.text);
		$('#search').search('clear');
		$('#show-movie').showMedia('clear');

		if (this.id == 'home') {

		} else if (this.id == 'movie') {
			$('#search').search('option', 'media', this.id).show();
		} else if (this.id == 'tv') {
			$('#search').search('option', 'media', this.id).show();
		} else if (this.id == 'config') {

		}

		return false;
	});

	$('#search').search({
		selectedMedia : function(event, data) {
			$('#show-movie').showMedia('loadData', data.media, data.id);
			$('#search').hide();
		}
	});
	loadConfig();
	$('#home').click();

	function loadConfig() {
		$.ajax({
			type : 'GET',
			url : 'api/config',
			success : function(data, status, jqXHR) {
				$('#show-movie').showMedia('option', 'url_img', data.url_img);
			}
		});
	}
});