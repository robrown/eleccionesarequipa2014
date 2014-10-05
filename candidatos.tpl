<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>CANDIDATOS MESA </title>
	<link rel="stylesheet" type="text/css" href="/css/estilo.css" media="screen">
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
	<p> Bienvenido {{username}}</p>
	<h1> MESA NUMERO {{mesa}}</h1>
	<p>LOCAL {{local}} </p>
	<section>
		<form action="/candidatos/{{mesa}}" method="POST">
		%for thing in things:
		<div>
			<img src="/img/{{thing["simbolo"]}}" width="64" height="64">
				<input type="text" name={{thing["simbolo"]}} size="4" value="" onkeypress="return justNumbers(event);" maxlength="3" autofocus ><br>
		</div>
		%end
		
	</section>
	<div id="boton">
	<input  type="submit" value="Enviar" >
	</div>
</body>
</html>