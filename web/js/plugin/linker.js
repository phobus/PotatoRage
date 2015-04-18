(function($) {
	'use strict';

	var url_imdb = 'http://www.imdb.com/title/';
	var url_tmdb = 'https://www.themoviedb.org/';
	var url_theTvDb;

	$.linker = {
		IMDb : function(id) {
			if (id !== undefined) {
				return url_imdb + id;
			} else {
				return undefined;
			}
		},
		TheMovieDb : function(media, id) {
			if (media !== undefined && id !== undefined) {
				return url_tmdb + media + '/' + id;
			} else {
				return undefined;
			}
		}
	}

}(jQuery));