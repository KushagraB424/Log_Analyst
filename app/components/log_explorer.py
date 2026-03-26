import streamlit as st
import pandas as pd

def show_log_explorer(df):
    st.header("🔍 Log Explorer")

    col1, col2, col3 = st.columns(3)

    with col1:
        ip_filter = st.text_input("Filter by IP")

    with col2:
        endpoint_filter = st.text_input("Filter by Endpoint")

    with col3:
        status_filter = st.selectbox(
            "Status Code",
            ["All"] + sorted(df["status"].dropna().unique().tolist())
        )

    filtered_df = df.copy()

    if ip_filter:
        filtered_df = filtered_df[filtered_df["ip"].str.contains(ip_filter, case=False, na=False)]

    if endpoint_filter:
        filtered_df = filtered_df[filtered_df["endpoint"].str.contains(endpoint_filter, case=False, na=False)]

    if status_filter != "All":
        filtered_df = filtered_df[filtered_df["status"] == status_filter]

    # Pagination
    page_size = 20
    total_pages = max(1, len(filtered_df) // page_size + 1)

    page = st.number_input("Page", min_value=1, max_value=total_pages, step=1)

    start = (page - 1) * page_size
    end = start + page_size

    st.dataframe(filtered_df.iloc[start:end])
    st.write(f"Showing {len(filtered_df)} results")