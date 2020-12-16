function initPayPalButton() {
              paypal.Buttons({
                style: {
                  shape: 'rect',
                  color: 'gold',
                  layout: 'vertical',
                  label: 'paypal',

                },

                createOrder: function(data, actions) {
                  return actions.order.create({
                    purchase_units: [{"description":"If you enjoy this site, consider making a donation to help support the costs of web services.","amount":{"currency_code":"USD","value":1}}]
                  });
                },

                onApprove: function(data, actions) {
                  return actions.order.capture().then(function(details) {
                    alert('Transaction completed by ' + details.payer.name.given_name + '!');
                  });
                },

                onError: function(err) {
                  console.log(err);
                }
              }).render('#paypal-button-container');
            }
            initPayPalButton();