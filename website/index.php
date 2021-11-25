<html>
  <head>
  </head>

  <body>
    <h1>Unser Portfolio</h1>
    <ul>
      <?php
        $json = file_get_contents('http://python-service');
	$obj = json_decode($json);

	$services = $obj->services;

	foreach($services as $service)
	{
	  echo "<li>$service</li>";
	}
      ?>
    </ul>
  </body>
</html>
