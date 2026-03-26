import streamlit as st
import pandas as pd
import plotly.express as px

def show_dashboard(req_time, top_endpoints, status_counts):
    st.header("📊 Dashboard")

    # Requests over time
    req_df = pd.DataFrame(req_time)
    def extract_time(x):
        if isinstance(x, dict):
            return x.get("start")
        elif isinstance(x, list):
            return x[0]
        return x
    st.subheader("📈 Key Metrics")

    col1, col2, col3 = st.columns(3)

    total_requests = sum([x["count"] for x in req_time])
    total_errors = sum([x["count"] for x in status_counts if x["status"] >= 400])
    error_rate = total_errors / total_requests if total_requests > 0 else 0

    with col1:
        st.metric("Total Requests", f"{total_requests:,}")

    with col2:
        st.metric("Total Errors", f"{total_errors:,}")

    with col3:
        st.metric("Error Rate", f"{error_rate:.2%}")
    
    req_df["time"] = req_df["window"].apply(extract_time)

    fig1 = px.line(req_df, x="time", y="count", title="Requests Over Time")
    st.plotly_chart(fig1, use_container_width=True)

    # Top endpoints
    top_df = pd.DataFrame(top_endpoints)
    fig2 = px.bar(top_df, x="endpoint", y="count", title="Top Endpoints")
    st.plotly_chart(fig2, use_container_width=True)

    # Status codes
    status_df = pd.DataFrame(status_counts)
    fig3 = px.pie(status_df, names="status", values="count", title="Status Distribution")
    st.plotly_chart(fig3, use_container_width=True)