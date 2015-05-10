(function($) {
	'use strict';
	$.widget("pr.search", {
		options : {
			media : null,
			indexer: null,
			selectedMedia : function() {
			}
		},

		_create : function() {
			this.element.addClass('ui-widget pr-search');

			this.panel_search = $('<div/>', {
				class : 'panel-search'
			}).appendTo(this.element);
			this.input = $('<input/>', {
				type : 'text'
			}).appendTo(this.panel_search);
			this.button = $("<button>", {
				text : 'Buscar',
				class: 'btn'
			}).appendTo(this.panel_search);

			this.table = $('<table/>').appendTo(this.element);
			this.colgroup = $('<colgroup/>').appendTo(this.table);
			this.thead = $('<thead/>').appendTo(this.table);
			this.tbody = $('<tbody/>', {
				class : 'ui-widget-content'
			}).appendTo(this.table);

			$('<col/>', {
				class : 'title'
			}).appendTo(this.colgroup);

			this.thead.append(this._createHeaderRow());

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
						indexer: this.options.indexer,
						media : this.options.media,
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
			if (this.options.media != null) {
				this.input.val('');
				this.tbody.empty();
				this.table.hide();
				this.element.hide();
				this.options.indexer = null;
				this.options.media = null;
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
			var date = '';
			if (data.date) {
				date = data.date.substr(0, 4);
			}
			
			var html = '<tr>';
			html += '<td>' + data.title + '</td>';
			html += '<td>' + date + '</td>';
			html += '<td><span class="stars">' + data.rating
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
				url : 'v1/idx/' + this.options.media,
				data : {
					query : query
				},
				success : function(data, status, jqXHR) {
					widget.options.indexer = data.indexer;
					
					widget.tbody.empty();
					var row;
					var buffer = [];
					for (var i = 0; i < data.results.length; i++) {
						buffer.push(widget._createRow(data.results[i]));
					}
					widget.tbody.append(buffer);
					widget.tbody.find('span.stars').stars();
					widget.table.show();
				}
			});
		}
	});
})(jQuery);