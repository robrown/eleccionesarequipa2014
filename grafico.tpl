<!DOCTYPE html>
<html lang="es">
  <head>
   <meta charset="utf-8">
   <title>RESULTADOS</title>
   
   <script type="text/javascript" src="js/Chart.js"></script>
 </head>
 <body>
 	<h1>RESULTADOS</h1>
 	<h2>Mesas computadas {{mesas_compu}}/110 - Porcentaje {{porcentaje_total}}% <h2>
 	<div style="width: 50%">
			<canvas id="canvas" height="450" width="600"></canvas>
	</div>
 	<script>
 
	var randomScalingFactor = function(){ return Math.round(Math.random()*100)};
	var por1 = (('{{renace}}') * 100) / (('{{total}}'));
	var por2 = (('{{accion}}') * 100) / (('{{total}}'));
	var por3 = (('{{alianza}}') * 100) / (('{{total}}'));
	var por4 = (('{{unidos}}') * 100) / (('{{total}}'));
	var por5 = (('{{avancemos}}') * 100) / (('{{total}}'));
	var por6 = (('{{fuerza}}') * 100) / (('{{total}}'));
	var por7 = (('{{popular}}') * 100) / (('{{total}}'));
	var por8 = (('{{restauracion}}') * 100) / (('{{total}}'));
	var por9 = (('{{juntos}}') * 100) / (('{{total}}'));
	var por10 = (('{{ppc}}') * 100) / (('{{total}}'));
	var por11 = (('{{patria}}') * 100) / (('{{total}}'));
	var por12 = (('{{union}}') * 100) / (('{{total}}'));
	var por13 = (('{{vamos}}') * 100) / (('{{total}}'));
	var por14 = (('{{peru}}') * 100) / (('{{total}}'));
	var por15 = (('{{yanahuara}}') * 100) / (('{{total}}'))
	var por16 = (('{{blanco}}') * 100) / (('{{total}}'));
	var por17 = (('{{nulo}}') * 100) / (('{{total}}'));


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
				data : ['{{renace}}','{{accion}}','{{alianza}}','{{unidos}}','{{avancemos}}','{{fuerza}}','{{popular}}','{{restauracion}}','{{juntos}}','{{ppc}}','{{patria}}','{{union}}','{{vamos}}','{{peru}}','{{yanahuara}}','{{blanco}}','{{nulo}}']},
			{
				fillColor : "rgba(12,12,8,0.5)",
				strokeColor : "rgba(220,220,220,0.8)",
				highlightFill: "rgba(220,220,220,0.75)",
				highlightStroke: "rgba(220,220,220,1)",
				data : [por1,por2,por3,por4,por5,por6,por7,por8,por9,por10,por11,por12,por13,por14,por15,por16,por17]

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