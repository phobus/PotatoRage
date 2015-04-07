$(document).ready(function() {
	$('#execute-search-serie').click(function() {
		var seriesname = $('#search-serie').val();
		getSeries(seriesname);
	});
});

function getSeries(name) {
	var oData = {
		name : name
	};

	var oSuccess = function(response) {
		var output = $('#output');
		output.html(response.result + '</br>');
		for (var i = 0; i < response.data.length; i++) {
			output.append('</br>seriesid:');
			output.append(response.data[i].seriesid);
			output.append(' | seriesname:');
			output.append(response.data[i].seriesname);
			output.append(' | network:');
			output.append(response.data[i].network);
			output.append(' | language:');
			output.append(response.data[i].language);
		}
	};

	$.ajax({
		url : 'api/series/search',
		data : oData,
		success : oSuccess
	});
}