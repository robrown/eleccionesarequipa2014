import bottle
import pymongo
import sys

conexion = pymongo.Connection("mongodb://localhost",safe=True)
#conexion = pymongo.MongoClient('localhost',27017)

@bottle.route('/')
def index():
    return bottle.template('ingreso.tpl',{'username':"Rodolfo"})

@bottle.post('/buscar_mesa')
def buscar_mesa():

	mesa = bottle.request.forms.get("mesa")
	if (mesa == None or mesa ==""):
		return '''
			<script type="text/javascript">
				alert("Mesa no valida");
				location.href='/';
			</script> 
			'''
	else:
		mesa = int(mesa)
		query = {'_id':mesa}
		
		db = conexion.test
		name = db.user
		
		try:
			item = name.find_one(query)
		except:
			print "Hubo un error al ejecutar la consulta:" ,sys.exc_info()[0]
	if item == None:
		return '''
			<script type="text/javascript">
				alert("Mesa no encontrada");
				location.href='/';
			</script> 
			'''
	if item['digitada']== True:
		return '''
			<script type="text/javascript">
				alert("La mesa ya fue ingresada");
				location.href='/';
			</script> 
			'''

	ubica = item['ubicacion']
	local = ubica['local']

	return bottle.template('candidatos.tpl',{'mesa':mesa,'local':local['nombre'],
	'electores':item['num_electores'],'username':"Rodolfo",'things':item['candidatos']})
	"""array(item['candidatos'])

def array (cedula):
	print cedula
	return bottle.redirect('candidatos.tpl', username="Rodolfo",mesa="14440", things=cedula)

"""

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
	except:
		print "Hubo un error al ejecutar la consulta:" ,sys.exc_info()[0]
	if suma <= item['num_electores']:
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
	
from bottle import static_file
@bottle.route('/css/<filename>')
def server_static(filename):
  return static_file(filename, root='/home/rodolfo/eleccionesmongo/elecciones/proyecto/yanahuara/css')
@bottle.route('/img/<filename>')
def server_static(filename):
	return static_file(filename, root='/home/rodolfo/eleccionesmongo/elecciones/proyecto/yanahuara/img')

bottle.debug(True)
bottle.run(host='localhost',port=8082)