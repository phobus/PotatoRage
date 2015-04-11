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
		html += '<th>Id</th>';
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
			date = data.release_date.substr(0,4);
		} else if (data.first_air_date) {
			date = data.first_air_date.substr(0,4);
		}

		var html = '<tr>';
		html += '<td>' + data.id + '</td>';
		html += '<td>' + title + '</td>';
		html += '<td>' + date + '</td>';
		html += '<td>' + data.vote_average + '</td>';
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
				for (var i = 0; i < data.results.length; i++) {
					rows += widget._createRow(data.results[i]);
				}
				widget.tbody.append(rows);
				widget.table.show();
			}
		});
	}
});