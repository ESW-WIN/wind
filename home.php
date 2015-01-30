<?php
ob_start();
?>
<div class="row">
	<div class="col-md-offset-3 col-md-6">
		<div class="row">
			<div class="col-md-12">
				<div class="panel panel-default panel-transparent">
					<div class="row">
						<div class="col-md-12">
							<h3 class="text-center">How much energy can the wind above Norris generate?</h3>
						</div>
						<div class="col-md-12">
							<div class="text-center">
								<div class="btn-group button-group-justified" role="group">
									<button type="button" class="btn btn-default">Hour</button>
									<button type="button" class="btn btn-default">Day</button>
									<button type="button" class="btn btn-default">Week</button>
									<button type="button" class="btn btn-default">Month</button>
								</div>
							</div>
						</div>
					</div>
					<div class="row">
						<div class="col-md-12">
							<h1 class="text-center">12 Watts</h1>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div class="row">
			<div class="col-md-6">
				<?php
				$panelTitle = "Weather";
				ob_start();
				?>
				<div class="">
					<div class="text-center">
						<div class="wi wi-cloudy" style="font-size: 300%;">
							34&deg;F
						</div>
					</div>
				</div>
				<?php
				$panelBody = ob_get_clean();
				include('panel.php');
				?>
			</div>
			<div class="col-md-6">
				<?php
				$panelTitle = "Sustainability Tips";
				$options = array(
					"unplug electronics: saves money on power bills and saves energy",
					"use cfl lightbulbs, or LEDs",
					"put a timer on electronic devices so they turn off at a certain time",
					"install low flow showerheads ",
					"use house plants as air purifiers",
					"eat less meat :P",
					"take the stairs",
					"reuse before you recycle",
					"bring your own reusable coffee cup",
					"remember to ecyle (recycle ewaste)",
					"buy in bulk",
					"bring your own grocery bag",
					"use public transit",
					"take yourself off junk mail mailing lists",
					"request your energy comes from renewable sources (can request wind energy in illinois)",
					"make your own house cleaner: use vinegar!"
					);
				$panelBody = '<div class="text-center">'.$options[floor(rand(0, count($options) - 1))].'</div>';
				include('panel.php');
				?>
			</div>
		</div>
	</div>
</div>
<?php
$body = ob_get_clean();
include('base.php');
?>
