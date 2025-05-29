<!DOCTYPE html>
<html>
<head>
<meta name="robots" content="noindex,nofollow">
<!--<meta content='width=device-width, initial-scale=1' name='viewport'/>-->
<style type="text/css">

</style>
</head>
<body>

<div style="text-align: center">


<?php
system("sudo i2cset -y 1 0x20 0x14 0x00");
system("sudo i2cset -y 1 0x20 0x15 0x00");
system("sudo i2cset -y 1 0x20 0x14 0x20");
?>
</div>
</body>
<p></p>
</html>