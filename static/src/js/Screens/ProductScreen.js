odoo.define('hmindustriales.ProductScreen', function(require) {
    'use strict';

    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    const rpc = require('web.rpc');
    var { Gui } = require('point_of_sale.Gui');
    var core = require('web.core');


    const PosProductScreen = (ProductScreen) =>
      class PosProductScreen extends ProductScreen {
        constructor(){
          super(...arguments);
          console.log('constru')
        }

        async _onClickPay() {
          
          //console.log('inherit hm')
           
          //this.showScreen('ProductScreen');
            console.log('inherit h2')
            var productos_pedido_dicc = await this.productos_pedido();
            var productos_sin_stock = await this.rpc({
                  model: 'pos.order',
                  method: 'buscar_stock',
                  args: [[],productos_pedido_dicc, this.env.pos.picking_type.id]
              });
            
            if (productos_sin_stock.length > 0){
                Gui.showPopup('ErrorPopup', {
                title:  this.env._t('Producto sin stock'),
                body: this.env._t(productos_sin_stock),
              }).then(({ confirmed }) => {

                  console.log("Linea 103");

              });
            }else{
                super._onClickPay();
            }

        }

        async productos_pedido(){
            var self = this;
            var cambiar_pantalla = true;
            var order = self.env.pos.get_order();

            var dicc_lineas_producto = {};


            var dicc_productos = {}

            order.get_orderlines().forEach(function(linea){
                console.log(linea);
                console.log(linea.quantity)
                if (linea.product.id in dicc_productos){
                    dicc_productos[linea.product.id] += linea.get_quantity();                
                }else{
                    if (dicc_productos[linea.product.id] === undefined){
                        dicc_productos[linea.product.id] = 0;
                    }

                    dicc_productos[linea.product.id] += linea.get_quantity();

                }
            });
            return dicc_productos
        } 
          
      };

      Registries.Component.extend(ProductScreen, PosProductScreen);

      return PosProductScreen;
});