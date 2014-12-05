import bottle
import pymongo
import sys


conexion = pymongo.Connection("mongodb://localhost",safe=True)
#conexion = pymongo.MongoClient('localhost',27017)

@bottle.post('/login')
def do_login():
	username = bottle.request.forms.get("username")
	password = bottle.request.forms.get("password")
	if check_login(username, password):
		bottle.response.set_cookie("account", username, secret='some-secret-key')
		return bottle.template('ingreso.tpl', {'username':username})
	else:
		return "<p>Login failed.</p>"

def check_login(usuario,contra):
	try:
		db = conexion.test
		name = db.usuarios
		consulta = {'usuario':usuario}
		item = name.find_one(consulta)
	except:
		print "Hubo un error al ejecutar la consulta:" ,sys.exc_info()[0]
	
	if usuario == item['usuario'] and contra == item['password']:
		return True
	else:
		return False

@bottle.route('/restricted')
def restricted_area():
	username = bottle.request.get_cookie("account", secret='some-secret-key')
	if username:
		return template("Hello {{name}}. Welcome back.", {'username':username})
	else:
		return "You are not logged in. Access denied."

@bottle.route('/')
def index():
    return bottle.template('login.tpl')

@bottle.route('/ingreso')
def ingreso():
	username = bottle.request.get_cookie("account", secret='some-secret-key')
	return bottle.template('ingreso.tpl',{'username':username})

@bottle.post('/buscar_mesa')
def buscar_mesa():

	mesa = bottle.request.forms.get("mesa")
	if (mesa == None or mesa ==""):
		return '''
			<script type="text/javascript">
				alert("Mesa no valida");
				location.href='/ingreso';
			</script> 
			'''
	else:
		mesa = int(mesa)
		query = {'_id':mesa}
		try:
			db = conexion.test
			name = db.user
			item = name.find_one(query)
		except:
			print "Hubo un error al ejecutar la consulta:" ,sys.exc_info()[0]
	if item == None:
		print mesa
		return '''
			<script type="text/javascript">
				alert("Mesa no encontrada");
				location.href='/ingreso';
			</script> 
			'''
	if item['digitada']== True:
		return '''
			<script type="text/javascript">
				alert("La mesa ya fue ingresada");
				location.href='/ingreso';
			</script> 
			'''

	ubica = item['ubicacion']
	local = ubica['local']
	criterio = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
	item['candidatos'].sort(key=lambda x: criterio.index(x['posicion']))
	username = bottle.request.get_cookie("account", secret='some-secret-key')
	return bottle.template('candidatos.tpl',{'mesa':mesa,'local':local['nombre'],'username':username,'things':item['candidatos']})
	#'electores':item['num_electores']


@bottle.post('/candidatos/<cedula>')
def candidatos(cedula):
	mesa = int(cedula)
	query = {'_id':mesa}
	suma = 0

	db = conexion.test
	name = db.user
	try:
	    item = name.find_one(query)
	    indice = 0
	    for voto in item['candidatos']:
	    	cursor = bottle.request.forms.get(voto['simbolo'])
	    	if cursor == "":
	    		cursor = 0
	    	else:
	    		cursor = int(cursor)
	    	item['candidatos'][indice]['votos']= cursor
	    	suma = suma + cursor
	    	indice += 1
	    item['digitada']= True
	    name.save(item)
	    return '''
			<script type="text/javascript">
				alert("Mesa computada satisfactoriamente!!");
				location.href='/ingreso';
			</script> 
	    '''
	except:
		print "Hubo un error al ejecutar la consulta:" ,sys.exc_info()[0]
	"""if suma <= item['num_electores']:
		try:
			item['digitada']= True
			name.save(item)

		except:
			print "Hubo un error al ejecutar la consulta:" ,sys.exc_info()[0]
		return '''
			<script type="text/javascript">
				alert("Mesa computada satisfactoriamente!!");
				location.href='/';
			</script> 
	    '''
	else:
		return '''
			<script type="text/javascript">
				alert("La SUMA de los datos ingresados no concuerdan con los de la mesa");
				history.back();
			</script> 
		    '''
    """
import json
@bottle.route('/resultados')
def resultados():
	pregunta = {'digitada':True}
	db = conexion.test
	name = db.user
	suma = {'AREQUIPA RENACE':0,'ACCION POPULAR':0,'ALIANZA PARA EL PROGRESO DE AREQUIPA':0,
	'UNIDOS POR EL GRAN CAMBIO':0,'AVANCEMOS YANAHUARA':0,'FUERZA AREQUIPENA':0,'FUERZA POPULAR':0,
	'RESTAURACION NACIONAL':0,'JUNTOS POR EL DESARROLLO DE AREQUIPA':0,'PARTIDO POPULAR CRISTIANO':0,
	'PERU PATRIA SEGURA':0,'RESTAURACION NACIONAL':0,'UNION POR EL PERU':0,'VAMOS AREQUIPA':0,
	'VAMOS PERU':0,'YANAHUARA UN SENTIMIENTO Y TRABAJO':0,'BLANCO':0,'NULO':0}
	total_votos = 0
	porcentaje_total = 0
	try:
		item = name.find(pregunta)
		mesas_compu= name.find(pregunta).count()
	except:
		print "Hubo un error al ejecutar la consulta:" ,sys.exc_info()[0]
	for x in item:
		for y in x['candidatos']:
			dato = suma[y['nombre']]
			dato = int(dato) + int(y['votos'])
			suma[y['nombre']] = dato
			total_votos+= int(y['votos'])
	#print total_votos
	porcentaje_total = (total_votos*100)/24000
	return bottle.template('grafico.tpl', 
		{'renace':suma["AREQUIPA RENACE"],'accion':suma["ACCION POPULAR"],
		'alianza':suma["ALIANZA PARA EL PROGRESO DE AREQUIPA"],'unidos':suma["UNIDOS POR EL GRAN CAMBIO"],
		'avancemos':suma["AVANCEMOS YANAHUARA"],'fuerza':suma["FUERZA AREQUIPENA"],'popular':suma["FUERZA POPULAR"],
		'restauracion':suma["RESTAURACION NACIONAL"],'juntos':suma["JUNTOS POR EL DESARROLLO DE AREQUIPA"],
		'ppc':suma["PARTIDO POPULAR CRISTIANO"],'patria':suma["PERU PATRIA SEGURA"],'union':suma["UNION POR EL PERU"],
		'vamos':suma["VAMOS AREQUIPA"],'peru':suma["VAMOS PERU"],'yanahuara':suma["YANAHUARA UN SENTIMIENTO Y TRABAJO"],
		'blanco':suma["BLANCO"],'nulo':suma["NULO"],'total':total_votos,'mesas_compu':mesas_compu,'porcentaje_total':porcentaje_total})

	
from bottle import static_file
@bottle.route('/css/<filename>')
def server_static(filename):
  return static_file(filename, root='/home/rodolfo/eleccionesarequipa2014/css')
  #Mac
  #return static_file(filename, root='/Users/iServidor/eleccionesarequipa2014/css')

@bottle.route('/img/<filename>')
def server_static(filename):
	return static_file(filename, root='/home/rodolfo/eleccionesarequipa2014/img')
	#return static_file(filename, root='/Users/iServidor/eleccionesarequipa2014/img')

@bottle.route('/js/<filename>')
def server_static(filename):
	return static_file(filename, root='/home/rodolfo/eleccionesarequipa2014/js')
	#return static_file(filename, root='/Users/iServidor/eleccionesarequipa2014/js')

bottle.debug(True)
bottle.run(host='localhost',port=8082)
