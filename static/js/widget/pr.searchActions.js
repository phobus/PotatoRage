(function($) {
	'use strict';
	$.widget("pr.searchActions", {
		options : {
			media: null,
			id: null,
			back : function() {
			},
			save : function() {
			}
		},

		_create : function() {
			this.element.addClass('ui-widget pr-search-actions');

			this.save = $("<button>", {
				text : "Añadir a mi coleccion"
			}).appendTo(this.element);

			this.back = $("<button>", {
				text : "Volver a la busqueda"
			}).appendTo(this.element);

			this._on(this.save, {
				click : function(event) {
					this.saveMedia();
					this._trigger('save', event);
				}
			});

			this._on(this.back, {
				click : function(event) {
					this._trigger('back', event);
				}
			});
			this._super();
		},

		_destroy : function() {
			this.element.removeClass('ui-widget pr-search-actions');
			this.element.empty();

			this._super();
		},
		
		saveMedia: function() {
			var widget = this;
			$.ajax({
				type : 'POST',
				url : 'api/idx/' + this.options.media,
				data : {
					id : this.options.id
				},
				success : function(data, status, jqXHR) {
					console.log(data);
				}
			});
		}
	});
})(jQuery);