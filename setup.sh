#!/bin/bash
# Script de configuración automática
echo "[*] Instalando dependencias de Andy Technology..."
pkg update && pkg upgrade -y
pkg install python git -y

echo "[*] Configurando permisos..."
chmod +x server.py
touch registro_privado.txt
chmod 666 registro_privado.txt

echo "[*] Todo listo. Para iniciar el servidor escribe: python server.py"