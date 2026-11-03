import streamlit as st

# Configuración visual accesible
st.markdown("""
    <style>
    .stApp {
        background-color: #FDFBF7;
    }
    h1, h2, h3 {
        color: #1E3A8A;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("### 🧠 PerfilAprende: Explorador de Estilos y Apoyos DUA")
st.markdown("Bienvenido/a. Este espacio está diseñado para comprender **cómo aprende mejor tu mente** y sugerir herramientas que faciliten tu proceso formativo en el SENA.")

st.markdown("---")
st.markdown("### 🧩 Formulario de Valoración y Preferencias")

# Datos básicos del aprendiz
col_nom, col_doc = st.columns(2)
with col_nom:
    nombre_aprendiz = st.text_input("Nombre completo del aprendiz:", "Aprendiz SENA")
with col_doc:
    programa_sena = st.text_input("Programa de Formación:", "Gestión del Talento Humano")

banco_preguntas_empaticas = [
    {
        "id": 1,
        "dimension": "Revisión y Detalle",
        "pregunta": "1. Cuando realizas guías o tareas, ¿te resulta útil hacer pausas para revisar detalles que pudiste haber pasado por alto en el primer borrador?",
        "opciones": ["Casi nunca me pasa", "A veces me sucede", "Me describe totalmente"],
        "puntaje": [0, 1, 2]
    },
    {
        "id": 2,
        "dimension": "Ritmo de Atención",
        "pregunta": "2. Al escuchar explicaciones o lecturas extensas, ¿sientes que aprendes mejor si la información se divide en bloques cortos con pausas?",
        "opciones": ["Casi nunca me pasa", "A veces me sucede", "Me describe totalmente"],
        "puntaje": [0, 1, 2]
    },
    {
        "id": 3,
        "dimension": "Enfoque e Indicaciones",
        "pregunta": "3. Cuando estás muy concentrado/a en una actividad, ¿te ayuda que te llamen por tu nombre o te muestren un apoyo visual para cambiar de tarea?",
        "opciones": ["Casi nunca me pasa", "A veces me sucede", "Me describe totalmente"],
        "puntaje": [0, 1, 2]
    },
    {
        "id": 4,
        "dimension": "Seguimiento de Metas",
        "pregunta": "4. Al iniciar un proyecto complejo, ¿prefieres contar con una guía paso a paso o una lista de verificación para no saltarte etapas?",
        "opciones": ["Casi nunca me pasa", "A veces me sucede", "Me describe totalmente"],
        "puntaje": [0, 1, 2]
    },
    {
        "id": 5,
        "dimension": "Organización y Tiempos",
        "pregunta": "5. ¿Te gustaría disponer de plantillas visuales u organizadores digitales para estructurar tus horarios y archivos de estudio?",
        "opciones": ["Casi nunca me pasa", "A veces me sucede", "Me describe totalmente"],
        "puntaje": [0, 1, 2]
    },
    {
        "id": 6,
        "dimension": "Estímulo y Motivación",
        "pregunta": "6. Frente a contenidos teóricos o extensos, ¿sientes que tu interés se mantiene más alto si se acompañan de videos o casos prácticos?",
        "opciones": ["Casi nunca me pasa", "A veces me sucede", "Me describe totalmente"],
        "puntaje": [0, 1, 2]
    },
    {
        "id": 7,
        "dimension": "Gestión de Recursos",
        "pregunta": "7. ¿Te ha ocurrido que pierdes tiempo buscando apuntes o archivos importantes justo antes de iniciar una actividad?",
        "opciones": ["Casi nunca me pasa", "A veces me sucede", "Me describe totalmente"],
        "puntaje": [0, 1, 2]
    },
    {
        "id": 8,
        "dimension": "Filtro de Estímulos",
        "pregunta": "8. En entornos con ruido, personas en movimiento o notificaciones, ¿notas que tu mente se distrae hacia esos estímulos?",
        "opciones": ["Casi nunca me pasa", "A veces me sucede", "Me describe totalmente"],
        "puntaje": [0, 1, 2]
    },
    {
        "id": 9,
        "dimension": "Recordatorios Activos",
        "pregunta": "9. ¿Te resulta conveniente utilizar alertas, calendarios visuales o recordatorios amigables para tus compromisos formativos?",
        "opciones": ["Casi nunca me pasa", "A veces me sucede", "Me describe totalmente"],
        "puntaje": [0, 1, 2]
    },
    {
        "id": 10,
        "dimension": "Canales de Comunicación",
        "pregunta": "10. Cuando te dan indicaciones habladas complejas, ¿prefieres que queden registradas por escrito o en un mapa gráfico?",
        "opciones": ["Casi nunca me pasa", "A veces me sucede", "Me describe totalmente"],
        "puntaje": [0, 1, 2]
    }
]

respuestas_estudiante = {}
puntaje_acumulado = 0

for item in banco_preguntas_empaticas:
    st.markdown(f"**Aspecto de Apoyo:** *{item['dimension']}*")
    seleccion = st.radio(
        label=item["pregunta"],
        options=item["opciones"],
        key=f"emp_p_{item['id']}"
    )
    idx = item["opciones"].index(seleccion)
    pts = item["puntaje"][idx]
    
    puntaje_acumulado += pts
    respuestas_estudiante[item["dimension"]] = pts
    st.write("")

# Botón para que el estudiante envíe sus respuestas
st.markdown("---")
if st.button("✅ Enviar mis respuestas", type="primary"):
    st.success(f"¡Muchas gracias, {nombre_aprendiz}! Tus respuestas han sido registradas. Tu instructor analizará la información para adaptar las metodologías DUA del curso.")

# =========================================================================
# SECCIÓN EXCLUSIVA DEL INSTRUCTOR (PROTEGIDA POR CLAVE TIPO ASK KAI)
# =========================================================================
st.markdown("---")
with st.expander("🔒 Área Exclusiva para el Instructor SENA (Consulta de Informe y Descarga)"):
    clave_ingresada = st.text_input("Ingrese la clave de autorización del instructor:", type="password")
    
    # Clave predeterminada de acceso para el docente
    CLAVE_INSTRUCTOR = "DUA2026"
    
    if clave_ingresada == CLAVE_INSTRUCTOR:
        st.success("Acceso concedido al Panel Docente de Orientación Pedagógica.")
        
        # 1. Construcción del Informe Texto tipo Ask Kai
        informe_texto = f"""# INFORME DE ORIENTACIÓN PEDAGÓGICA Y APORTES DUA
PerfilAprende - Servicio Nacional de Aprendizaje (SENA)

INFORMACIÓN DEL APRENDIZ:
- Nombre: {nombre_aprendiz}
- Programa: {programa_sena}
- Puntaje de Indicadores DUA: {puntaje_acumulado} / 20

ACERCA DE ESTE INFORME:
Este documento constituye una guía orientativa pedagógica basada en los principios del Diseño Universal 
para el Aprendizaje (DUA). No reemplaza una evaluación clínica ni constituye un diagnóstico de salud mental.

RESULTADOS Y NIVELES DE RECOMENDACIÓN:
"""
        if puntaje_acumulado <= 6:
            informe_texto += "- Perfil de Procesamiento Estándar: Sin indicios significativos de barreras. Mantener retos de profundización.\n"
        elif 7 <= puntaje_acumulado <= 13:
            informe_texto += "- Indicios Moderados de Apoyo: Se sugieren ajustes razonables como tipografías accesibles, guías paso a paso y tiempos flexibles.\n"
        else:
            informe_texto += "- Alta Necesidad de Andamiaje DUA: Se requiere estructuración multisensorial (audios, esquemas visuales y fragmentación rigurosa de tareas).\n"

        informe_texto += "\nÁREAS PRIORITARIAS DE APOYO DETECTADAS:\n"
        areas_prioritarias = [dim for dim, pts in respuestas_estudiante.items() if pts == 2]
        if areas_prioritarias:
            for area in areas_prioritarias:
                informe_texto += f"- {area}: Aplicar apoyos específicos en la presentación de guías y evaluaciones.\n"
        else:
            informe_texto += "- No se detectan áreas críticas individuales de puntaje máximo.\n"

        informe_texto += """
RECURSOS RECOMENDADOS PARA EL INSTRUCTOR:
1. Guía rápida sobre el Diseño Universal para el Aprendizaje (DUA)[cite: 25].
2. Estrategias de adaptación de contenidos para el programa de Gestión del Talento Humano[cite: 25].
"""

        # 2. Renderizar el informe en pantalla para el docente
        st.markdown(f"### 📄 Reporte Generado para {nombre_aprendiz}")
        st.text_area("Vista previa del Informe Técnico (Ask Kai Format):", informe_texto, height=300)
        
        # 3. Botón para la descarga del archivo en formato TXT / Markdown
        st.download_button(
            label="📥 Descargar Informe Completo para Archivo Docente (.txt)",
            data=informe_texto,
            file_name=f"Informe_DUA_{nombre_aprendiz.replace(' ', '_')}.txt",
            mime="text/plain"
        )
    elif clave_ingresada != "":
        st.error("Clave incorrecta. Solo el instructor o personal autorizado puede consultar o descargar este reporte.")
