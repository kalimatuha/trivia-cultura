import random
import json
import streamlit as st

# Cargar el dataset de preguntas desde un archivo JSON
with open('trivia.json', 'r', encoding='utf-8') as f:
    trivia_data = json.load(f)

# Función principal del juego de trivia
def trivia_game():
    st.title("Trivial Jedi - ¡Juega ahora!")
    st.write("Te haré preguntas de cultura general de cualquier categoría. ¡Responde y ve tu puntuación en tiempo real!")

    # Inicializar estado de la sesión
    if "score" not in st.session_state:
        st.session_state.score = 0
        st.session_state.total_questions = 0
        st.session_state.question = None
        st.session_state.correct_answer = None

    # Generar nueva pregunta si no hay una activa
    if st.session_state.question is None:
        category = random.choice(trivia_data['categories'])
        item = random.choice(category['questions'])
        st.session_state.question = item['question']
        st.session_state.correct_answer = item['answer'].lower()

    # Mostrar pregunta actual
    st.write(f"**Pregunta:** {st.session_state.question}")

    # Entrada de texto para respuesta, reiniciada al enviar
    user_input = st.text_input("Tu respuesta:", key="respuesta").strip().lower()

    if st.button("Enviar respuesta"):
        if user_input:
            st.session_state.total_questions += 1
            if user_input == st.session_state.correct_answer:
                st.success("¡Correcto!")
                st.session_state.score += 1
            else:
                st.error(f"Incorrecto. La respuesta correcta era: {st.session_state.correct_answer}")

            # Reiniciar la pregunta y vaciar cuadro de texto
            st.session_state.question = None
            st.session_state["respuesta"] = ""

    # Mostrar puntuación actual
    st.write(f"**Puntuación:** {st.session_state.score}/{st.session_state.total_questions}")

# Ejecutar la aplicación
if __name__ == "__main__":
    trivia_game()

