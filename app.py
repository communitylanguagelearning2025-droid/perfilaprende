import streamlit as st

# Configuración inicial de la página
st.set_page_config(
    page_title="PerfilAprende - SENA DUA",
    page_icon="🧠",
    layout="wide"
)

# Estilos visuales avanzados y accesibles
st.markdown("""
    <style>
    .stApp {
        background-color: #F8FAFC;
    }
    .main-title {
        color: #1E3A8A;
        font-family: 'Lexend', sans-serif;
        text-align: center;
        font-weight: 700;
        padding-bottom: 5px;
    }
    .sub-title {
        color: #0284C7;
        text-align: center;
        font-size: 1.1rem;
        margin-bottom: 30px;
    }
    .card-welcome {
        background: linear-gradient(135deg, #E0F2FE 0%, #BAE6FD 100%);
        padding: 24px;
        border-radius: 16px;
        border-left: 8px solid #0284C7;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .card-diagnostic {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 16px;
        border: 2px solid #E2E8F0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }
    .card-challenge {
        background-color: #FEF3C7;
        padding: 24px;
        border-radius: 16px;
        border-left: 8px solid #D97706;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }
    .card-neuro {
        background-color: #F3E8FF;
        padding: 24px;
        border-radius: 16px;
        border-left: 8px solid #9333EA;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }
    .card-nomina {
        background-color: #ECFDF5;
        padding: 24px;
        border-radius: 16px;
        border-left: 8px solid #059669;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }
    .card-docente {
        background-color: #FFF1F2;
        padding: 24px;
        border-radius: 16px;
        border-left: 8px solid #E11D48;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# MENÚ LATERAL: SELECCIÓN DE ROL
# -------------------------------------------------------------
st.sidebar.markdown("### ⚙️ Panel de Navegación")
rol = st.sidebar.selectbox("Seleccione el Rol de Usuario:", ("👨‍🎓 Vista de Aprendiz", "👩‍🏫 Vista de Instructor (Docente)"))

# Encabezado principal
st.markdown("<h1 class='main-title'>🎓 PerfilAprende</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Entorno Inteligente de Aprendizaje Inclusivo | Guía GFPI-F-135</p>", unsafe_allow_html=True)


# =============================================================
# VISTA 1: APRENDIZ
# =============================================================
if rol == "👨‍🎓 Vista de Aprendiz":
    st.markdown("""
    <div class='card-welcome'>
        <h3>✨ ¡Bienvenido(a) al espacio de formación activa!</h3>
        <p>Este sistema integrado evalúa tus decisiones técnicas en Gestión del Talento Humano adaptándose a tu estilo de aprendizaje bajo los principios del <b>Diseño Universal para el Aprendizaje (DUA)</b>.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        nombre = st.text_input("👤 Nombre completo o preferido del Aprendiz:")
    with col2:
        ficha = st.text_input("🏷️ Número de Ficha SENA:")

    if nombre and ficha:
        st.success(f"¡Excelente, **{nombre}**! Perfil vinculado a la ficha **{ficha}** correctamente.")
        st.divider()
        
        # Guardar en session_state para el panel docente
        st.session_state['nombre_aprendiz'] = nombre
        st.session_state['ficha_aprendiz'] = ficha

        # FASE 1: DIAGNÓSTICO
        st.markdown("""
        <div class='card-diagnostic'>
            <h3>🧩 Fase 1: Diagnóstico de Preferencias y Accesibilidad DUA</h3>
            <p>Personaliza tu experiencia de aprendizaje seleccionando cómo deseas interactuar con los contenidos:</p>
        </div>
        """, unsafe_allow_html=True)

        with st.form("form_diagnostico"):
            p1 = st.radio(
                "📖 1. ¿Cómo prefieres visualizar los textos densos y casos de estudio?",
                ("Texto completo tradicional", "Párrafos cortos fragmentados con viñetas clave", "Apoyo visual con esquemas y resúmenes gráficos")
            )
            p2 = st.radio(
                "⏱️ 2. ¿Cuál es tu ritmo ideal durante las simulaciones técnicas?",
                ("Sesiones continuas sin interrupciones", "Pausas breves y estructuradas entre cada caso", "Bloques dinámicos con retroalimentación inmediata")
            )
            p3 = st.radio(
                "📊 3. Al analizar datos cuantitativos o tablas de idoneidad, prefieres:",
                ("Tablas numéricas detalladas", "Gráficos visuales y códigos de color", "Explicación guiada paso a paso")
            )
            
            submitted = st.form_submit_button("Guardar Preferencias y Cargar Módulos 🚀")
            
            if submitted:
                st.session_state['configurado'] = True
                st.session_state['preferencias'] = {"lectura": p1, "ritmo": p2, "datos": p3}

        if st.session_state.get('configurado', False):
            st.success("🎉 **¡Andamios DUA configurados con éxito!** Se han aplicado los ajustes visuales a tu sesión.")
            st.divider()
            
            # MÓDULO 2: PROFESIOGRAMAS
            st.markdown("""
            <div class='card-challenge'>
                <h3>🎯 Módulo 2: Micro-desafío - Validación de Profesiogramas</h3>
                <p><b>Caso de Estudio:</b> Una empresa del sector industrial requiere contratar un <i>Coordinador de Logística</i>. Analiza los componentes clave del profesiograma según la Unidad 1.</p>
            </div>
            """, unsafe_allow_html=True)

            with st.form("form_profesiograma"):
                decision = st.radio(
                    "¿Cuál es el propósito principal de incluir competencias comportamentales específicas y exigencias físicas en el profesiograma?",
                    (
                        "A) Rellenar formato institucional exigido por el SENA sin mayor impacto operativo.",
                        "B) Garantizar el ajuste técnico y la seguridad del candidato al perfil del cargo, previniendo riesgos laborales.",
                        "C) Servir únicamente como referencia decorativa para el archivo general de recursos humanos."
                    )
                )
                enviar_reto = st.form_submit_button("Validar Decisión Técnica 🔍")
                
                if enviar_reto:
                    if "B) Garantizar el ajuste técnico" in decision:
                        st.success("✅ **¡Respuesta Correcta y Rigurosa!** Has comprendido el valor del profesiograma como herramienta de mitigación de riesgos.")
                    else:
                        st.error("❌ **Validación Estricta:** Incorrecto. El profesiograma asegura la idoneidad técnica y la seguridad del trabajador.")

            st.divider()

            # MÓDULO 3: CRIBADO NEUROPSICOPEDAGÓGICO (Transparente para el aprendiz)
            st.markdown("""
            <div class='card-neuro'>
                <h3>🧠 Módulo 3: Actividad de Procesamiento y Secuenciación Técnica</h3>
                <p><b>Ejercicio de Interacción:</b> Por favor, responde las siguientes situaciones sobre tus preferencias al ejecutar instrucciones complejas.</p>
            </div>
            """, unsafe_allow_html=True)

            with st.form("form_cribado"):
                c1 = st.radio(
                    "1. Al enfrentarte a un procedimiento técnico de varios pasos (ej. filtrado de hojas de vida con varios criterios), experimentas:",
                    (
                        "A) Facilidad para retener, secuenciar y ejecutar cada instrucción sin problemas.",
                        "B) Saturación o bloqueo temporal si las instrucciones son extensas, requiriendo fragmentación visual o pausas.",
                        "C) Imposibilidad total para seguir el hilo lógico de la tarea, perdiendo el foco de manera recurrente."
                    )
                )

                c2 = st.radio(
                    "2. Al procesar textos técnicos o normativos extensos (como la Guía GFPI-F-135), notas que:",
                    (
                        "A) Comprendes la lectura de corrido al primer intento.",
                        "B) Requieres apoyo de mapas conceptuales, lectura en voz alta o resaltado de colores para no perder la decodificación.",
                        "C) Confundes palabras, omites líneas o experimentas fatiga visual severa al intentar leer bloques seguidos."
                    )
                )

                enviar_cribado = st.form_submit_button("Guardar Respuestas de Procesamiento ⚙️")

                if enviar_cribado:
                    st.session_state['cribado_c1'] = c1
                    st.session_state['cribado_c2'] = c2
                    st.success("📊 **¡Respuestas guardadas con éxito!** El entorno ha ajustado los apoyos de accesibilidad para optimizar tu experiencia.")

            st.divider()

            # MÓDULO 4: EVALUACIÓN DE DESEMPEÑO Y NÓMINA
            st.markdown("""
            <div class='card-nomina'>
                <h3>💰 Módulo 4: Estudio de Caso - Evaluación de Desempeño y Efectos en Nómina</h3>
                <p><b>Caso Práctico:</b> Un operario de planta obtiene una calificación insatisfactoria en su evaluación de desempeño por incumplimiento reiterado de metas de productividad. Como analista de Talento Humano, debes determinar el curso de acción legal y operativo correcto.</p>
            </div>
            """, unsafe_allow_html=True)

            with st.form("form_nomina"):
                caso_resp = st.radio(
                    "¿Cuál es el procedimiento técnico y normativo adecuado que debe seguir el área de Talento Humano ante este resultado?",
                    (
                        "A) Descontar inmediatamente el 50% del salario básico en la siguiente nómina como medida sancionatoria.",
                        "B) Iniciar un plan de mejora concertado, documentando el proceso formativo antes de tomar decisiones sobre la vinculación o novedades salariales.",
                        "C) Omitir la evaluación y otorgar la prima de servicios y bonificaciones completas para evitar conflictos laborales."
                    )
                )

                enviar_nomina = st.form_submit_button("Validar Decisión de Nómina y Desempeño 📋")

                if enviar_nomina:
                    if "B) Iniciar un plan de mejora concertado" in caso_resp:
                        st.balloons()
                        st.success("✅ **¡Excelente Análisis Técnico!** Has aplicado correctamente el debido proceso y la relación entre la evaluación de desempeño y la administración de personal.")
                    else:
                        st.error("❌ **Validación Estricta (Cero Complacencia):** Incorrecto. Las deducciones salariales arbitrarias o la omisión de planes de mejora violan el marco normativo laboral.")


# =============================================================
# VISTA 2: INSTRUCTOR / DOCENTE (PRIVADA)
# =============================================================
elif rol == "👩‍🏫 Vista de Instructor (Docente)":
    st.markdown("""
    <div class='card-docente'>
        <h3>🔒 Panel de Analíticas y Reporte Confidencial del Instructor</h3>
        <p><b>Área Restringida:</b> Visualización técnica de barreras cognitivas detectadas y apoyos DUA requeridos por el aprendiz durante la sesión.</p>
    </div>
    """, unsafe_allow_html=True)

    # Contraseña sencilla de seguridad para el docente
    password = st.text_input("🔑 Ingrese la contraseña de acceso docente:", type="password")

    if password == "sena2026":
        st.success("✅ Acceso autorizado al panel de seguimiento.")
        st.divider()

        if 'nombre_aprendiz' in st.session_state and 'cribado_c1' in st.session_state:
            nom = st.session_state['nombre_aprendiz']
            fic = st.session_state['ficha_aprendiz']
            res_c1 = st.session_state['cribado_c1']
            res_c2 = st.session_state['cribado_c2']

            st.write(f"### 📋 Reporte del Aprendiz: {nom} (Ficha: {fic})")

            if "C)" in res_c1 or "C)" in res_c2:
                st.error("🚨 **Estado de Alerta:** El aprendiz presenta indicios de barreras significativas en memoria de trabajo o decodificación.")
                st.markdown("""
                * **Recomendaciones pedagógicas y andamios requeridos:**
                  * Activar tipografías accesibles (Lexend / OpenDyslexic).
                  * Fragmentación radical de contenidos en micro-pasos guiados.
                  * Inclusión de soporte auditivo (Text-to-Speech).
                """)
            elif "B)" in res_c1 or "B)" in res_c2:
                st.warning("⚠️ **Estado Moderado:** El aprendiz requiere apoyos estructurados de ritmo y visualización.")
                st.markdown("""
                * **Recomendaciones pedagógicas y andamios requeridos:**
                  * Establecer pausas estructuradas entre casos prácticos.
                  * Uso complementario de organizadores gráficos y resúmenes visuales.
                """)
            else:
                st.success("🌟 **Estado Estándar:** El aprendiz procesa la información de manera fluida.")
                st.markdown("""
                * **Recomendaciones pedagógicas y andamios requeridos:**
                  * Mantener itinerarios de profundización técnica estándar.
                """)
        else:
            st.info("ℹ️ Aún no hay registros de cribado guardados. El aprendiz debe completar el Módulo 3 en su vista correspondiente para generar este reporte.")
    elif password:
        st.error("❌ Contraseña incorrecta. Intente de nuevo (clave por defecto: sena2026).")
    else:
        st.info("ℹ️ Por favor, ingrese la contraseña de instructor para visualizar las analíticas.")