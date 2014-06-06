/* JS File */

// Start Ready
$(document).ready(function() {  
	// Live Search
	// On Search Submit and Get Results
	function search() {
		var query_value = $('input#search').val();
		$('b#search-string').html(query_value);
		if(query_value !== ''){
			$.ajax({
				type: "GET",
				url: "/streets/" + query_value,
				data: { query: query_value },
				cache: false,
				success: function(html){
					$("ul#results").html(list_results(html["streets"]));
				}
			});
		}return false;    
	}

	$("input#search").live("keyup", function(e) {
		// Set Timeout
		clearTimeout($.data(this, 'timer'));

		// Set Search String
		var search_string = $(this).val();

		// Do Search
		if (search_string == '') {
			$("ul#results").fadeOut();
			$('h4#results-text').fadeOut();
		}else{
			$("ul#results").fadeIn();
			$('h4#results-text').fadeIn();
			$(this).data('timer', setTimeout(search, 100));
		};
	});
	function list_results(results) {
		results.each(function(index,item) {
			ul.append(
				$(document.createElement('li')).text(item)
				);
		});
	}
});
