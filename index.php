<?php

// configuration
$url = 'index.php';
$file = 'photogram_panels.py';

// check if form has been submitted
if (isset($_POST['text']))
{
    // save the text contents
    file_put_contents($file, $_POST['text']);

    // redirect to form again
    header(sprintf('Location: %s', $url));
    printf('<a href="%s">Moved</a>.', htmlspecialchars($url));
    exit();
}

// read the textfile
$text = file_get_contents($file);

?>

<!doctype html>
<html>
<head>

<meta name="viewport" content="width=device-width, initial-scale=1">

<style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}</style>

	<title>3D spectral panels</title>
	<link href="css/ui-lightness/jquery-ui-1.9.2.custom.css" rel="stylesheet">
	<script src="js/jquery-1.8.3.js"></script>
	<script src="js/jquery-ui-1.9.2.custom.js"></script>
	<script>
	$(function() {
		
		$( "#accordion" ).accordion();
		

		

		$( "#button1" ).button();
		$( "#button2" ).button();
		$( "#button3" ).button();
		$( "#button4" ).button();
		$( "#button5" ).button();
		$( "#button6" ).button();
		$( "#button7" ).button();
		$( "#button8" ).button();
		$( "#button9" ).button();
		$( "#button10" ).button();
		$( "#button10" ).button();
		$( "#button11" ).button();
		$( "#button12" ).button();
		$( "#button13" ).button();
		$( "#button14" ).button();
		$( "#button15" ).button();
		$( "#radioset" ).buttonset();
		

		

	});
	</script>
	<style>
	body{
		font: 100% "Trebuchet MS", sans-serif;
	    margin: 50px;
		background-color: white;
		color:black;
	}
	.demoHeaders {
		margin-top: 2em;
	}
	#dialog-link {
		padding: .4em 1em .4em 20px;
		text-decoration: none;
		position: relative;
	}
	#dialog-link span.ui-icon {
		margin: 0 5px 0 0;
		position: absolute;
		left: .2em;
		top: 50%;
		margin-top: -8px;
	}
	#icons {
		margin: 0;
		padding: 0;
	}
	#icons li {
		margin: 2px;
		position: relative;
		padding: 4px 0;
		cursor: pointer;
		float: left;
		list-style: none;
	}
	#icons span.ui-icon {
		float: left;
		margin: 0 4px;
	}
	.fakewindowcontain .ui-widget-overlay {
		position: absolute;
	}
	</style>
</head>

<script type="text/javascript">
      

function leds() {

	$.get("leds_panels.php");
    return false;
}


function photogram_panels() {

	$.get("photogram_panels.php");
    return false;
}



function uv_365() {
    $.get("uv_365.php");
    return false;
}
function uv_385() {
    $.get("uv_385.php");
    return false;
}
function uv_405() {
    $.get("uv_405.php");
    return false;
}
function blue_425() {
    $.get("blue_425.php");
    return false;
}
function blue_445() {
    $.get("blue_445.php");
    return false;
}
function blue_460() {
    $.get("blue_460.php");
    return false;
}
function green_530() {
    $.get("green_530.php");
    return false;
}
function green_570() {
    $.get("green_570.php");
    return false;
}
function yellow_590() {
    $.get("yellow_590.php");
    return false;
}
function red_620() {
    $.get("red_620.php");
    return false;
}
function red_670() {
    $.get("red_670.php");
    return false;
}

function ir_730() {
    $.get("ir_730.php");
    return false;
}

function ir_850() {
    $.get("ir_850.php");
    return false;
}
function ir_950() {
    $.get("ir_950.php");
    return false;
}
function white_4000K() {
    $.get("white_4000K.php");
    return false;
}


function off() {
    $.get("off.php");
    return false;
}

function edit() {
	window.location.href = "edit.php";
    return false;
}

function kill() {
	 $.get("kill.php");
    return false;
}

function backup() {
	 $.get("backup.php");
    return false;
}


function show_edit() {
  var x = document.getElementById("edit");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
} 

</script>

 
<body>




<P align="center">
<h2>3D spectral Panels 2022 :</h2>
<button id="button1" onclick="leds()" style="color: #555555"> LEDs tests</button> LEDs cycles for test<p><p>
<button onclick="uv_365()" style="background-color: #eeccff;">365nm</button>
<button onclick="uv_385()" style="background-color: #eeccff;">380nm</button>
<button onclick="uv_405()" style="background-color: #eeccff;">400nm</button><p>
<button onclick="blue_425()" style="background-color: #CCCCFF;">410nm</button>
<button onclick="blue_445()" style="background-color: #66ccff;">440nm</button>
<button onclick="blue_460()" style="background-color: #66ccff;">455nm</button><p>
<button onclick="green_530()" style="background-color:  #66ff33;">515nm</button>
<button onclick="green_570()" style="background-color: #ffff66;">570nm</button>
<button onclick="yellow_590()" style="background-color: #ff9900;">595nm</button><p>
<button onclick="red_620()" style="background-color: #ff9999;">640nm</button>
<button onclick="red_670()" style="background-color: #ff9999;">660nm</button>
<button onclick="ir_730()" style="background-color:  #ff9999;">730nm</button><p>
<button onclick="ir_850()" style="background-color: #CCCCCC;">850nm</button>
<button onclick="ir_950()" style="background-color: #CCCCCC;">950nm</button><p>
<button onclick="white_4000K()" style="background-color: #FFFFFF;">white 4000K</button>


<button onclick="off()" style="background-color: #555555;">OFF</button><p>
<button id="button2" onclick="photogram_panels()" style="color: #008800">Photogrammetry</button> photogrammetry cycle (14 wavelengths + white)<br><br><p>
<button id="button3" onclick="show_edit()" style="color: #880000">Edit photogrammetry script</button><br><br>
<button id="button4" onclick="kill()" style="color: #880000">Stop script</button>
<button id="button5" onclick="backup()" style="color: #555555">Reload backup script</button><br><br>

    <div id="edit" style="display:none"> 
          
			<!-- HTML form -->
			<form action="" method="post">
			<textarea name="text" cols=80 rows=20><?php echo htmlspecialchars($text) ?></textarea>
			<input type="submit" />
			<input type="reset" />
			</form>
    </div> 





</body>
</html>
