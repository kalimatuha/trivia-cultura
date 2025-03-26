import random
import json
import streamlit as st

# Cargar el dataset de preguntas desde un archivo JSON
with open('trivia.json', 'r', encoding='utf-8') as f:
    trivia_data = json.load(f)

# Función principal del juego de trivia
def trivia_game():
    st.title("Trivial Jedi - ¡Juega ahora!")
    st.write("Responde las preguntas y acumula puntos en tiempo real.")

    # Inicializar estado de la sesión
    if "score" not in st.session_state:
        st.session_state.score = 0
        st.session_state.total_questions = 0
        st.session_state.question = None
        st.session_state.correct_answer = None
        st.session_state.answered = False  # Controla si se respondió la pregunta

    # Generar nueva pregunta si no hay una activa o si se presionó "Siguiente"
    if st.session_state.question is None or st.session_state.answered:
        category = random.choice(trivia_data['categories'])
        item = random.choice(category['questions'])
        st.session_state.question = item['question']
        st.session_state.correct_answer = item['answer'].lower()
        st.session_state.answered = False  # Reinicia el estado de respuesta

    # Mostrar pregunta actual
    st.write(f"**Pregunta:** {st.session_state.question}")

    # Entrada de texto para respuesta con clave única
    user_input = st.text_input(
        "Tu respuesta:", key=f"respuesta_{st.session_state.total_questions}"
    ).strip().lower()

    # Botón para enviar respuesta
    if st.button("Enviar respuesta") and not st.session_state.answered:
        if user_input:
            st.session_state.total_questions += 1
            if user_input == st.session_state.correct_answer:
                st.success("¡Correcto!")
                st.session_state.score += 1
            else:
                st.error(f"Incorrecto. La respuesta correcta era: {st.session_state.correct_answer}")
            st.session_state.answered = True  # Cambiar estado a respondido

    # Mostrar puntuación actual
    st.write(f"**Puntuación:** {st.session_state.score}/{st.session_state.total_questions}")

    # Botón para pasar a la siguiente pregunta
    if st.session_state.answered and st.button("Siguiente"):
        st.session_state.question = None  # Reiniciar la pregunta activa

# Ejecutar la aplicación
if __name__ == "__main__":
    trivia_game()

