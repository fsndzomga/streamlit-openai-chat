#!/bin/bash

# Run FastAPI in the background
uvicorn backend:app --host 0.0.0.0 --port 8000 &

# Run Streamlit on the default port 8501
streamlit run frontend.py --server.port 8501 --server.address 0.0.0.0
