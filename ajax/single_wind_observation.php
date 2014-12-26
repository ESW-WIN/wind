<?php
	$time = $_GET['time'];

	if ($time != null) {
		$data = file_get_contents('http://nuwind.herokuapp.com/observations/single/?time='.$time);
		echo $data;
	} else {
		$data = file_get_contents('http://nuwind.herokuapp.com/observations/single/');
		echo $data;
	}
?>