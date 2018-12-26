var ajaxLoading = false;
document.addEventListener('DOMContentLoaded', () => {

	// Have each button save the request to the session
	document.querySelectorAll('.item').forEach(function(button) {
		button.onclick = function() {
			// Initialize new request
			
			const price_id = button.dataset.id;
			const item_type = button.dataset.type;
			const operation = button.dataset.operation;
			var items_in_cart = document.getElementById("items_in_cart");
			button.disabled = true;
			if(operation === "add" && ajaxLoading === false) {
				ajaxLoading = true;
				$.ajax({
					url: '/add_item',
					data:{
						price_id: price_id,
						item: item_type
					},
					success: function(data) {
						button.disabled = false;
						button.title = "Remove from the cart";
						button.classList.add("itemIsSelected");
						button.dataset.operation = "remove";

						if (items_in_cart.innerHTML != ""){
							items_in_cart.innerHTML = parseInt(items_in_cart.innerHTML)+1;
						}
						else {
							items_in_cart.innerHTML = 1
						}
						ajaxLoading = false;
					},
					failure: function(data) { 
						button.disabled = false;
						alert('Got an error dude');
						ajaxLoading = false;
					}
				});
			}
			debugger
			if(operation === "remove" && ajaxLoading === false) {
				ajaxLoading = true;
				$.ajax({
					url: '/remove_item',
					data:{
						price_id: price_id,
						item: item_type
					},
					success: function(data) {
						debugger
						button.title = "Add to the cart";
						button.classList.remove("itemIsSelected");
						button.dataset.operation = "add";
						if (items_in_cart.innerHTML != ""){
							if(parseInt(items_in_cart.innerHTML) <= 1){
								items_in_cart.innerHTML = "";
							}
							else{
								items_in_cart.innerHTML = parseInt(items_in_cart.innerHTML)-1;
							}
							
						}
						ajaxLoading = false;
					},
					failure: function(data) { 
						
						alert('Got an error dude');
						ajaxLoading = false;
					}
				});
			}
			
			
			return false;
		};
	});

	
	
});
