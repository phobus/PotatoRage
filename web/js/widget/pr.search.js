(function($) {
	'use strict';
	$.widget("pr.search", {
		options : {
			type : null,
			selectedMedia : function() {
			}
		},

		_create : function() {
			this.element.addClass('ui-widget pr-search');

			this.searchBox = $('<div/>').appendTo(this.element);
			this.input = $('<input type="text"/>').appendTo(this.searchBox);
			this.button = $("<button>", {
				text : "Buscar"
			}).appendTo(this.searchBox);

			this.table = $('<table/>').appendTo(this.element);
			this.colgroup = $('<colgroup/>').appendTo(this.table);
			this.thead = $('<thead/>').appendTo(this.table);
			this.tbody = $('<tbody class="ui-widget-content"/>').appendTo(
					this.table);

			$('<col class="title"/>').appendTo(this.colgroup);

			this.thead.append(this._createHeaderRow());

			this.element.hide();
			this.table.hide();
			
			this._on(this.button, {
				click : function(event) {
					this.search(this.input.val());
				}
			});

			this._on(this.tbody, {
				'mouseover tr' : function(event) {
					$(event.currentTarget).addClass('ui-state-highlight');
				},
				'mouseout tr' : function(event) {
					$(event.currentTarget).removeClass('ui-state-highlight');
				},
				'click tr' : function(event) {
					var currentTarget = $(event.currentTarget);
					this._trigger("selectedMedia", event, {
						type : this.options.type,
						id : currentTarget.data('id')
					});
				}
			});

			this._super();
		},

		_destroy : function() {
			this.element.removeClass('ui-widget pr-search');
			this.element.empty();

			this._super();
		},

		clear : function() {
			if (this.options.type != null) {
				this.input.val('');
				this.tbody.empty();
				this.table.hide();
				this.element.hide();
				this.options.type = null;
			}
		},

		_createHeaderRow : function() {
			var html = '<tr class="ui-widget-header">';
			html += '<th>Nombre</th>';
			html += '<th>Fecha</th>';
			html += '<th>Puntuacion</th>';
			html += '</tr>';
			return html;
		},

		_createRow : function(data) {
			var title = '';
			if (data.title) {
				title = data.title;
			} else if (data.name) {
				title = data.name;
			}

			var date = '';
			if (data.release_date) {
				date = data.release_date.substr(0, 4);
			} else if (data.first_air_date) {
				date = data.first_air_date.substr(0, 4);
			}

			var html = '<tr>';
			html += '<td>' + title + '</td>';
			html += '<td>' + date + '</td>';
			html += '<td><span class="stars">' + data.vote_average
					+ '</span></td>';
			html += '</tr>';

			var $html = $(html);
			$html.data('id', data.id);

			return $html;
		},

		search : function(query) {
			var widget = this;
			$.ajax({
				type : 'GET',
				url : 'api/idx/' + this.options.type,
				data : {
					q : query
				},
				success : function(data, status, jqXHR) {
					widget.tbody.empty();
					var row;
					for (var i = 0; i < data.results.length; i++) {
						row = widget._createRow(data.results[i]);
						widget.tbody.append(row);
					}
					widget.tbody.find('span.stars').stars();
					widget.table.show();
				}
			});
		}
	});
})(jQuery);