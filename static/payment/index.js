var stripe = Stripe('pk_test_51KEZgSGN1xHMll4X7zH9iecvd9KPhyxoiQCDjysHrkIbFmUX4eBxAJLD0KTLkO8xGlaP4VkjOuKIjXjJqCHJY0ye00LHBg8Bg9');

var elem = document.getElementById('submit');
clientsecret = elem.getAttribute('data-secret');

var elements = stripe.elements();
var style = {
    base : {
        color: '#000',
        lineHeight: '2.4',
        fontSize: '16px'
    }
};

var card = elements.create("card", {style: style});
card.mount("#card-element");

card.on('change', function(e){
    var displayError = document.getElementById('card-errors')
    if(event.error){
        displayError.textContent = event.error.message;
        $('#card-errors').addClass('alert alert-info');
    } else {
        displayError.textContent = '';
        $('#card-errors').removeClass('alert alert-info');
    }
});