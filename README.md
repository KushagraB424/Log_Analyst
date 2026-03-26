# Distributed Log Analytics & AI Monitoring System

## Overview
This project is a scalable log analytics system that processes large-scale web server logs and provides an interactive dashboard with AI-powered insights. It combines distributed data processing (PySpark) with a modern analytics UI (Streamlit) and LLM-based intelligence (Gemini) to simulate a real-world monitoring system used in production environments.
<img width="1913" height="838" alt="image" src="https://github.com/user-attachments/assets/3cf0c9a3-e0db-47af-83cb-6459058b63a6" />

## Key Features

### Log Explorer
* Filter logs by IP, endpoint, and status code
* Pagination for efficient browsing

### Interactive Dashboard
* Requests over time (time-series visualization)
* Top endpoints analysis
* Status code distribution

### Anomaly Detection
* Detects traffic spikes using statistical methods
* Identifies abnormal request patterns

### AI-Powered Insights
* Automatic summarization of traffic trends
* Natural language Q&A over log metrics

## How It Works

### Batch Processing (PySpark)
* Parses raw web server logs
* Extracts structured data (IP, timestamp, endpoint, status, etc.)
* Computes aggregated metrics

### Frontend (Streamlit)
* Loads preprocessed data
* Provides interactive visualization and filtering

### AI Layer (Gemini)
* Generates insights from metrics
* Answers user queries in natural language

<img width="1847" height="873" alt="image" src="https://github.com/user-attachments/assets/32f117a1-f9a1-40c6-86eb-4071c72ae3cb" />


## Tech Stack
* **PySpark** – Distributed data processing
* **Streamlit** – Interactive dashboard
* **Pandas & Plotly** – Data handling and visualization
* **Google Gemini API** – AI insights and Q&A
* **Python** – Core development

## Live Demo
[https://loganalyst-kushagra-gupta.streamlit.app/]

## Use Case
This system mimics a real-world log monitoring platform, useful for:
* Observability dashboards
* Traffic analysis
* Error monitoring
* AI-assisted debugging

## Conclusion
This project demonstrates the integration of data engineering, analytics, and AI into a unified system, showcasing how modern applications can leverage LLMs for intelligent monitoring.
