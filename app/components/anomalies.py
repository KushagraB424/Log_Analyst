import streamlit as st
import pandas as pd

def show_anomalies(anomalies):
    st.header("🚨 Anomaly Alerts")

    if len(anomalies) > 0:
        st.error(f"⚠️ {len(anomalies)} anomalies detected!")
    else:
        st.success("✅ No anomalies detected")

    df = pd.DataFrame(anomalies)

    st.dataframe(df)