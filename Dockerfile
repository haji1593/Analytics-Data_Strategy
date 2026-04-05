FROM python:3.12-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY dashboard.py .
COPY .streamlit/ .streamlit/

# Expose port
EXPOSE 8513

# Run Streamlit
CMD ["streamlit", "run", "dashboard.py", "--server.port=8513", "--server.address=0.0.0.0"]
