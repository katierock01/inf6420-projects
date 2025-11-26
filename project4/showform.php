<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<title>Processing Form Data</title>
	<style>
		body {font-family: "Open Sans", Arial, sans-serif; background: #E8F2F7; color: #083B55; margin: 0; padding: 24px;}
		h1 {margin-top: 0;}
		table {width: 100%; border-collapse: collapse; margin-top: 16px; background: #fff;}
		th, td {padding: 0.6em 0.8em; border: 1px solid #0D5A7F; text-align: left; vertical-align: top;}
		th {background: #083B55; color: #fff; text-transform: uppercase; font-size: 0.9em; letter-spacing: 0.05em;}
		code {color: #FF6B63; font-weight: 600; font-size: 1em;}
		ul {list-style: disc; padding-left: 1.5em; margin: 0;}
		.message {background: #fff; border: 1px solid #0D5A7F; padding: 16px; border-radius: 6px;}
	</style>
</head>
<body>
	<h1>Submitted Form Data</h1>
	<p>This helper page lists each submitted field name alongside the value that was sent with it. Use this to confirm your form is sending the expected data.</p>

	<?php
	$payload = $_POST ?: $_GET;

	if (empty($payload)) {
		echo '<div class="message"><strong>No data was submitted.</strong> Please return to the form and try again.</div>';
	} else {
		echo '<table>';
		echo '<thead><tr><th>Field Name</th><th>Value(s)</th></tr></thead>';
		echo '<tbody>';

		foreach ($payload as $key => $value) {
			$safeKey = htmlspecialchars((string) $key, ENT_QUOTES, 'UTF-8');

			if (is_array($value)) {
				echo '<tr><td><code>' . $safeKey . '</code></td><td><ul>';
				foreach ($value as $item) {
					$safeItem = htmlspecialchars((string) $item, ENT_QUOTES, 'UTF-8');
					echo '<li>' . $safeItem . '</li>';
				}
				echo '</ul></td></tr>';
				continue;
			}

			$safeValue = htmlspecialchars((string) $value, ENT_QUOTES, 'UTF-8');
			echo '<tr><td><code>' . $safeKey . '</code></td><td>' . $safeValue . '</td></tr>';
		}

		echo '</tbody></table>';
	}
	?>
</body>
</html>
