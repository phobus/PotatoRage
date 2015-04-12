(function($) {
	'use strict';
	$.widget("pr.showMedia", {
		options : {
			type : null,
			id : null
		},

		_create : function() {
			this.element.addClass('ui-widget pr-show-media');
			this.element.hide();

			this.title = $('<h3/>').appendTo(this.element);
			this.imdb_link = $('<a href="">imdb</a>').appendTo(this.element);
			this.status = $('<span/>').appendTo(this.element);
			this.release_date = $('<span/>').appendTo(this.element);
			this.overview = $('<span/>').appendTo(this.element);
			this.poster_path = $('<span/>').appendTo(this.element);
			this.vote_average = $('<span class="stars"/>').appendTo(
					this.element);
			this._super();
		},

		_destroy : function() {
			this.element.removeClass('ui-widget pr-show-media');
			this.element.empty();

			this._super();
		},

		loadData : function(type, id) {
			var widget = this;
			this.options.type = type;
			this.options.id = id;
			$.ajax({
				type : 'GET',
				url : 'api/idx/' + type + '/' + id,
				success : function(data, status, jqXHR) {
					if (widget.options.type == 'movie') {
						widget.title.text(data.title);
						widget.imdb_link.text(data.imdb_link);
						widget.release_date.text(data.release_date);
					} else if (widget.options.type == 'serie') {
						widget.title.text(data.name);
						widget.imdb_link.text('');
						widget.release_date.text(data.first_air_date);
					}
					widget.status.text(data.status);
					widget.overview.text(data.overview);
					widget.poster_path.text(data.poster_path);
					widget.vote_average.text(data.vote_average);
					widget.element.show();
				}
			});
		},

		clear : function() {
			if (this.options.id != null) {
				this.title.text('');
				this.imdb_link.text('');
				this.status.text('');
				this.release_date.text('');
				this.overview.text('');
				this.poster_path.text('');
				this.vote_average.text('');

				this.options.type = null;
				this.options.id = null;

				this.element.hide();
			}
		}
	});
})(jQuery);