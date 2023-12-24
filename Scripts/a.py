import requests

def hacer_peticion(url):
    respuesta = requests.get(url)
    
    # Verificar el código de respuesta
    if respuesta.status_code == 301:
        # Obtener la nueva ubicación desde las cabeceras de la respuesta
        nueva_url = respuesta.headers['Location']
        
        # Hacer una nueva petición a la nueva ubicación
        nueva_respuesta = requests.get(nueva_url)
        
        # Devolver la respuesta de la nueva ubicación
        return nueva_respuesta
    else:
        # Devolver la respuesta original si no es un redireccionamiento
        return respuesta

# Ejemplo de uso
url_original = "https://ejemplo.com"
respuesta_final = hacer_peticion(url_original)

print(respuesta_final.text)