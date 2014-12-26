<?php
ob_start();
?>
<div class="row">
	<div class="col-md-offset-2 col-md-8">
		<div data-my-chart>
		</div>
	</div>
</div>
<?php
$body = ob_get_clean();
include('base.php');
?>
