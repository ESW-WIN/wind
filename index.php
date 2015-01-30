<?php
ob_start();
?>
<div class="row">
	<div class="col-md-offset-3 col-md-6">
		<div class="row">
			<div class="col-md-12">
				<?php
				$panelTitle = "";
				ob_start();
				?>
				<h1 class="text-center">
					In the last hour, Norris has 
				</h1>
				<h1 class="text-center">
					generated 38 Watts of wind energy!
				</h1>
				<div class="row">
					<div class="col-md-offset-4 col-md-4 text-center">
						<a type="button" class="btn btn-primary btn-lg" href="home.php">Go!</a>
					</div>
				</div>
				<?php
				$panelBody = ob_get_clean();
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
