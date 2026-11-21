# Rol y Objetivo
Actúa como un Desarrollador Senior de Python especializado en Streamlit y Diseño UI/UX corporativo. Tu objetivo es desarrollar una aplicación web multipágina limpia, profesional y responsiva para **Gestiones Ambientales del Caribe SAS (GAC SAS)**, una empresa dedicada al manejo de residuos sólidos no peligrosos en Barranquilla y la Costa Caribe.

---

# 1. Arquitectura y Estructura del Proyecto
- **Archivo principal:** `app.py` (código modular, limpio, bien comentado y siguiendo estándares PEP 8).
- **Gestión de activos:** Carga las imágenes y el logotipo dinámicamente desde el directorio local `./resources/static/` utilizando `pathlib` o `os.path`.
- **Manejo de errores:** Implementa una función auxiliar para cargar imágenes que muestre un contenedor visual elegante (placeholder con icono o mensaje) en caso de que algún archivo específico aún no exista en `./resources/static/`.
- **Configuración de página:** Usa `st.set_page_config(page_title="GAC SAS | Gestiones Ambientales del Caribe", page_icon="🌿", layout="wide", initial_sidebar_state="expanded")`.

---

# 2. Sistema de Diseño (UI/UX) y Paleta de Colores
Inyecta CSS personalizado mediante `st.markdown(..., unsafe_allow_html=True)` para garantizar una estética corporativa y ambiental:
- **Paleta de colores:**
  - *Primario (Verde Bosque Profundo):* `#1B4332` (títulos principales, encabezados, acentos fuertes).
  - *Secundario (Verde Esmeralda / Hoja):* `#2D6A4F` (subtítulos, botones, bordes activos).
  - *Acento Suave (Verde Menta Claro):* `#D8F3DC` (fondos de tarjetas destacadas, badges).
  - *Fondo Principal:* `#F8FAF9` (blanco hueso muy sutil para evitar fatiga visual).
  - *Texto Principal:* `#1E293B` (gris pizarra oscuro, alta legibilidad).
- **Tipografía y Layout:**
  - Fuentes limpias sans-serif (`Inter`, `Roboto` o `sans-serif` del sistema).
  - **Diseño compacto (Anti-scroll excesivo):** Utiliza columnas (`st.columns`), tarjetas con bordes sutiles y pestañas (`st.tabs`) o selectores horizontales para que cada vista quepa cómodamente en pantalla sin requerir desplazamientos verticales interminables.
  - Estilo sobrio, sin animaciones estridentes ni exceso de efectos visuales.

---

# 3. Navegación (Sidebar Izquierdo)
- En la parte superior del `st.sidebar`, muestra el logotipo de la empresa (`./resources/static/logo.png` o el archivo de logo disponible) acompañado del nombre **GAC SAS**.
- Implementa un menú de navegación limpio (usando `st.radio` estilizado como botones de navegación o `streamlit-option-menu` si se incluye en dependencias) con las siguientes 5 secciones:
  1. `Inicio`
  2. `Quiénes Somos`
  3. `Servicios`
  4. `Cómo Trabajamos`
  5. `Contáctenos`
- Añade al pie del sidebar una breve nota institucional: *"Barranquilla y Costa Caribe • Desde 2021"*.

---

# 4. Especificación de Contenido por Sección

### Sección 1: Inicio
- **Layout:** Distribución en 2 columnas (60% texto / 40% imagen destacada de operaciones).
- **Contenido:**
  - **Título / Hero:** Gestiones Ambientales del Caribe SAS (GAC SAS).
  - **Subtítulo:** Tratamiento de residuos sólidos no peligrosos.
  - **Copy principal:**
    - Clasificamos y tratamos los materiales según cada operación. Al revisar sus volúmenes y costos actuales, podemos identificar oportunidades de aprovechamiento y evaluar posibles ahorros, sin asumir que todas las empresas obtendrán el mismo resultado.
    - Un manejo más organizado permite estudiar el aprovechamiento de materiales y el costo de gestionarlos.
  - **Llamado a la acción (CTA):** Un botón sutil que invite a explorar los servicios o contactar.

### Sección 2: Quiénes Somos
- **Layout:** Encabezado limpio + distribución balanceada entre información corporativa, métricas/hitos clave y fotografía institucional.
- **Contenido:**
  - **Badge / Dato clave:** *Tratamiento de residuos sólidos no peligrosos | Operando desde 2021*.
  - **Descripción:**
    - GAC Gestiones Ambientales del Caribe SAS trabaja con empresas de Barranquilla y la Costa Caribe que generan grandes cantidades de residuos sólidos no peligrosos y buscan organizar su manejo.
    - Clasificamos y tratamos los materiales según cada operación. Al revisar sus volúmenes y costos actuales, podemos identificar oportunidades de aprovechamiento y evaluar posibles ahorros, sin asumir que todas las empresas obtendrán el mismo resultado.
  - **Valores diferenciales (en 3 mini-tarjetas horizontales):** Enfoque a la medida, Trazabilidad operativa, Cobertura en la Costa Caribe.

### Sección 3: Servicios
- **Layout:** Para mantener la página compacta y visualmente atractiva, presenta los 3 servicios mediante **pestañas (`st.tabs`)** o **3 tarjetas en columnas** con imagen superior, título, descripción y el valor agregado sugerido.
- **Contenido y Sugerencias de Valor Agregado:**
  1. **Gestión de residuos**
     - *Descripción:* Identificamos las corrientes de residuos, los volúmenes y los costos actuales de manejo. Con esa información definimos dónde conviene intervenir para organizar la separación según los materiales y el ritmo de trabajo de la empresa.
     - *Sugerencia incluida (Enfoque / Entregable):* **Diagnóstico inicial y trazabilidad:** Entrega de informes periódicos de volúmenes clasificados y soporte documental para la gestión ambiental interna de la empresa.
  2. **Jardinería y zonas verdes**
     - *Descripción:* Realizamos labores de jardinería y mantenimiento de áreas verdes empresariales. Revisamos las condiciones del terreno y la vegetación para acordar las tareas y la frecuencia que necesita el espacio.
     - *Sugerencia incluida (Enfoque / Entregable):* **Planes preventivos y compostaje:** Programación periódica adaptada al clima del Caribe y aprovechamiento responsable del material vegetal resultante de las podas.
  3. **Obras civiles**
     - *Descripción:* Atendemos necesidades de adecuación y mantenimiento vinculadas a las instalaciones y de acuerdo al espacio.
     - *Sugerencia incluida (Enfoque / Entregable):* **Adecuación de puntos ecológicos y centros de acopio:** Construcción y mejora de cuartos de residuos cumpliendo con normativas de higiene, señalización y seguridad industrial.

### Sección 4: Cómo Trabajamos
- **Layout:** Presentación tipo flujo de trabajo paso a paso en una cuadrícula de **2x2 tarjetas** o **4 columnas compactas** (cada una con su imagen/ilustración correspondiente, número de fase, título y texto).
- **Contenido de las 4 Fases:**
  1. **01. Entendemos la operación:** Conversamos sobre lo que la empresa genera, cómo se mueve dentro de sus instalaciones y cuánto cuesta gestionarlo hoy. El alcance se diseña según los tipos de residuos, los volúmenes y la operación específica de cada cliente; no se traslada el mismo esquema de una empresa a otra.
  2. **02. Revisamos lo que se genera:** Conversamos sobre la operación, identificamos las corrientes de residuos sólidos no peligrosos y revisamos volúmenes y costos actuales. Esa información permite reconocer dónde conviene intervenir.
  3. **03. Organizamos la clasificación:** Definimos un manejo ajustado a los materiales y al ritmo de trabajo de la empresa. Una separación más clara facilita el tratamiento y permite identificar oportunidades de aprovechamiento.
  4. **04. Evaluamos el resultado real:** Contrastamos las opciones de manejo con los costos de la organización. El posible ahorro se estudia caso por caso: depende de la información, los residuos y la operación de cada cliente.
- **Sugerencia incluida (Cierre de sección):** Un pequeño banner informativo que resalte el **"Principio de Personalización GAC"**: *Cada diagnóstico parte de datos reales de operación, evitando soluciones genéricas.*

### Sección 5: Contáctenos
- **Layout:** 2 columnas (Izquierda: Tarjeta con datos de contacto directo y ubicación; Derecha: Formulario visual de contacto).
- **Contenido Columna Izquierda:**
  - **Empresa:** Gestiones Ambientales del Caribe SAS (GAC SAS)
  - **Teléfono / WhatsApp:** +57 301 622 6317
  - **Correo electrónico:** gac-sas@miempresa.co
  - **Ubicación:** Barranquilla, Atlántico – Cobertura en la Costa Caribe.
- **Contenido Columna Derecha (Formulario sin envío real):**
  - Construido con `st.form("contact_form")`.
  - Campos: Nombre completo, Empresa, Correo electrónico, Teléfono, Servicio de interés (`st.selectbox`), y Mensaje (`st.text_area`).
  - Botón `Enviar mensaje`: Al hacer clic, muestra únicamente un mensaje visual de confirmación simulada (`st.info` o `st.success` indicando que es una demostración visual y mostrando los canales directos de contacto), sin ejecutar lógica de backend ni envío de correos.

---

# 5. Entregables Esperados
1. Código completo y funcional en un único archivo `app.py` listo para ejecutarse con `streamlit run app.py`.
2. Archivo `requirements.txt` con las dependencias mínimas necesarias (`streamlit`, `Pillow`).
3. Breve instrucción sobre los nombres de archivo esperados dentro de `./resources/static/` (ej. `logo.png`, `inicio.jpg`, `quienes_somos.jpg`, `servicio_residuos.jpg`, etc.) para que el usuario solo tenga que renombrar o mapear sus imágenes existentes.