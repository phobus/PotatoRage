$.widget("pr.search", {
	options : {
		type : null
	},

	_create : function() {
		this.element.addClass('ui-widget pr-search');
		this.element.hide();

		this.title = $('<h2/>').appendTo(this.element);

		this.searchBox = $('<div/>').appendTo(this.element);
		this.input = $('<input type="text"/>').appendTo(this.searchBox);
		this.button = $("<button>", {
			text : "Buscar"
		}).appendTo(this.searchBox);

		this.table = $('<table/>').appendTo(this.element);
		this.thead = $('<thead/>').appendTo(this.table);
		this.tbody = $('<tbody/>').appendTo(this.table);

		this.thead.append(this._createHeaderRow());

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
			}
		});

		this._super();
	},

	_destroy : function() {
		this.element.removeClass('ui-widget pr-search');
		this.element.empty();

		this._super();
	},

	_setOption : function(key, value) {
		if (key == 'type') {
			this.tbody.empty();
			this.input.val('');
			if (value == 'series') {
				this.title.text('Series');
				this.element.show();
				this.table.hide();
			} else if (value == 'movies') {
				this.title.text('Peliculas');
				this.element.show();
				this.table.hide();
			} else {
				this.element.hide();
			}
		}
		this._super(key, value);
	},

	_createHeaderRow : function() {
		var html = '<tr class="ui-widget-header">';
		html += '<th/>';
		html += '<th>Nombre</th>';
		html += '<th>Cadena</th>';
		html += '<th>Idioma</th>';
		html += '</tr>';
		return html;
	},

	_createRow : function(idx, data) {
		var html = '<tr>';
		html += '<td>' + idx + '</td>';
		html += '<td>' + data.seriesname + '</td>';
		html += '<td>' + data.network + '</td>';
		html += '<td>' + data.language + '</td>';
		html += '</tr>';
		return html;
	},

	search : function(q) {
		var widget = this;
		$.ajax({
			type : 'GET',
			url : 'api/idx/' + this.options.type,
			data : {
				q : q
			},
			success : function(data, status, jqXHR) {
				widget.tbody.empty();
				var rows = '';
				for (var i = 0; i < data.series.length; i++) {
					rows += widget._createRow(i + 1, data.series[i]);
				}
				widget.tbody.append(rows);
				widget.table.show();
			}
		});
	}
});