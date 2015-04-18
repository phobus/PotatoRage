(function($) {
	'use strict';
	$.widget("pr.searchActions", {
		options : {
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
		
		saveMedia: function(id) {
			var widget = this;
			$.ajax({
				type : 'POST',
				url : 'api/idx/' + this.options.media,
				data : {
					id : id
				},
				success : function(data, status, jqXHR) {
					
				}
			});
		}
	});
})(jQuery);