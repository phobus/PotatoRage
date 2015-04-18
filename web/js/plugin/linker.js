(function($) {
	'use strict';

	var idx = {
		imdb : {
			alt : 'IMDb',
			url : 'http://www.imdb.com/title/',
			src : '/st/img/imdb_small.png'
		},
		tmdb : {
			alt : 'TheMovieDb',
			url : 'https://www.themoviedb.org/',
			src : '/st/img/themoviedb.png'
		}
	};

	function createImageLink(href, src, alt) {
		var link = $('<a/>', {
			target : '_blank',
			href : href,
			class: 'pr-icon',
			title: alt
		});
		$('<img/>', {
			src : src,
			alt : alt
		}).appendTo(link);
		return link;
	}

	$.linker = {
		IMDb : function(id) {
			if (id) {
				return createImageLink(idx.imdb.url + id, idx.imdb.src,
						idx.imdb.alt);
			} else {
				return undefined;
			}
		},
		TheMovieDb : function(media, id) {
			if (media && id) {
				return createImageLink(idx.tmdb.url + media + '/' + id,
						idx.tmdb.src, idx.tmdb.alt);
			} else {
				return undefined;
			}
		}
	}

}(jQuery));