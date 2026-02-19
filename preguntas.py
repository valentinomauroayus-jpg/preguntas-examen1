import streamlit as st

st.title("🚀 Evolución del iPhone y sus Innovaciones")
st.write("Responde a las preguntas.¡Buena suerte!")

preguntas = [
    {
        "texto": "¿En qué año presentó Steve Jobs el primer iPhone, revolucionando la industria de la telefonía móvil?",
        "opciones": ["2006", "2007", "2005", "2008"],
        "correcta": "2007"
    },
    {
        "texto": "¿Cuál fue el primer modelo de iPhone en introducir el sistema de biometría 'Face ID'?",
        "opciones": ["Iphone X", "Iphone 8", "Iphone XS", "Iphone 7 Plus"],
        "correcta": "Iphone X"
    },
    {
        "texto": "¿Qué nombre recibe el procesador diseñado por Apple que debutó en el iPhone 15 Pro?",
        "opciones": ["M2", "A16 Bionic", "A17 Pro", "A17 Bionic"],
        "correcta": "A17 Pro"
    },
    {
        "texto": "¿Cuál fue el primer iPhone que reemplazó el puerto Lightning por el estándar USB-C?",
        "opciones": ["Iphone 14 Pro", "Iphone 12", "Iphone 15", "Iphone13"],
        "correcta": "Iphone 15"
    },
    {
        "texto": "El iPhone 4 fue famoso por su diseño de cristal y acero, pero ¿qué problema de hardware causó controversia en su lanzamiento?",
        "opciones": ["Pantallas amarillentas", "Problemas de cobertura (Antennagate)", "Sobrecalentamiento excesivo", "Baterías que se hinchaban"],
        "correcta": "Problemas de cobertura (Antennagate)"
    },
    {
        "texto": "¿Cuál fue el primer modelo de iPhone en ofrecer una versión Plus con pantalla más grande?",
        "opciones": ["iPhone 5", "iPhone 6S", "iPhone 7", "iPhone 6"],
        "correcta": "iPhone 6"
    },
    {
        "texto": "¿Cómo se llama la función introducida en el iPhone 14 Pro que aprovecha el recorte de la pantalla para mostrar notificaciones interactivas?",
        "opciones": ["Dynamic Island", "Control Center", "Interactive Notch", "Smart Cutout"],
        "correcta": "Dynamic Island"
    },
    {
        "texto": "¿Qué modelo de iPhone fue el primero en eliminar el conector de auriculares de 3.5 mm?",
        "opciones": ["iPhone 6S", "iPhone 8", "iPhone 7", "iPhone X"],
        "correcta": "iPhone 7"
    },
    {
        "texto": "¿Cuál es el sistema operativo que ejecutan todos los iPhone?",
        "opciones": ["iPadOS", "iOS", "macOS", "watchOS"],
        "correcta": "iOS"
    }
]

with st.form("quiz_form"):

    respuestas_usuario = []

    for i, pregunta in enumerate(preguntas):
        st.subheader(pregunta["texto"])

        # Permitimos dejar en blanco añadiendo una opción vacía
        eleccion = st.radio(
            "Elige una opción:",
            [""] + pregunta["opciones"],
            format_func=lambda x: "Selecciona una opción" if x == "" else x,
            key=f"pregunta_{i}"
        )

        respuestas_usuario.append(eleccion)
        st.write("---")

    enviado = st.form_submit_button("Entregar examen")

if enviado:

    aciertos = 0
    errores = 0
    informe = []
    total = len(preguntas)

    for i in range(total):

        if respuestas_usuario[i] == "":
            informe.append(f"➖ **Pregunta {i+1}**: No respondida")
            continue

        if respuestas_usuario[i] == preguntas[i]["correcta"]:
            aciertos += 1
            informe.append(f"✅ **Pregunta {i+1}**: Correcta")
        else:
            errores += 1
            informe.append(
                f"❌ **Pregunta {i+1}**: Incorrecta (Correcta: {preguntas[i]['correcta']})"
            )

    # Las incorrectas restan
    nota = ((aciertos - errores) / total) * 10
    nota = max(nota, 0)

    # Nota redondeada
    nota = round(nota, 2)

    st.divider()
    st.header(f"Resultado final: {nota} / 10")

    # Feedback por tramos
    if nota < 2:
        st.error("Muy insuficiente. Necesitas repasar todo el contenido.")
    elif 2 <= nota < 5:
        st.error("Insuficiente. Debes estudiar más.")
    elif 5 <= nota < 6:
        st.warning("Suficiente. Has aprobado por poco.")
        st.balloons()
    elif 6 <= nota < 7:
        st.success("Bien. Buen trabajo.")
        st.balloons()
    elif 7 <= nota < 9:
        st.success("Notable. Muy buen resultado.")
        st.balloons()
    elif 9 <= nota < 10:
        st.success("Sobresaliente. Excelente dominio del tema.")
        st.balloons()
    else:
        st.success("Excelente. Examen perfecto.")
        st.balloons()

    tab_resumen, tab_informe = st.tabs(["Resumen", "Informe detallado"])

    with tab_resumen:
        st.metric("Aciertos", aciertos)
        st.metric("Errores", errores)
        st.metric("Nota final", nota)

    with tab_informe:
        st.markdown("### 📋 Informe del examen")
        for linea in informe:
            st.markdown(linea)
