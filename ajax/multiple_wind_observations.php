<?php
	$start = $_GET['start'];
	$end = $_GET['end'];
	$data = '';

	if ($start != null && $end != null) {
		$data = file_get_contents('http://nuwind.herokuapp.com/observations/multiple/?start=' . $start . '&end=' . $end);
		echo $data;
	} else {
		$data = file_get_contents('http://nuwind.herokuapp.com/observations/multiple/');
		echo $data;
	}
?>