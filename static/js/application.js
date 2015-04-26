$(document).ready(function() {
	'use strict';
	$('#search').search().hide();
	$('#show-media').showMedia().hide();
	$('#search-actions').searchActions().hide();

	$('#navigation a').click(function() {
		$('#section').text(this.text);
		$('#search').search('clear').hide();
		$('#show-media').showMedia('clear').hide();
		$('#search-actions').hide();
		
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
			$('#show-media').showMedia('loadData', data.indexer, data.media, data.id).show();;
			$('#search-actions').searchActions({
				indexer: data.indexer,
				media : data.media,
				id : data.id
			}).show();
			$('#search').hide();
		}
	});
	
	$('#search-actions').searchActions({
		back : function(event) {
			$('#show-media').showMedia('clear').hide();
			$('#search').show();
			$('#search-actions').hide();
		}
	});
	
	$('#home').click();
});