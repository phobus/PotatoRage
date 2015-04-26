(function($) {
	'use strict';
	$.widget("pr.showMedia", {
		options : {
			media : null,
			id : null
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
			this.rating = $('<span/>', {
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
				url : 'v1/idx/' + media + '/' + id,
				success : function(data, status, jqXHR) {
					widget.title.text(data.title);
					widget.release_date.text(data.date);
					if (widget.options.media == 'movie') {
						widget.item_n_episodes.hide();
						widget.item_n_seasons.hide();
					} else if (widget.options.media == 'tv') {
						widget.n_episodes.text(data.n_episodes);
						widget.n_seasons.text(data.n_seasons);
					}
					widget.status.text(data.status);
					widget.overview.text(data.overview);
					widget.rating.text(data.rating);

					widget.poster.attr('src', data.poster);
					widget.panel_links.append(widget._createLinks(
							widget.options.media, data.id, data.imdb_id));

					widget.rating.stars();
				}
			});
		},

		_createLinks : function(media, id, imdb_id) {
			var buffer = [];
			var link = $.linker.TheMovieDb(media, id);
			if (link) {
				buffer.push(link);
			}

			link = $.linker.IMDb(imdb_id);
			if (link) {
				buffer.push(link);
			}
			return buffer;
		},

		clear : function() {
			if (this.options.id != null) {
				this.title.text('');

				this.status.text('');
				this.release_date.text('');
				this.overview.text('');
				this.poster.attr('src', '');
				this.rating.text('');

				this.n_episodes.text('');
				this.n_seasons.text('');

				this.item_n_episodes.show();
				this.item_n_seasons.show();

				this.panel_links.empty();

				this.options.media = null;
				this.options.id = null;
			}
		}
	});
})(jQuery);