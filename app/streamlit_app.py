from utils.data_loader import load_logs, load_json
from components.log_explorer import show_log_explorer
from components.dashboard import show_dashboard
from components.anomalies import show_anomalies
from utils.gemini_client import setup_gemini, generate_summary
import streamlit as st
from utils.gemini_client import ask_question

st.set_page_config(
    page_title="Log Analytics AI System",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

st.title("📊 Distributed Log Analytics System")

# Load data
logs_df = load_logs()
req_time = load_json("data/processed/requests_over_time.json")
top_endpoints = load_json("data/processed/top_endpoints.json")
status_counts = load_json("data/processed/status_counts.json")
anomalies = load_json("data/processed/anomalies.json")
metrics = load_json("data/processed/aggregated_metrics.json")

# Sidebar
st.sidebar.title("⚙️ Navigation")

section = st.sidebar.radio(
    "Go to",
    ["Dashboard", "Log Explorer", "Anomalies", "AI Insights"]
)

if section == "Dashboard":
    show_dashboard(req_time, top_endpoints, status_counts)

elif section == "Log Explorer":
    show_log_explorer(logs_df)

elif section == "Anomalies":
    show_anomalies(anomalies)

elif section == "AI Insights":
    st.header("🤖 AI Insights")

    tab1, tab2 = st.tabs(["📊 Summary", "❓ Ask Questions"])

    # -------- SUMMARY TAB --------
    with tab1:
        if st.button("Generate Summary"):
            with st.spinner("Analyzing logs with AI..."):
                summary = generate_summary(metrics)
                st.success("Summary Generated")
                st.write(summary)

    # -------- Q&A TAB --------
    with tab2:
        st.subheader("Ask Questions About Logs")

        # Initialize chat history
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        # Input box
        question = st.text_input("Enter your question:")

        if st.button("Ask"):
            if question:
                with st.spinner("Thinking..."):
                    answer = ask_question(metrics, question)

                    # Store in history
                    st.session_state.chat_history.append({
                        "question": question,
                        "answer": answer
                    })

        # Display chat history
        for chat in reversed(st.session_state.chat_history):
            st.markdown(f"**🧑‍💻 You:** {chat['question']}")
            st.markdown(f"**🤖 AI:** {chat['answer']}")
            st.markdown("---")

st.markdown("---")
st.markdown("Built with ❤️ using PySpark, Streamlit & Gemini AI")