# -MELI-Test-Gestion-Operativa | SCRIPT REQUEST API MELI
## Descripcion 
**search_seller.py** es un script que realiza una request a la API de Mercado Libre. Como respuesta obtenemos todos los items de un site 
dado un vendedor. Ademas como salida obtendremos un archivo LOG con los siguientes datos:

 * *'id'* del item
 * *'title'* del item
 * *'category_id'* donde esta publicado
 * *'name'* de la categoria
 
## Caracteristicas Clave
  
  * Se puede ejecutar en Windows 10 y GNU Linux.
  * Se puede realizar consultas a la API con diferentes **token** de User.
  * Se puede realizar consultas a la API con diferentes **seller_id** de User.
    
 # Linea de Comando
 
 Antes de utilizar el script tenga en cuenta lo siguiente:
 
 * Necesitara de un TOKEN de conexion, autorizado por la API de MELI. En caso de no contar con ello, ver DOCUMENTACION DE API MELI para obtenerlo.
 * Ademas necesitara de un ID de vendedor activo en MELI.
  
# Requerimientos
**search_seller.py** utiliza los siguientes modulos externos para su utilizacion:


 * json
 * requests
 * argparse
 * time

# Modo de Uso
  Es muy sencillo:
  
  Clonamos este repositorio:
  git clone https://github.com/Marc0s94/-MELI-Test-Gestion-Operativa.git
  
  #Nos dirigimos a la ruta del script:
  cd -MELI-Test-Gestion-Operativa
  
  #Podemos ver la ayuda del script:
  
  ![image](https://user-images.githubusercontent.com/25506305/116181992-f6084b80-a6f1-11eb-8b0b-6974abcb9e37.png)
  
  Como vemos nos pides dos parametros, Token y seller_id.

 
