# Gestiones Ambientales del Caribe SAS (GAC SAS) 🌿

Plataforma web corporativa moderna, profesional y responsiva desarrollada con **Python** y **Streamlit**, diseñada especialmente para **Gestiones Ambientales del Caribe SAS (GAC SAS)**, empresa líder en el manejo, clasificación y tratamiento de residuos sólidos no peligrosos en Barranquilla y la Costa Caribe.

---

## 📋 Características Principales

1. **Identidad Corporativa y Paleta Ambiental:**
   - **Verde Bosque Profundo (`#1B4332`):** Encabezados, títulos y acentos principales.
   - **Verde Esmeralda (`#2D6A4F`):** Subtítulos, botones e interactividad.
   - **Verde Menta Suave (`#D8F3DC` / `#B7E4C7`):** Badges, etiquetas y fondos destacados.
   - **Fondo Limpio (`#F8FAF9`):** Contraste suave, evitando fatiga visual.
   - **Tipografía Moderna:** Sans-serif nítida (`Plus Jakarta Sans`), con jerarquía visual equilibrada.

2. **Diseño Compacto (Anti-scroll Excesivo):**
   - Distribución eficiente en columnas (`st.columns`), tarjetas (`cards`) y pestañas (`st.tabs`).
   - Cada sección se visualiza cómodamente sin obligar al usuario a desplazamientos verticales extensos.

3. **Navegación Intuitiva en Sidebar:**
   - Logotipo corporativo institucional en la parte superior izquierda.
   - Menú de radio personalizado sincronizado con estado de sesión (`st.session_state`).
   - 5 Secciones clave:
     1. **Inicio:** Hero corporativo, descripción de valor, indicadores clave y llamados a la acción (CTA).
     2. **Quiénes Somos:** Identidad desde 2021, visión de tratamiento y 3 pilares diferenciales.
     3. **Servicios:** Pestañas visuales con valor agregado estructurado para:
        - *Gestión de residuos* (Diagnóstico y trazabilidad documental).
        - *Jardinería y zonas verdes* (Planes preventivos y compostaje de biomasa).
        - *Obras civiles* (Puntos ecológicos y centros de acopio normativos).
     4. **Cómo Trabajamos:** Flujo secuencial de 4 fases (Entendemos la operación, Revisamos lo que se genera, Organizamos la clasificación, Evaluamos el resultado real) y banner del *Principio de Personalización GAC*.
     5. **Contáctenos:** Datos oficiales de contacto directo (Teléfono/WhatsApp: `+57 301 622 6317`, Correo: `gac-sas@miempresa.co`, Barranquilla) y formulario corporativo de contacto con validación visual.

4. **Gestión Robusta de Activos:**
   - Carga dinámica y segura de imágenes desde `./resources/static/`.
   - Sistema de *fallback* automático con placeholders elegantes en caso de archivos faltantes.

---

## 📁 Estructura del Proyecto

```text
webpages-ai/
├── app.py                      # Aplicación principal de Streamlit
├── requirements.txt            # Dependencias del proyecto (streamlit, pillow)
├── README.md                   # Documentación técnica y de usuario
├── resources/
│   ├── prompt.md               # Especificación inicial de requerimientos
│   ├── prompt_developer.md     # Especificación senior UI/UX detallada
│   └── static/                 # Logotipo y activos visuales
│       ├── logo.png
│       ├── 01-Inicio.png
│       ├── 02-inicio.webp
│       ├── 02-servicios.webp
│       ├── 03-Jardineria.webp
│       ├── 03-jardineria2.jpeg
│       ├── 03-residuos.png
│       └── contactanos.webp
```

---

## 🚀 Requisitos Previos e Instalación

### 1. Clonar el repositorio o ingresar al directorio:
```bash
cd webpages-ai
```

### 2. Crear y activar un entorno virtual (Recomendado):
**En Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**En Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

---

## 💻 Ejecución de la Aplicación

Para iniciar el servidor local de Streamlit:

```bash
streamlit run app.py
```

O utilizando el entorno virtual directamente:
```powershell
.\.venv\Scripts\streamlit.exe run app.py
```

La aplicación se abrirá automáticamente en su navegador web predeterminado en:
`http://localhost:8501`

---

## 🏢 Contacto Institucional
- **Razón Social:** Gestiones Ambientales del Caribe SAS (GAC SAS)
- **Ubicación:** Barranquilla, Atlántico – Cobertura en toda la Costa Caribe
- **Teléfono / WhatsApp:** [+57 301 622 6317](tel:+573016226317)
- **Correo Corporativo:** [gac-sas@miempresa.co](mailto:gac-sas@miempresa.co)
