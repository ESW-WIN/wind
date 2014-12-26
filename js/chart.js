$.ajax({
	url: 'ajax/multiple_wind_observations.php',
	contentType: 'application/json',
	success: function(data, status) {
		data = $.parseJSON(data);
		var windSpeedValues = [],
			temperatureValues = [],
			pressureValues = [];

		for (var i = 0; i < data.length; i++) {
			windSpeedValues.push([data[i]['time'] * 1000, data[i]['wind_speed']]);
			temperatureValues.push([data[i]['time'] * 1000, data[i]['temperature']]);
			pressureValues.push([data[i]['time'] * 1000, data[i]['pressure']]);
		}

		generateLinePlot(windSpeedValues, 'Wind Speed', 'time', 'speed');
		generateLinePlot(temperatureValues, 'Temperature', 'time', 'temperature');
		generateLinePlot(pressureValues, 'Pressure', 'time', 'pressure');
	}
});

var generateLinePlot = function(values, title, xlabel, ylabel) {
	$('[data-my-chart]').highcharts({
		title: {
			text: title
		},
		xAxis: {
			type: 'datetime',
			title: {
				text: xlabel
			}
		},
		yAxis: {
			title: {
				text: ylabel
			}
		},
		legend: {
			enabled: false
		},
		series: [{
			name: title,
			data: values
		}]
	});
}