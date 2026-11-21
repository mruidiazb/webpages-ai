"""
Gestiones Ambientales del Caribe SAS (GAC SAS) - Plataforma Web Corporativa
Desarrollado con Streamlit y Python siguiendo estándares de diseño UI/UX ambiental.
"""

from pathlib import Path
from typing import Optional
import streamlit as st
from PIL import Image

# -----------------------------------------------------------------------------
# 1. Configuración de la Página
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="GAC SAS | Gestiones Ambientales del Caribe",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------------------------------
# 2. Rutas y Gestión de Activos
# -----------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "resources" / "static"


def load_image(file_name: str) -> Optional[Image.Image]:
    """
    Carga de forma segura una imagen desde el directorio de recursos estáticos.
    Retorna un objeto PIL Image si existe, o None con fallback controlado.
    """
    file_path = STATIC_DIR / file_name
    if file_path.is_file():
        try:
            return Image.open(file_path)
        except Exception as err:
            st.warning(f"No se pudo cargar la imagen {file_name}: {err}")
            return None
    return None


def render_image_or_placeholder(file_name: str, caption: str = "", use_column_width: bool = True):
    """
    Muestra una imagen si está disponible, o un contenedor de respaldo estilizado.
    """
    img = load_image(file_name)
    if img:
        st.image(img, caption=caption if caption else None, use_container_width=use_column_width)
    else:
        st.markdown(
            f"""
            <div class="gac-placeholder">
                <div style="font-size: 2.2rem; margin-bottom: 0.5rem;">🌱</div>
                <div style="font-weight: 600; color: #2D6A4F;">Recurso Visual: {file_name}</div>
                <div style="font-size: 0.85rem; color: #64748B;">{caption or 'Gestiones Ambientales del Caribe SAS'}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# -----------------------------------------------------------------------------
# 3. Inyección de Estilos CSS Personalizados (Diseño UI/UX Ambiental y Compacto)
# -----------------------------------------------------------------------------
CUSTOM_CSS = """
<style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        color: #1E293B;
    }

    /* Fondo principal y espaciado compacto */
    .stApp {
        background-color: #F8FAF9;
    }
    
    .block-container {
        padding-top: 1.8rem !important;
        padding-bottom: 2rem !important;
        max-width: 1200px;
    }

    /* Ocultar barra superior por defecto si se desea */
    header[data-testid="stHeader"] {
        background-color: rgba(248, 250, 249, 0.85);
        backdrop-filter: blur(8px);
    }

    /* Estilos del Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #FFFFFF 0%, #F1F7F4 100%);
        border-right: 1px solid #E2E8F0;
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 1.5rem !important;
    }

    /* Tarjetas y Contenedores */
    .gac-card {
        background: #FFFFFF;
        border-radius: 14px;
        padding: 1.25rem 1.5rem;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 14px -2px rgba(27, 67, 50, 0.05);
        margin-bottom: 1rem;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .gac-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px -2px rgba(27, 67, 50, 0.1);
        border-color: #52B788;
    }

    .gac-card-highlight {
        background: linear-gradient(135deg, #FFFFFF 0%, #F3FAF6 100%);
        border-left: 4px solid #2D6A4F;
    }

    /* Badges / Etiquetas */
    .gac-badge {
        display: inline-block;
        background-color: #D8F3DC;
        color: #1B4332;
        font-size: 0.78rem;
        font-weight: 700;
        padding: 0.28rem 0.75rem;
        border-radius: 9999px;
        letter-spacing: 0.04em;
        text-transform: uppercase;
        margin-bottom: 0.75rem;
        border: 1px solid #B7E4C7;
    }

    /* Encabezados */
    .gac-title {
        color: #1B4332;
        font-weight: 800;
        font-size: 2.1rem;
        line-height: 1.2;
        margin-bottom: 0.4rem;
        letter-spacing: -0.02em;
    }

    .gac-subtitle {
        color: #2D6A4F;
        font-size: 1.15rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    /* Texto descriptivo */
    .gac-text {
        color: #334155;
        font-size: 0.98rem;
        line-height: 1.6;
        margin-bottom: 0.85rem;
    }

    /* Tarjetas de mini-valores */
    .gac-val-box {
        background: #FFFFFF;
        border-radius: 12px;
        padding: 1rem;
        border: 1px solid #E2E8F0;
        height: 100%;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }
    .gac-val-title {
        color: #1B4332;
        font-weight: 700;
        font-size: 0.95rem;
        margin-bottom: 0.35rem;
        display: flex;
        align-items: center;
        gap: 0.4rem;
    }
    .gac-val-desc {
        color: #475569;
        font-size: 0.84rem;
        line-height: 1.45;
    }

    /* Fases de trabajo */
    .gac-step-num {
        font-size: 1.8rem;
        font-weight: 800;
        color: #52B788;
        line-height: 1;
        margin-bottom: 0.35rem;
    }
    .gac-step-title {
        color: #1B4332;
        font-weight: 700;
        font-size: 1.05rem;
        margin-bottom: 0.4rem;
    }

    /* Banner informativo */
    .gac-banner {
        background: linear-gradient(90deg, #1B4332 0%, #2D6A4F 100%);
        color: #FFFFFF;
        padding: 1rem 1.4rem;
        border-radius: 12px;
        margin-top: 1.2rem;
        display: flex;
        align-items: center;
        gap: 0.8rem;
        box-shadow: 0 4px 12px rgba(27, 67, 50, 0.15);
    }

    /* Placeholder visual para imágenes faltantes */
    .gac-placeholder {
        background: #F1F5F9;
        border: 2px dashed #CBD5E1;
        border-radius: 12px;
        padding: 2.5rem 1.5rem;
        text-align: center;
        margin-bottom: 1rem;
    }

    /* Estilo de botones en Streamlit */
    div.stButton > button {
        background-color: #2D6A4F !important;
        color: #FFFFFF !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 0.5rem 1.2rem !important;
        box-shadow: 0 2px 6px rgba(45, 106, 79, 0.2) !important;
        transition: all 0.2s ease !important;
    }
    div.stButton > button:hover {
        background-color: #1B4332 !important;
        box-shadow: 0 4px 12px rgba(27, 67, 50, 0.3) !important;
        transform: translateY(-1px);
    }

    /* Estilos del sidebar radio */
    div[data-testid="stSidebar"] div[role="radiogroup"] > label {
        padding: 0.55rem 0.9rem;
        border-radius: 8px;
        margin-bottom: 0.25rem;
        transition: background-color 0.15s ease;
    }
    div[data-testid="stSidebar"] div[role="radiogroup"] > label:hover {
        background-color: #E8F5E9;
    }
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 4. Manejo de Estado de Navegación
# -----------------------------------------------------------------------------
MENU_ITEMS = [
    "Inicio",
    "Quiénes Somos",
    "Servicios",
    "Cómo Trabajamos",
    "Contáctenos",
]

if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Inicio"
if "nav_radio" not in st.session_state:
    st.session_state["nav_radio"] = st.session_state["current_page"]


def on_nav_change():
    """Sincroniza la página activa al interactuar con el menú de radio del sidebar."""
    st.session_state["current_page"] = st.session_state["nav_radio"]


def set_page(page_name: str):
    """Callback seguro ejecutado antes del ciclo de renderizado de Streamlit."""
    st.session_state["current_page"] = page_name
    st.session_state["nav_radio"] = page_name


def navigate_to(page_name: str):
    """Permite cambiar de vista programáticamente si se requiere fuera de callbacks."""
    set_page(page_name)
    st.rerun()


# -----------------------------------------------------------------------------
# 5. Renderizado del Sidebar
# -----------------------------------------------------------------------------
with st.sidebar:
    # Logotipo
    logo_img = load_image("logo.png")
    if logo_img:
        st.image(logo_img, use_container_width=True)
    else:
        st.markdown(
            """
            <div style="text-align: center; padding: 1rem 0;">
                <div style="font-size: 2.4rem;">🌿</div>
                <div style="font-weight: 800; font-size: 1.15rem; color: #1B4332;">GAC SAS</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 1.2rem;">
            <div style="font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.08em; color: #2D6A4F; font-weight: 700;">
                Gestiones Ambientales del Caribe SAS
            </div>
            <div style="font-size: 0.75rem; color: #64748B; margin-top: 2px;">
                NIT & Soluciones Ambientales
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<hr style='margin: 0.5rem 0 1rem 0; border: none; border-top: 1px solid #E2E8F0;' />", unsafe_allow_html=True)

    # Sincronización previa del radio antes de su instanciación
    if st.session_state.get("nav_radio") != st.session_state.get("current_page"):
        st.session_state["nav_radio"] = st.session_state.get("current_page", "Inicio")

    # Menú de selección con sincronización bidireccional inmediata
    st.radio(
        label="Navegación Principal",
        options=MENU_ITEMS,
        key="nav_radio",
        on_change=on_nav_change,
        label_visibility="collapsed",
    )

    st.markdown("<hr style='margin: 1.5rem 0 1rem 0; border: none; border-top: 1px solid #E2E8F0;' />", unsafe_allow_html=True)

    # Footer Institucional en Sidebar
    st.markdown(
        """
        <div style="font-size: 0.8rem; color: #64748B; text-align: center; line-height: 1.5;">
            📍 <strong>Barranquilla y Costa Caribe</strong><br/>
            🌱 <em>Operando con rigor ambiental desde 2021</em>
        </div>
        """,
        unsafe_allow_html=True,
    )


# -----------------------------------------------------------------------------
# 6. Vistas y Secciones de la Aplicación
# -----------------------------------------------------------------------------

def view_inicio():
    """Vista de Inicio: Hero corporativo y resumen de propuesta de valor."""
    col_text, col_img = st.columns([1.15, 0.85], gap="large")

    with col_text:
        st.markdown('<div class="gac-badge">Costa Caribe • Eficiencia y Cumplimiento</div>', unsafe_allow_html=True)
        st.markdown('<h1 class="gac-title">Gestiones Ambientales del Caribe SAS</h1>', unsafe_allow_html=True)
        st.markdown('<div class="gac-subtitle">Tratamiento de residuos sólidos no peligrosos</div>', unsafe_allow_html=True)

        st.markdown(
            """
            <div class="gac-text">
                Clasificamos y tratamos los materiales según cada operación. Al revisar sus volúmenes y costos actuales, podemos identificar oportunidades de aprovechamiento y evaluar posibles ahorros, sin asumir que todas las empresas obtendrán el mismo resultado.
            </div>
            <div class="gac-text" style="font-weight: 500; color: #1E293B;">
                Un manejo más organizado permite estudiar el aprovechamiento de materiales y el costo de gestionarlos con precisión y apego normativo.
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<div style='height: 0.6rem;'></div>", unsafe_allow_html=True)

        btn_col1, btn_col2 = st.columns([1, 1])
        with btn_col1:
            st.button(
                "Explorar Servicios ➔",
                key="btn_hero_explorar_servicios",
                use_container_width=True,
                on_click=set_page,
                args=("Servicios",),
            )
        with btn_col2:
            st.button(
                "Contactar Asesor ✉",
                key="btn_hero_contactar_asesor",
                use_container_width=True,
                on_click=set_page,
                args=("Contáctenos",),
            )

    with col_img:
        render_image_or_placeholder("01-Inicio.png", caption="Operación de gestión y valorización de residuos en planta.")

    st.markdown("<div style='height: 1.2rem;'></div>", unsafe_allow_html=True)

    # Barra compacta con indicadores destacados
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown(
            """
            <div class="gac-val-box">
                <div class="gac-val-title">🏢 Enfoque Industrial</div>
                <div class="gac-val-desc">Adaptado a los flujos reales de producción y logística en Barranquilla y la región Caribe.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with m2:
        st.markdown(
            """
            <div class="gac-val-box">
                <div class="gac-val-title">♻️ Economía Circular</div>
                <div class="gac-val-desc">Maximización del aprovechamiento de materiales no peligrosos reduciendo disposición final.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with m3:
        st.markdown(
            """
            <div class="gac-val-box">
                <div class="gac-val-title">📋 Soporte Documental</div>
                <div class="gac-val-desc">Certificación y registro claro de corrientes y pesajes para auditorías ambientales.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def view_quienes_somos():
    """Vista Quiénes Somos: Identidad institucional, experiencia y pilares."""
    st.markdown('<div class="gac-badge">Nuestra Organización • Desde 2021</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="gac-title">Quiénes Somos</h2>', unsafe_allow_html=True)
    st.markdown('<div class="gac-subtitle">Tratamiento de residuos sólidos no peligrosos / Desde 2021</div>', unsafe_allow_html=True)

    col_info, col_pic = st.columns([1.1, 0.9], gap="large")

    with col_info:
        st.markdown(
            """
            <div class="gac-card gac-card-highlight">
                <p class="gac-text" style="font-size: 1.02rem; margin-bottom: 0.75rem;">
                    <strong>GAC Gestiones Ambientales del Caribe SAS</strong> trabaja con empresas de Barranquilla y la Costa Caribe que generan grandes cantidades de residuos sólidos no peligrosos y buscan organizar su manejo integral.
                </p>
                <p class="gac-text" style="margin-bottom: 0;">
                    Clasificamos y tratamos los materiales según cada operación. Al revisar sus volúmenes y costos actuales, podemos identificar oportunidades de aprovechamiento y evaluar posibles ahorros, sin asumir que todas las empresas obtendrán el mismo resultado.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div style="margin-top: 0.8rem;">
                <div class="gac-text">
                    Nuestra trayectoria se fundamenta en un entendimiento directo de la dinámica productiva regional. No creemos en soluciones estandarizadas: cada diagnóstico se levanta en campo, respetando los tiempos de producción y el espacio de nuestros aliados.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_pic:
        render_image_or_placeholder("02-inicio.webp", caption="Equipo técnico y operativo GAC SAS en campo.")

    st.markdown("<div style='height: 0.5rem;'></div>", unsafe_allow_html=True)

    # 3 Valores diferenciales
    v1, v2, v3 = st.columns(3)
    with v1:
        st.markdown(
            """
            <div class="gac-card">
                <div class="gac-val-title">🎯 Enfoque a la Medida</div>
                <div class="gac-val-desc">El alcance se diseña según los tipos de residuos y el ritmo de trabajo real, sin imponer esquemas forzados.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with v2:
        st.markdown(
            """
            <div class="gac-card">
                <div class="gac-val-title">📊 Trazabilidad Operativa</div>
                <div class="gac-val-desc">Control pormenorizado de pesajes y reportes de clasificación que respaldan la toma de decisiones contables y ambientales.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with v3:
        st.markdown(
            """
            <div class="gac-card">
                <div class="gac-val-title">🌊 Cobertura Costa Caribe</div>
                <div class="gac-val-desc">Base operativa en Barranquilla con capacidad de respuesta logística en los principales corredores industriales.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div style='height: 0.8rem;'></div>", unsafe_allow_html=True)
    c_btn1, c_btn2 = st.columns([1, 1])
    with c_btn1:
        st.button(
            "Ver Portafolio de Servicios ➔",
            key="btn_qs_servicios",
            use_container_width=True,
            on_click=set_page,
            args=("Servicios",),
        )
    with c_btn2:
        st.button(
            "Contactar al Equipo GAC ✉",
            key="btn_qs_contacto",
            use_container_width=True,
            on_click=set_page,
            args=("Contáctenos",),
        )


def view_servicios():
    """Vista de Servicios: 3 líneas de servicio presentadas de forma compacta y visual."""
    st.markdown('<div class="gac-badge">Portafolio Integral</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="gac-title">Nuestros Servicios</h2>', unsafe_allow_html=True)
    st.markdown(
        '<div class="gac-subtitle">Soluciones operativas orientadas al orden, la sostenibilidad y la eficiencia</div>',
        unsafe_allow_html=True,
    )

    tab_residuos, tab_jardineria, tab_obras = st.tabs([
        "♻️ Gestión de Residuos",
        "🌿 Jardinería y Zonas Verdes",
        "🏗️ Obras Civiles y Adecuaciones",
    ])

    with tab_residuos:
        c1, c2 = st.columns([1.1, 0.9], gap="medium")
        with c1:
            st.markdown(
                """
                <div class="gac-card">
                    <h3 style="color: #1B4332; margin-top: 0; font-weight: 700;">Gestión de Residuos Sólidos No Peligrosos</h3>
                    <p class="gac-text">
                        Identificamos las corrientes de residuos, los volúmenes y los costos actuales de manejo. Con esa información definimos dónde conviene intervenir para organizar la separación según los materiales y el ritmo de trabajo de la empresa.
                    </p>
                    <div style="background-color: #F3FAF6; border-left: 3px solid #2D6A4F; padding: 0.8rem 1rem; border-radius: 6px; margin-top: 0.8rem;">
                        <strong style="color: #1B4332; font-size: 0.9rem;">📌 Valor Agregado Incluido:</strong>
                        <div style="color: #334155; font-size: 0.85rem; margin-top: 0.25rem;">
                            <strong>Diagnóstico inicial y trazabilidad:</strong> Entrega de informes periódicos de volúmenes clasificados y soporte documental estructurado para auditorías y gestión ambiental interna.
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with c2:
            render_image_or_placeholder("03-residuos.png", caption="Clasificación y acopio organizado de materiales no peligrosos.")

    with tab_jardineria:
        c1, c2 = st.columns([1.1, 0.9], gap="medium")
        with c1:
            st.markdown(
                """
                <div class="gac-card">
                    <h3 style="color: #1B4332; margin-top: 0; font-weight: 700;">Jardinería y Zonas Verdes</h3>
                    <p class="gac-text">
                        Realizamos labores de jardinería y mantenimiento de áreas verdes empresariales. Revisamos las condiciones del terreno y la vegetación para acordar las tareas y la frecuencia que necesita el espacio.
                    </p>
                    <div style="background-color: #F3FAF6; border-left: 3px solid #2D6A4F; padding: 0.8rem 1rem; border-radius: 6px; margin-top: 0.8rem;">
                        <strong style="color: #1B4332; font-size: 0.9rem;">📌 Valor Agregado Incluido:</strong>
                        <div style="color: #334155; font-size: 0.85rem; margin-top: 0.25rem;">
                            <strong>Planes preventivos y compostaje:</strong> Cronogramas ajustados a la estacionalidad del Caribe y aprovechamiento responsable del material vegetal resultante de podas para bio-abonos.
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with c2:
            # Prueba primero imagen principal de jardineria
            render_image_or_placeholder("03-Jardineria.webp", caption="Mantenimiento paisajístico y conservación de zonas verdes corporativas.")

    with tab_obras:
        c1, c2 = st.columns([1.1, 0.9], gap="medium")
        with c1:
            st.markdown(
                """
                <div class="gac-card">
                    <h3 style="color: #1B4332; margin-top: 0; font-weight: 700;">Obras Civiles y Adecuaciones</h3>
                    <p class="gac-text">
                        Atendemos necesidades de adecuación y mantenimiento vinculadas a las instalaciones y de acuerdo al espacio disponible en su sede.
                    </p>
                    <div style="background-color: #F3FAF6; border-left: 3px solid #2D6A4F; padding: 0.8rem 1rem; border-radius: 6px; margin-top: 0.8rem;">
                        <strong style="color: #1B4332; font-size: 0.9rem;">📌 Valor Agregado Incluido:</strong>
                        <div style="color: #334155; font-size: 0.85rem; margin-top: 0.25rem;">
                            <strong>Adecuación de puntos ecológicos y centros de acopio:</strong> Construcción y optimización de cuartos de almacenamiento temporal con señalización, control de lixiviados y normatividad industrial.
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with c2:
            render_image_or_placeholder("02-servicios.webp", caption="Infraestructura y adecuaciones físicas para el manejo seguro de residuos.")

    st.markdown("<div style='height: 0.8rem;'></div>", unsafe_allow_html=True)
    c_sbtn1, c_sbtn2 = st.columns([1, 1])
    with c_sbtn1:
        st.button(
            "Conocer Nuestra Metodología de Trabajo ➔",
            key="btn_serv_como_trabajamos",
            use_container_width=True,
            on_click=set_page,
            args=("Cómo Trabajamos",),
        )
    with c_sbtn2:
        st.button(
            "Solicitar Diagnóstico para su Empresa ✉",
            key="btn_serv_contacto",
            use_container_width=True,
            on_click=set_page,
            args=("Contáctenos",),
        )


def view_como_trabajamos():
    """Vista Cómo Trabajamos: Metodología secuencial de 4 fases y banner de personalización."""
    st.markdown('<div class="gac-badge">Metodología Clara y Transparente</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="gac-title">Cómo Trabajamos</h2>', unsafe_allow_html=True)
    st.markdown(
        '<div class="gac-subtitle">Un proceso estructurado en 4 fases para garantizar resultados sostenibles</div>',
        unsafe_allow_html=True,
    )

    fase1, fase2 = st.columns(2, gap="medium")
    with fase1:
        st.markdown(
            """
            <div class="gac-card" style="height: 100%;">
                <div class="gac-step-num">01</div>
                <div class="gac-step-title">Entendemos la operación</div>
                <p class="gac-text">
                    Conversamos sobre lo que la empresa genera, cómo se mueve dentro de sus instalaciones y cuánto cuesta gestionarlo hoy. El alcance se diseña según los tipos de residuos, los volúmenes y la operación específica de cada cliente; no se traslada el mismo esquema de una empresa a otra.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with fase2:
        st.markdown(
            """
            <div class="gac-card" style="height: 100%;">
                <div class="gac-step-num">02</div>
                <div class="gac-step-title">Revisamos lo que se genera</div>
                <p class="gac-text">
                    Conversamos sobre la operación, identificamos las corrientes de residuos sólidos no peligrosos y revisamos volúmenes y costos actuales. Esa información permite reconocer con exactitud dónde conviene intervenir.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div style='height: 0.5rem;'></div>", unsafe_allow_html=True)

    fase3, fase4 = st.columns(2, gap="medium")
    with fase3:
        st.markdown(
            """
            <div class="gac-card" style="height: 100%;">
                <div class="gac-step-num">03</div>
                <div class="gac-step-title">Organizamos la clasificación</div>
                <p class="gac-text">
                    Definimos un manejo ajustado a los materiales y al ritmo de trabajo de la empresa. Una separación más clara facilita el tratamiento y permite identificar oportunidades de aprovechamiento viables técnica y financieramente.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with fase4:
        st.markdown(
            """
            <div class="gac-card" style="height: 100%;">
                <div class="gac-step-num">04</div>
                <div class="gac-step-title">Evaluamos el resultado real</div>
                <p class="gac-text">
                    Contrastamos las opciones de manejo con los costos de la organización. El posible ahorro se estudia caso por caso: depende de la información suministrada, los residuos y la operación de cada cliente.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Banner de Principio de Personalización GAC
    st.markdown(
        """
        <div class="gac-banner">
            <div style="font-size: 1.8rem;">💡</div>
            <div>
                <strong style="font-size: 1rem; letter-spacing: 0.02em;">Principio de Personalización GAC:</strong>
                <div style="font-size: 0.9rem; opacity: 0.95; margin-top: 2px;">
                    Cada diagnóstico parte de datos reales de su operación, evitando recetas genéricas y asegurando viabilidad económica y ambiental.
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height: 0.8rem;'></div>", unsafe_allow_html=True)
    st.button(
        "Conversemos sobre la operación de su empresa ✉",
        key="btn_como_contacto",
        use_container_width=True,
        on_click=set_page,
        args=("Contáctenos",),
    )


def view_contactenos():
    """Vista Contáctenos: Canales directos y formulario de solicitud de contacto."""
    st.markdown('<div class="gac-badge">Canales Oficiales</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="gac-title">Contáctenos</h2>', unsafe_allow_html=True)
    st.markdown(
        '<div class="gac-subtitle">Conversemos sobre las necesidades ambientales y operativas de su empresa</div>',
        unsafe_allow_html=True,
    )

    col_direct, col_form = st.columns([1, 1.1], gap="large")

    with col_direct:
        st.markdown(
            """
            <div class="gac-card gac-card-highlight">
                <h4 style="color: #1B4332; margin-top: 0; font-size: 1.15rem; font-weight: 700;">
                    Gestiones Ambientales del Caribe SAS (GAC SAS)
                </h4>
                <div style="margin-top: 1rem;">
                    <div style="margin-bottom: 0.85rem;">
                        <span style="font-size: 1.2rem; margin-right: 0.4rem;">📞</span>
                        <strong>Teléfono / WhatsApp:</strong><br/>
                        <a href="tel:+573016226317" style="color: #2D6A4F; font-weight: 600; text-decoration: none; margin-left: 1.8rem;">
                            +57 301 622 6317
                        </a>
                    </div>
                    <div style="margin-bottom: 0.85rem;">
                        <span style="font-size: 1.2rem; margin-right: 0.4rem;">✉️</span>
                        <strong>Correo Electrónico:</strong><br/>
                        <a href="mailto:gac-sas@miempresa.co" style="color: #2D6A4F; font-weight: 600; text-decoration: none; margin-left: 1.8rem;">
                            gac-sas@miempresa.co
                        </a>
                    </div>
                    <div style="margin-bottom: 0.5rem;">
                        <span style="font-size: 1.2rem; margin-right: 0.4rem;">📍</span>
                        <strong>Ubicación y Cobertura:</strong><br/>
                        <span style="color: #475569; margin-left: 1.8rem; font-size: 0.92rem;">
                            Barranquilla, Atlántico • Atención a toda la Costa Caribe
                        </span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        render_image_or_placeholder("contactanos.webp", caption="Atención personalizada para el sector productivo e industrial.")

    with col_form:
        st.markdown(
            """
            <div style="background: #FFFFFF; border-radius: 14px; padding: 1.4rem; border: 1px solid #E2E8F0; box-shadow: 0 4px 14px -2px rgba(27, 67, 50, 0.05);">
                <div style="font-weight: 700; color: #1B4332; font-size: 1.1rem; margin-bottom: 0.3rem;">
                    Formulario de Contacto Corporativo
                </div>
                <div style="font-size: 0.82rem; color: #64748B; margin-bottom: 1rem;">
                    Complete los siguientes campos y nuestro equipo técnico se pondrá en contacto a la brevedad.
                </div>
            """,
            unsafe_allow_html=True,
        )

        with st.form("contact_form", clear_on_submit=False):
            nombre = st.text_input("Nombre Completo *", placeholder="Ej. Carlos Martínez")
            c_emp, c_tel = st.columns(2)
            with c_emp:
                empresa = st.text_input("Empresa *", placeholder="Ej. Manufacturas del Caribe")
            with c_tel:
                telefono = st.text_input("Teléfono de Contacto *", placeholder="Ej. +57 300 000 0000")

            correo = st.text_input("Correo Electrónico Corporativo *", placeholder="ejemplo@empresa.com")
            
            servicio = st.selectbox(
                "Servicio de Interés Principal",
                [
                    "Gestión de Residuos Sólidos No Peligrosos",
                    "Jardinería y Zonas Verdes",
                    "Obras Civiles y Adecuaciones",
                    "Diagnóstico y Asesoría Integral",
                ],
            )
            
            mensaje = st.text_area(
                "Detalles de la Solicitud / Operación",
                placeholder="Describa brevemente el tipo de residuo, frecuencia o requerimiento...",
                height=95,
            )

            submit_button = st.form_submit_button("Enviar Mensaje ✉", use_container_width=True)

            if submit_button:
                if not nombre.strip() or not correo.strip() or not empresa.strip():
                    st.error("Por favor diligencie los campos obligatorios marcados con asterisco (*).")
                else:
                    st.success(
                        f"¡Gracias, {nombre}! Su solicitud para **{empresa}** ha sido registrada con éxito (Demostración visual). "
                        "Nos comunicaremos mediante el correo provisto o al teléfono de contacto."
                    )
                    st.info("Para contacto directo inmediato, recuerde escribir a **gac-sas@miempresa.co** o al **+57 301 622 6317**.")

        st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 7. Despachador de Vistas
# -----------------------------------------------------------------------------
PAGES = {
    "Inicio": view_inicio,
    "Quiénes Somos": view_quienes_somos,
    "Servicios": view_servicios,
    "Cómo Trabajamos": view_como_trabajamos,
    "Contáctenos": view_contactenos,
}

current_view = PAGES.get(st.session_state["current_page"], view_inicio)
current_view()
