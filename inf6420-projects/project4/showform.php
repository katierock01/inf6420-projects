<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<title>Processing Form Data</title>
<style type="text/css">
code {color:#F00C4D;font-weight:bold;font-size:1.2em}
i {color: #6D0CF0}
th, td {padding:.1em;border:1px solid blue;text-align:left}
p {font-size:.9em;font-style:italic}
</style>
</head>
<body>
<p>This is a very simple PHP script that outputs the name of each bit of information (that corresponds to the <code>name</code> attribute for that field) along with the value that was sent with it right in the browser window.</p>
<p>In a more useful script, you might store this information in a MySQL database, or send it to your email address.</p>
<table>
<tr><th>Field Name</th><th>Value(s)</th></tr>

<?php
if (empty($_POST)) {
	print "<p>No data was submitted.</p>";
} else {

foreach ($_POST as $key => $value) {
	if (get_magic_quotes_gpc()) $value=stripslashes($value);
	if ($key=='extras') {
		
	if (is_array($_POST['extras']) ){
		print "<tr><td><code>$key</code></td><td>";
		foreach ($_POST['extras'] as $value) {
				print "<i>$value</i><br />";
				}
				print "</td></tr>";
		} else {
		print "<tr><td><code>$key</code></td><td><i>$value</i></td></tr>\n";
		}
	} else {

	print "<tr><td><code>$key</code></td><td><i>$value</i></td></tr>\n";
	}
}
}
?>
</table>
</body>
</html>
