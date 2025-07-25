FROM python:3.9-slim

WORKDIR /app

COPY . .

# Install required Python package
RUN pip install PyMuPDF

# Ensure output directory exists in the container
RUN mkdir -p output

# Run the Python script
ENTRYPOINT ["python", "extractor.py"]
