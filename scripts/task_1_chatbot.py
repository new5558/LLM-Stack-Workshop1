import streamlit as st


# =====================================================
# Initialize your LLM client here (e.g., OpenAI, Google Gemini, etc.)
# =====================================================


# ====== LLM CALL FUNCTION ======
def get_response(messages):
    return "Please fill this function."


# ====== STREAMLIT UI ======
st.set_page_config(page_title="LLM Chatbot")

st.title("🤖 LLM Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Type your message..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Call LLM
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_response(st.session_state.messages)
            st.markdown(response)

    # Add assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})
