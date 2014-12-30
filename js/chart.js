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

		generateLinePlot('[data-wind-speed-chart]', windSpeedValues, {
			title: 'Wind Speed',
			xlabel: 'time',
			ylabel: 'speed'
		});
		generateLinePlot('[data-pressure-chart]', pressureValues, {
			title: 'Pressure',
			xlabel: 'time',
			ylabel: 'pressure',
			color: '#000000'
		});
		generateLinePlot('[data-temperature-chart]', pressureValues, {
			title: 'Temperature',
			xlabel: 'time',
			ylabel: 'temperature',
			color: '#EE0000'
		});
		showLabelValue('[data-wind-speed]', 'Wind Speed: ', ' mph', windSpeedValues[windSpeedValues.length - 1][1]);
		showLabelValue('[data-temperature]', 'Temperature: ', ' &#176;F', temperatureValues[temperatureValues.length - 1][1]);
		showLabelValue('[data-pressure]', 'Pressure: ', ' inHg', pressureValues[pressureValues.length - 1][1]);
	}
});

var generateLinePlot = function(element_label, values, attributes) {
		var title = attributes.title || "",
			xlabel = attributes.xlabel || "",
			ylabel = attributes.ylabel || "",
			color = attributes.color || null;
		$(element_label).highcharts({
			title: {
				text: title
			},
			chart: {
				height: 250
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
				},
				floor: 0
			},
			legend: {
				enabled: false
			},
			series: [{
				type: 'spline',
				name: title,
				data: values,
				color: color,
				lineWidth: 3
			}]
		});
	},
	showLabelValue = function(element_label, before, after, value) {
		$(element_label).html(before + value + after);
	};