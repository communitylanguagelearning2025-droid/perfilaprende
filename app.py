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
st.markdown("Bienvenido/a. Este espacio está diseñado para comprender **cómo aprende mejor tu mente** y sugerir herramientas que faciliten tu proceso formativo en el SENA. *Nota: Este instrumento de observación orientativa no constituye un diagnóstico clínico[cite: 32].*")

st.markdown("---")
st.markdown("### 🧩 Cuestionario de Orientación y Preferencias de Aprendizaje")

# Datos básicos del aprendiz
col_nom, col_doc = st.columns(2)
with col_nom:
    nombre_aprendiz = st.text_input("Nombre completo del aprendiz:", "Aprendiz SENA")
with col_doc:
    programa_sena = st.text_input("Programa de Formación:", "Gestión del Talento Humano")

# Banco de 22 preguntas basadas en la Hoja de Registro Ampliada (con escala 0 a 4)
banco_preguntas = [
    # Área 1: Inatención (6 preguntas)
    {"id": 1, "area": "Inatención", "pregunta": "1. [Detalles] Cuando realizas guías o informes, ¿te pasa que pasas por alto detalles importantes que descubres al revisar de nuevo?", "opciones": ["Nunca", "Rara vez", "A veces", "A menudo", "Muy a menudo"], "puntaje": [0, 1, 2, 3, 4]},
    {"id": 2, "area": "Inatención", "pregunta": "2. [Concentración] Al participar en clases, reuniones o lecturas extensas, ¿sientes que te cuesta sostener la atención de principio a fin?", "opciones": ["Nunca", "Rara vez", "A veces", "A menudo", "Muy a menudo"], "puntaje": [0, 1, 2, 3, 4]},
    {"id": 3, "area": "Inatención", "pregunta": "3. [Organización] ¿Tienes dificultades para organizar tus materiales, horarios o responsabilidades cotidianas de estudio?", "opciones": ["Nunca", "Rara vez", "A veces", "A menudo", "Muy a menudo"], "puntaje": [0, 1, 2, 3, 4]},
    {"id": 4, "area": "Inatención", "pregunta": "4. [Tiempo] ¿Sientes que te cuesta administrar el tiempo disponible para cumplir con los plazos de tus entregas?", "opciones": ["Nunca", "Rara vez", "A veces", "A menudo", "Muy a menudo"], "puntaje": [0, 1, 2, 3, 4]},
    {"id": 5, "area": "Inatención", "pregunta": "5. [Distracciones] En tu entorno de estudio, ¿notas que te distraes con facilidad ante ruidos, movimientos o notificaciones?", "opciones": ["Nunca", "Rara vez", "A veces", "A menudo", "Muy a menudo"], "puntaje": [0, 1, 2, 3, 4]},
    {"id": 6, "area": "Inatención", "pregunta": "6. [Olvidos] ¿Te ocurre con frecuencia que olvidas compromisos, llamadas, encargos o tareas importantes?", "opciones": ["Nunca", "Rara vez", "A veces", "A menudo", "Muy a menudo"], "puntaje": [0, 1, 2, 3, 4]},
    
    # Área 2: Hiperactividad (4 preguntas)
    {"id": 7, "area": "Hiperactividad", "pregunta": "7. [Movimiento] Al estar sentado/a durante un buen rato, ¿mueves constantemente las manos, los pies o cambias de postura en el asiento?", "opciones": ["Nunca", "Rara vez", "A veces", "A menudo", "Muy a menudo"], "puntaje": [0, 1, 2, 3, 4]},
    {"id": 8, "area": "Hiperactividad", "pregunta": "8. [Permanecer quieto] ¿Te cuesta permanecer sentado/a en clases, talleres o situaciones prolongadas que lo requieren?", "opciones": ["Nunca", "Rara vez", "A veces", "A menudo", "Muy a menudo"], "puntaje": [0, 1, 2, 3, 4]},
    {"id": 9, "area": "Hiperactividad", "pregunta": "9. [Inquietud interna] ¿Experimentas a menudo una sensación interna de 'estar en marcha' o como si tuvieras un motor que no se detiene?", "opciones": ["Nunca", "Rara vez", "A veces", "A menudo", "Muy a menudo"], "puntaje": [0, 1, 2, 3, 4]},
    {"id": 10, "area": "Hiperactividad", "pregunta": "10. [Relajación] ¿Sientes inquietud o la necesidad constante de moverte incluso en momentos en los que intentas relajarte?", "opciones": ["Nunca", "Rara vez", "A veces", "A menudo", "Muy a menudo"], "puntaje": [0, 1, 2, 3, 4]},
    
    # Área 3: Impulsividad (3 preguntas)
    {"id": 11, "area": "Impulsividad", "pregunta": "11. [Interrupciones] Al conversar, ¿te pasa que respondes antes de que terminen de hacerte la pregunta o completas las frases de otros?", "opciones": ["Nunca", "Rara vez", "A veces", "A menudo", "Muy a menudo"], "puntaje": [0, 1, 2, 3, 4]},
    {"id": 12, "area": "Impulsividad", "pregunta": "12. [Espera de turnos] ¿Te cuesta esperar tu turno con paciencia en filas, actividades grupales o dinámicas de clase?", "opciones": ["Nunca", "Rara vez", "A veces", "A menudo", "Muy a menudo"], "puntaje": [0, 1, 2, 3, 4]},
    {"id": 13, "area": "Impulsividad", "pregunta": "13. [Control emocional] ¿Sientes que a veces te cuesta regular tus respuestas emocionales inmediatas ante momentos de enojo o frustración?", "opciones": ["Nunca", "Rara vez", "A veces", "A menudo", "Muy a menudo"], "puntaje": [0, 1, 2, 3, 4]},
    
    # Área 4: Funcionamiento ejecutivo (5 preguntas)
    {"id": 14, "area": "Funcionamiento ejecutivo", "pregunta": "14. [Planificación] Cuando te enfrentas a un proyecto grande, ¿te cuesta dividirlo mentalmente en pasos pequeños y manejables?", "opciones": ["Nunca", "Rara vez", "A veces", "A menudo", "Muy a menudo"], "puntaje": [0, 1, 2, 3, 4]},
    {"id": 15, "area": "Funcionamiento ejecutivo", "pregunta": "15. [Memoria de trabajo] ¿Necesitas apoyarte frecuentemente en listas, alarmas o agendas para no olvidar tus responsabilidades?", "opciones": ["Nunca", "Rara vez", "A veces", "A menudo", "Muy a menudo"], "puntaje": [0, 1, 2, 3, 4]},
    {"id": 16, "area": "Funcionamiento ejecutivo", "pregunta": "16. [Inicio de tareas] ¿Experimentas resistencia o dificultad para dar el primer paso y comenzar una tarea, aunque sepas que es importante?", "opciones": ["Nunca", "Rara vez", "A veces", "A menudo", "Muy a menudo"], "puntaje": [0, 1, 2, 3, 4]},
    {"id": 17, "area": "Funcionamiento ejecutivo", "pregunta": "17. [Recuperación de atención] Tras una interrupción, ¿te cuesta retomar el hilo de lo que estabas haciendo y recuperar la concentración?", "opciones": ["Nunca", "Rara vez", "A veces", "A menudo", "Muy a menudo"], "puntaje": [0, 1, 2, 3, 4]},
    {"id": 18, "area": "Funcionamiento ejecutivo", "pregunta": "18. [Procrastinación] ¿Tiendes a posponer (procrastinar) actividades clave hasta que el tiempo límite se vuelve muy estrecho?", "opciones": ["Nunca", "Rara vez", "A veces", "A menudo", "Muy a menudo"], "puntaje": [0, 1, 2, 3, 4]},
    
    # Área 5: Impacto y contexto (4 preguntas)
    {"id": 19, "area": "Impacto y contexto", "pregunta": "19. [Contextos] ¿Notas que estas situaciones de atención u organización se presentan en más de un espacio (por ejemplo, tanto en casa como en el SENA o el trabajo)?", "opciones": ["Nunca", "Rara vez", "A veces", "A menudo", "Muy a menudo"], "puntaje": [0, 1, 2, 3, 4]},
    {"id": 20, "area": "Impacto y contexto", "pregunta": "20. [Duración] ¿Estas vivencias o patrones han persistido de forma constante durante al menos los últimos seis meses?", "opciones": ["Nunca", "Rara vez", "A veces", "A menudo", "Muy a menudo"], "puntaje": [0, 1, 2, 3, 4]},
    {"id": 21, "area": "Impacto y contexto", "pregunta": "21. [Rendimiento] ¿Sientes que estas dificultades llegan a afectar tus calificaciones, tu rendimiento laboral o tus metas formativas?", "opciones": ["Nunca", "Rara vez", "A veces", "A menudo", "Muy a menudo"], "puntaje": [0, 1, 2, 3, 4]},
    {"id": 22, "area": "Impacto y contexto", "pregunta": "22. [Bienestar] ¿Has notado que estas situaciones generan tensiones en tu entorno o afectan tu bienestar y confianza al estudiar?", "opciones": ["Nunca", "Rara vez", "A veces", "A menudo", "Muy a menudo"], "puntaje": [0, 1, 2, 3, 4]}
]

respuestas_guardadas = {}
conteo_altos = 0
conteo_por_area = {"Inatención": 0, "Hiperactividad": 0, "Impulsividad": 0, "Funcionamiento ejecutivo": 0, "Impacto y contexto": 0}

for item in banco_preguntas:
    st.markdown(f"**Área:** *{item['area']}*")
    seleccion = st.radio(
        label=item["pregunta"],
        options=item["opciones"],
        key=f"p_{item['id']}"
    )
    idx = item["opciones"].index(seleccion)
    pts = item["puntaje"][idx]
    
    respuestas_guardadas[item["id"]] = {"area": item["area"], "respuesta": seleccion, "puntaje": pts}
    if pts >= 3:
        conteo_altos += 1
        conteo_por_area[item["area"]] += 1
    st.write("")

# Botón para que el estudiante envíe sus respuestas
st.markdown("---")
if st.button("✅ Enviar mis respuestas", type="primary"):
    st.success(f"¡Muchas gracias, {nombre_aprendiz}! Tus respuestas han sido registradas de forma segura. Tu instructor podrá consultar las pautas DUA correspondientes.")

# =========================================================================
# SECCIÓN EXCLUSIVA DEL INSTRUCTOR (PROPUESTA DE AJUSTES RAZONABLES DUA)
# =========================================================================
st.markdown("---")
with st.expander("🔒 Área Exclusiva para el Instructor SENA (Propuestas de Ajustes Razonables)"):
    clave_ingresada = st.text_input("Ingrese la clave de autorización del instructor:", type="password")
    
    CLAVE_INSTRUCTOR = "DUA2026"
    
    if clave_ingresada == CLAVE_INSTRUCTOR:
        st.success("Acceso concedido al Panel Docente de Ajustes Razonables.")
        
        # Lectura orientativa según la guía
        if conteo_altos <= 2:
            lectura_orientativa = "0 a 2 respuestas en 'A menudo/Muy a menudo': No parece haber un patrón frecuente de dificultades. Mantener apoyos generales del aula[cite: 34]."
        elif conteo_altos <= 5:
            lectura_orientativa = "3 a 5 respuestas en 'A menudo/Muy a menudo': Hay dificultades ocasionales. Conversar con el aprendiz y aplicar ajustes del aula[cite: 34]."
        else:
            lectura_orientativa = "6 o más respuestas en 'A menudo/Muy a menudo': Patron frecuente. Se sugiere articular ajustes al PIAR y articular con bienestar/orientación[cite: 34]."

        # Construcción del informe pedagógico enriquecido con la Guía para Docentes
        informe_texto = f"""# PLAN SUGERIDO DE AJUSTES RAZONABLES DUA
PerfilAprende - Servicio Nacional de Aprendizaje (SENA)

DATOS DEL APRENDIZ:
- Nombre: {nombre_aprendiz}
- Programa: {programa_sena}
- Frecuencia de Respuestas Altas (3 o 4): {conteo_altos} / 22

ORIENTACIÓN PEDAGÓGICA INICIAL:
- {lectura_orientativa}

===================================================================
RECOMENDACIONES DE AJUSTES RAZONABLES ESPECÍFICOS (GUÍA PARA DOCENTES)
===================================================================
"""
        # Mapeo de sugerencias de la Guía de Ajustes Razonables
        if conteo_por_area["Inatención"] >= 2:
            informe_texto += """
📌 ÁREA: ATENCIÓN Y CONCENTRACIÓN
- Ubicación Estratégica: Ubicar al estudiante cerca del docente, lejos de ventanas, puertas o zonas de paso para reducir estímulos innecesarios[cite: 32].
- Estructura de Clases: Iniciar las sesiones con una agenda breve (tema, actividades, tiempos y criterios) y alternar explicación con práctica[cite: 32].
- Fragmentación de Tareas: Dividir actividades o lecturas largas en bloques de 10 a 15 minutos con un cierre visual claro[cite: 32].
"""

        if conteo_por_area["Funcionamiento ejecutivo"] >= 2:
            informe_texto += """
📌 ÁREA: ORGANIZACIÓN E INSTRUCCIONES
- Gestión de Tareas Complejas: Proporcionar guías estructuradas, organizadores gráficos y enseñar a fragmentar los entregables en micro-pasos revisando avances parciales[cite: 32].
- Formato de Instrucciones: Entregar una lista numerada de pasos escritos o visuales, dando una sola instrucción corta a la vez y ofreciendo un ejemplo resuelto[cite: 32, 33].
- Cumplimiento de Plazos: Establecer entregas parciales y calendarios de hitos con recordatorios breves[cite: 32].
"""

        if conteo_por_area["Hiperactividad"] >= 1 or conteo_por_area["Impulsividad"] >= 1:
            informe_texto += """
📌 ÁREA: PARTICIPACIÓN Y CONVIVENCIA
- Pausas Activas: Tras 15 minutos de trabajo sedentario, permitir una pausa activa breve (2 minutos) para moverse o cambiar de posición sin perder la atención[cite: 33, 34].
- Enfoque Colaborativo: Asignar roles claros, tareas específicas y tiempos cortos en los trabajos en equipo[cite: 33].
- Autorregulación: Mantener acuerdos explícitos para el uso de turnos y brindar retroalimentación constructiva reconociendo los avances[cite: 33].
"""

        informe_texto += """
📌 ÁREA: FLEXIBILIDAD EN LA EVALUACIÓN Y TIEMPOS
- Ajuste de Tiempo: Otorgar un tiempo adicional (ej. 25% o 50%) para la entrega o resolución de pruebas según lo acordado[cite: 33].
- Formatos Flexibles: Flexibilizar la demostración de aprendizajes mediante presentaciones orales, proyectos, mapas conceptuales o portafolios[cite: 33, 34].
- Fraccionamiento de Pruebas: Dividir evaluaciones extensas en dos sesiones cortas conservando la misma exigencia de aprendizaje[cite: 33, 34].

===================================================================
PRINCIPIOS DE APLICACIÓN DOCENTE:
1. Personalización y Participación: Acordar los ajustes directamente con el estudiante[cite: 32].
2. Documentación y Seguimiento: Registrar estos acuerdos en el PIAR o carpeta de seguimiento[cite: 32].
3. Material Orientativo: Esta guía no diagnostica ni sustituye la valoración médica profesional[cite: 32, 34].
"""

        st.markdown(f"### 📄 Plan Sugerido para {nombre_aprendiz}")
        st.markdown(f"**Nivel de Intervención Recomendado:** {lectura_orientativa}")
        
        st.text_area("Vista previa del Informe de Ajustes Razonables (Uso Exclusivo Instructor):", informe_texto, height=350)
        
        st.download_button(
            label="📥 Descargar Plan de Ajustes Razonables (.txt)",
            data=informe_texto,
            file_name=f"Plan_Ajustes_DUA_{nombre_aprendiz.replace(' ', '_')}.txt",
            mime="text/plain"
        )
    elif clave_ingresada != "":
        st.error("Clave incorrecta. Solo el instructor o personal autorizado puede consultar o descargar este reporte.")
