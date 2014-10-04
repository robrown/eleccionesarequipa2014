<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Conteo de Votos</title>
 	<link rel="stylesheet" type="text/css" href="/css/estilo.css" />
    <!-- CSS de Bootstrap -->
    <link href="/css/bootstrap.css" rel="stylesheet" media="screen">
    <link href="/css/bootstrap.min.css" rel="stylesheet" media="screen">
 
	<script type="text/javascript">
	function justNumbers(e)
	{
	var keynum = window.event ? window.event.keyCode : e.which;
	if ((keynum == 8) || (keynum == 46) || (keynum ==0))
	return true;
	 
	return /\d/.test(String.fromCharCode(keynum));
	}
	</script>
</head>
<body>
	<h1>Bienvenido {{username}}</h1>
	<form action="/buscar_mesa" method="POST">
		INGRESE LA MESA:
	<input type="text" name="mesa" size="6" value="" onkeypress="return justNumbers(event);" maxlength="6" autofocus ><br>
	<input type="submit" value="Enviar">
	</form>
</body>
</html>