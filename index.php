<?php
ob_start();
?>
<div class="row">
	<div class="col-md-offset-1 col-md-10">
		<div class="row">
			<div data-wind-speed-chart class="col-md-12"></div>
		</div>
		<div class="row">
			<div data-pressure-chart class="col-md-6"></div>
			<div data-temperature-chart class="col-md-6"></div>
		</div>
		<div>
			<h4 data-wind-speed></h4>
			<h4 data-pressure></h4>
			<h4 data-temperature></h4>
		</div>
	</div>
</div>
<?php
$body = ob_get_clean();
include('base.php');
?>
