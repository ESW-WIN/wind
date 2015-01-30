<?php
ob_start();
?>
<div class="row">
	<div class="col-md-offset-3 col-md-6">
		<?php
		$panelTitle = "About";
		ob_start();
		?>
		<p>Engineers for a Sustainable World (ESW) is a nationwide organization committed to building a better world. ESW is comprised of students, university faculty and professionals who are dedicated to building a more sustainable world for current and future generations.</p>
		<p>The Wind Initiative at Northwestern (WIN), is an ESW group whose goal is to raise awareness and visibility of wind power on campus and to educate people about renewable energy solutions. One of our ongoing projects involves gathering and analyzing wind data in order to assess the feasibility of installing rooftop wind turbines on campus buildings. We believe wind power is an important energy source and will only grow in importance in the future.</p>
		<?php
		$panelBody = ob_get_clean();
		include('panel.php');
		?>
	</div>
</div>
<?php
$body = ob_get_clean();
include('base.php');
?>
