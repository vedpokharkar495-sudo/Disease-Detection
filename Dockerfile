FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY .. .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "frontend/app.py", "--server.address=0.0.0.0"]