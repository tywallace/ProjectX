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
				success: function(res){
					list_results(res["streets"]);
				}
			});
		}return false;    
	}

	$("input#search").live("keyup", function(e) {
		$("ul#results").empty();
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

	function list_results(streets) {
		for (i = 0; i < streets.length; ++i) {
			$("ul#results").append('<li>'+streets[i]+"</li>")
				};
		}
});
