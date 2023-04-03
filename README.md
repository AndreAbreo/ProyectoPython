# ProyectoPython
## Tercera entrega del curso de Python comision 40425 por André Abreo.
Se trata de un Blog relacionado a los comics, con 3 modeloes para carga de datos que son las revistas de comics, personajes de comics y usuarios de la APP.

El proyecto ya tiene todo el CRUD terminado y listo para probar.
Cada botón ya está linkeado a su respectiva url y cuenta con toda la consigna del curso

## admin/
Se accede a la página de admin de django (usuario "admin" pass "1234")
## [name='inicio']
Página de inicio con botones linkeados para recorrer toda la APP
## productos [name='consultar']
Página de creación de productos con listado de items creados
## productos/guardar [name='guardar']
Guardado de datos de producto
## productos/eliminar/<int:id> [name='eliminar']
Eliminación de datos de producto
## productos/detalle/<int:id> [name='detalle']
Vista de datos de producto
## productos/editar [name='editar']
Modificacion de datos de producto
## productos/list [name='producto-list']
Página de busqueda de productos
## heroes [name='consultar1']
Página de creación de personajes con listado de items creados
## heroes/guardar1 [name='guardar1']
Guardado de datos de personaje
## heroes/eliminar1/<int:id> [name='eliminar1']
Eliminación de datos de personaje
## heroes/detalle1/<int:id> [name='detalle1']
Vista de datos de personaje
## heroes/editar1 [name='editar1']
Modificacion de datos de personaje
## heroes/list [name='heroe-list']
Página de busqueda de personajes
## usuarios [name='consultar2']
Página de creación de usuarios con listado de items creados
## usuarios/guardar2 [name='guardar2']
Guardado de datos de usuario
## usuarios/eliminar2/<int:id> [name='eliminar2']
Eliminación de datos de usuario
## usuarios/detalle2/<int:id> [name='detalle2']
Vista de datos de usuario
## usuarios/editar2 [name='editar2']
Modificacion de datos de usuario
## usuarios/list [name='usuario-list']
Página de busqueda de usuarios

# Se recomienda ingresar directamente a la APP y probar todas las funcionalidades con sus botones correspondientes. 
## Recuerde correr el servidor de django para hacer funcionar la APP
python manage.py runserver
