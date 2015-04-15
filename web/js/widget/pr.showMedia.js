(function($) {
	'use strict';
	$.widget("pr.showMedia", {
		options : {
			media : null,
			id : null,
			url_imdb : 'http://www.imdb.com/title/',
			url_tmdb : 'https://www.themoviedb.org/'
		},

		_create : function() {
			this.element.addClass('ui-widget pr-show-media');

			// image column
			this.panel_img = $('<div/>', {
				class : 'panel-img'
			}).appendTo(this.element);
			this.poster = $('<img/>', {
				src : ''
			}).appendTo(this.panel_img);

			// text column
			this.panel_text = $('<div/>', {
				class : 'panel-text'
			}).appendTo(this.element);
			// title - release_date
			this.title = $('<h3/>').appendTo(this.panel_text);
			this.release_date = $('<span/>').appendTo(this.panel_text);

			// rating
			this.vote_average = $('<span/>', {
				class : 'stars'
			}).appendTo(this.panel_text);

			// overview
			$('<strong/>', {
				text : 'Sinopsis:'
			}).appendTo(this.panel_text);
			this.overview = $('<p/>').appendTo(this.panel_text);

			// status
			var item_status = $('<p/>').appendTo(this.panel_text);
			$('<strong/>', {
				text : 'Estado:'
			}).appendTo(item_status);
			this.status = $('<span/>').appendTo(item_status);

			// number_of_episodes
			this.item_n_episodes = $('<p/>').appendTo(this.panel_text);
			$('<strong/>', {
				text : 'Episodios:'
			}).appendTo(this.item_n_episodes);
			this.n_episodes = $('<span/>').appendTo(this.item_n_episodes);

			// number_of_seasons
			this.item_n_seasons = $('<p/>').appendTo(this.panel_text);
			$('<strong/>', {
				text : 'Temporadas:'
			}).appendTo(this.item_n_seasons);
			this.n_seasons = $('<span/>').appendTo(this.item_n_seasons);

			// icons
			this.panel_links = $('<div/>', {
				class : 'panel-links'
			}).appendTo(this.element);

			this.link_imdb = $('<a />', {
				href : '',
				target : '_blank',
				class : 'pr-icon icon-imdb',
				title : 'IMDb'
			}).appendTo(this.panel_links);

			this.link_tmdb = $('<a />', {
				href : '',
				target : '_blank',
				class : 'pr-icon icon-tmdb',
				title : 'themoviedb'
			}).appendTo(this.panel_links);

			this._super();
		},

		_destroy : function() {
			this.element.removeClass('ui-widget pr-show-media');
			this.element.empty();

			this._super();
		},

		loadData : function(media, id) {
			var widget = this;
			this.options.media = media;
			this.options.id = id;
			$.ajax({
				type : 'GET',
				url : 'api/idx/' + media + '/' + id,
				success : function(data, status, jqXHR) {
					widget.title.text(data.title);
					widget.release_date.text(data.date);
					if (widget.options.media == 'movie') {
						widget.link_imdb.attr('href',
								widget.options.url_imdb + data.imdb_id);
						widget.item_n_episodes.hide();
						widget.item_n_seasons.hide();
					} else if (widget.options.media == 'tv') {
						widget.link_imdb.hide();
						widget.n_episodes.text(data.n_episodes);
						widget.n_seasons.text(data.n_seasons);
					}
					widget.link_tmdb.attr('href', widget.options.url_tmdb
							+ widget.options.media + '/' + data.id);
					widget.status.text(data.status);
					widget.overview.text(data.overview);
					widget.vote_average.text(data.vote_average);

					widget.poster.attr('src', data.url_poster);

					widget.vote_average.stars();
				}
			});
		},

		clear : function() {
			if (this.options.id != null) {
				this.title.text('');

				this.status.text('');
				this.release_date.text('');
				this.overview.text('');
				this.poster.attr('src', '');
				this.link_imdb.attr('href', '');
				this.link_tmdb.attr('href', '');
				this.vote_average.text('');

				this.n_episodes.text('');
				this.n_seasons.text('');

				this.item_n_episodes.show();
				this.item_n_seasons.show();
				this.link_imdb.show();
				
				this.options.media = null;
				this.options.id = null;
			}
		}
	});
})(jQuery);