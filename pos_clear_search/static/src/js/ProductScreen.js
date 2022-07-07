odoo.define('pos_clear_search.productScreen', function(require) {
	"use strict";

	const Registries = require('point_of_sale.Registries');
	const ProductScreen = require('point_of_sale.ProductScreen');
	const SearchProductScreen = (ProductScreen) =>
		class extends ProductScreen {
			constructor() {
				super(...arguments);
			}
			async _clickProduct(event) {
				let call_super = true;
				var clear_search = document.getElementById("clear_search_icon");
				clear_search.click();
				if(call_super){
					super._clickProduct(event);
				}
			}
		};

	Registries.Component.extend(ProductScreen, SearchProductScreen);
	return ProductScreen;
});
