(function($) {
	'use strict';
	$.widget("pr.movie", {
		options : {
			id : null
		},

		_create : function() {
			this.element.addClass('ui-widget pr-movie');
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
			this.element.removeClass('ui-widget pr-movie');
			this.element.empty();

			this._super();
		},

		_setOption : function(key, value) {
			this._super(key, value);
			if (key == 'id') {
				this.loadData(value);
			}
		},

		loadData : function(id) {
			var widget = this;
			$.ajax({
				type : 'GET',
				url : 'api/idx/movie/' + id,
				success : function(data, status, jqXHR) {
					widget.title.text(data.title);
					widget.imdb_link.text(data.imdb_link);
					widget.status.text(data.status);
					widget.release_date.text(data.release_date);
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
				this.element.hide();
			}
		}
	});
})(jQuery);