import streamlit as st
import requests
import sqlite3

con = sqlite3.connect("test_db.db")

cur = con.cursor()

# Streamlit app title
st.title("Chat with LLM")

# Input field for user to ask a question
user_question = st.text_input("Ask a question:")


# Function to communicate with FastAPI backend
def get_answer_from_backend(question):
    url = "http://127.0.0.1:8000/ask/"
    payload = {"user_question": question}
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        answer = response.json().get("answer")
        cur.execute("""INSERT INTO answers VALUES(?, ?, ?)""", (1, question, answer))
        con.commit()
        return answer
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
        return None

# Display conversation history
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Button to submit the question
if st.button("Submit"):
    if user_question:
        # Get the response from the backend
        answer = get_answer_from_backend(user_question)

        # Append question and answer to the conversation history
        if answer:
            st.session_state.conversation.append({"question": user_question, "answer": answer})
    else:
        st.error("Please ask a question.")

# Display the conversation
for chat in st.session_state.conversation:
    st.markdown(f"**You**: {chat['question']}")
    st.markdown(f"**LLM**: {chat['answer']}")
    st.markdown("---")
