$(document).ready(function() {
	$('#execute-search-serie').click(function() {
		var seriesname = $('#search-serie').val();
		getSeries(seriesname);
	});
});

function getSeries(seriesname) {
	var oData = {
		seriesname : seriesname
	};

	var oSuccess = function(response) {
		var output =  $('#output');
		output.append(response.result+'</br>');
		for(var i=0; i<response.data.length; i++){
			output.append('</br>seriesname:</br>');
			output.append(response.data[i].seriesname+'</br>');
			output.append('</br>network</br>');
			output.append(response.data[i].network+'</br>');
			output.append('</br>overview</br>');
			output.append(response.data[i].overview+'</br>');
		}
	};

	$.ajax({
		url : 'api/GetSeries/' + seriesname,
		// data : oData,
		success : oSuccess
	});
}