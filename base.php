<!DOCTYPE html>
<head>
	<link href="css/bootstrap.min.css" rel="stylesheet">
	<link href="css/base.css" rel="stylesheet">
	<link href="css/weather-icons.css" rel="stylesheet">
</head>
<html>
<body>
	<nav class="navbar navbar-default">
		<div class="container-fluid">
			<!-- Brand and toggle get grouped for better mobile display -->
			<div class="navbar-header">
				<a class="navbar-brand" href="index.php">ESW Wind</a>
			</div>

			<!-- Collect the nav links, forms, and other content for toggling -->
			<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
				<ul class="nav navbar-nav">
					<li><a href="home.php">Home</a></li>
					<li><a href="about.php">About</a></li>
					<li><a href="#Shuttle">Shuttles</a></li>
					<li><a href="#Calendar">Upcoming Events</a></li>
				</ul>
				<ul class="nav navbar-nav navbar-right">
					<li><a class="clock"></a></li>
				</ul>
			</div><!-- /.navbar-collapse -->
		</div><!-- /.container-fluid -->
	</nav>
	<div class="content">
		<?php
			echo $body;
		?>
	</div>
</body>
<script src="js/jquery.min.js"></script>
<script src="js/bootstrap.min.js"></script>
<script src="js/highcharts.js"></script>
<script src="js/chart.js"></script>
<script src="js/clock.js"></script>
</html>