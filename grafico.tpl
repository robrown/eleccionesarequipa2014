<!DOCTYPE html>
<html lang="es">
  <head>
   <meta charset="utf-8">
   <title>RESULTADOS</title>
   
   <script type="text/javascript" src="js/Chart.js"></script>
 </head>
 <body>
 	<div style="width: 50%">
			<canvas id="canvas" height="450" width="600"></canvas>
	</div>
 	<script>
 
	var randomScalingFactor = function(){ return Math.round(Math.random()*100)};

	var barChartData = {
		labels : ["AREQUIPA RENACE","ACCION POPULAR","ALIANZA PARA EL PROGRESO DE AREQUIPA",
	"UNIDOS POR EL GRAN CAMBIO","AVANCEMOS YANAHUARA","FUERZA AREQUIPENA","FUERZA POPULAR",
	"RESTAURACION NACIONAL","JUNTOS POR EL DESARROLLO DE AREQUIPA","PARTIDO POPULAR CRISTIANO",
	"PERU PATRIA SEGURA","UNION POR EL PERU","VAMOS AREQUIPA",
	"VAMOS PERU","YANAHUARA UN SENTIMIENTO Y TRABAJO","BLANCO","NULO"],
		datasets : [
			{
				fillColor : "rgba(58,156,8,0.5)",
				strokeColor : "rgba(220,220,220,0.8)",
				highlightFill: "rgba(220,220,220,0.75)",
				highlightStroke: "rgba(220,220,220,1)",
				data : ['{{renace}}','{{accion}}','{{alianza}}','{{unidos}}','{{avancemos}}','{{fuerza}}','{{popular}}','{{restauracion}}','{{juntos}}','{{ppc}}','{{patria}}','{{union}}','{{vamos}}','{{peru}}','{{yanahuara}}','{{blanco}}','{{nulo}}']
			}
		]

	}
	window.onload = function(){
		var ctx = document.getElementById("canvas").getContext("2d");
		window.myBar = new Chart(ctx).Bar(barChartData, {
			responsive : true
		});
	}

	</script>
 </body>
</html>