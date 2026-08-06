🛡️ ANDY TECHNOLOGY SYSTEMS
SIMULADOR DE CONCIENTIZACIÓN — INICIO DE SESIÓN FALSO
Herramienta Educativa de Demostración de Phishing e Ingeniería Social
Prueba de Concepto (PoC) diseñada para mostrar cómo funcionan los mecanismos de engaño en páginas que imitan plataformas oficiales como Facebook y Google. El objetivo es educar sobre su detección, demostrando que los atacantes no necesitan validar tus datos en el momento —solo recibirlos para probarlos después.
⚠️ AVISO LEGAL Y DESLINDE DE RESPONSABILIDAD
FINES EXCLUSIVAMENTE EDUCATIVOS: Este entorno se desarrolló solo para demostración en videos, charlas o análisis personal y autorizado.
USO ÉTICO Y AUTORIZADO: Queda estrictamente prohibido ejecutarlo en dominios públicos, enviarlo a personas ajenas o usarlo para recopilar datos reales sin el consentimiento explícito y por escrito del propietario.
CUMPLIMIENTO LEGAL: La suplantación de identidad y el acceso no autorizado a sistemas informáticos son delitos sancionados por leyes internacionales. El autor no se responsabiliza por el uso indebido o los daños derivados de una ejecución incorrecta.
⚙️ CARACTERÍSTICAS TÉCNICAS
Servidor backend en Python + Flask: Interceptación en tiempo real, con salida clara en consola.
Interfaz profesional: Fondo oscuro con candados de contenido bloqueado, botones al estilo oficial, formularios que se despliegan al seleccionar la plataforma.
Sin estructuras obligatorias: Todos los archivos funcionan juntos en la misma carpeta.
Persistencia visual: Al enviar los datos se muestran inmediatamente en consola, sin validaciones intermedias.
Compatibilidad total: Optimizado para Termux/Android y Linux, con soporte para túneles de acceso remoto.
🚀 INSTALACIÓN Y EJECUCIÓN (Laboratorio Termux / Linux)
Paso 1: Actualizar sistema e instalar dependencias
bash
pkg update && pkg upgrade -y
pkg install python git -y
pip install flask
Paso 2: Clonar el repositorio y acceder a la carpeta
bash
git clone https://github.com/Andyromerook1/andart1.git
cd andart1
Paso 3: Iniciar el servidor
bash
python server.py
Al ejecutarlo verás en pantalla la dirección de acceso: http://0.0.0.0:5000 o http://127.0.0.1:5000. Ingresá desde tu navegador a esa dirección.
🔌 (Opcional) Acceso externo con túnel Cloudflare
Si necesitás compartir el enlace para la demostración:
Abrí una segunda terminal
Ejecutá:
bash
pkg install cloudflared -y
cloudflared tunnel --url http://127.0.0.1:5000
Te devolverá un enlace público seguro para acceder desde cualquier navegador.
📁 ESTRUCTURA DEL PROYECTO
plaintext
andart1/
 ├─ server.py       → Lógica del servidor y recepción de datos
 ├─ index.html      → Página principal con botones y formularios
 ├─ aterrizaje.html → Página final con el "contenido prometido"
 ├─ setup.sh        → Instalador automático de dependencias
 ├─ .gitignore      → Archivos que no se suben al repositorio
 └─ README.md       → Esta documentación completa
🔍 ¿CÓMO FUNCIONA LA DEMOSTRACIÓN?
Ingresás a la página: se ve el fondo negro con candados y el aviso de "contenido bloqueado".
Seleccionás Iniciar con Facebook o Iniciar con Google: se despliega el formulario correspondiente.
Escribís cualquier usuario y contraseña y enviás:
En la página: te lleva al contenido prometido.
En la consola de Termux: aparecen inmediatamente todos los datos ingresados, sin ninguna comprobación previa.
Queda demostrado que el atacante no necesita saber si la clave es correcta en el momento: solo la recibe para probarla luego en la plataforma real.
🛡️ ¿CÓMO DETECTAR Y EVITAR ESTE TIPO DE ATAQUES?
Revisá siempre la dirección en la barra del navegador: solo confiá en dominios oficiales.
Nunca ingresés tus claves en sitios que prometan contenido a cambio de iniciar sesión con redes sociales.
Activá la verificación en dos pasos en todas tus cuentas.
Si te llega un mensaje urgente o amenazante, no hagas clic: ingresá tú mismo a la plataforma oficial desde cero.
📌 NOTA FINAL
Esta herramienta es una réplica controlada diseñada exclusivamente para concientizar. El uso indebido es responsabilidad total de quien lo ejecute y puede tener consecuencias legales graves.
