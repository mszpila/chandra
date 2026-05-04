FROM vllm/vllm-openai:latest

WORKDIR /app

# Instalujemy Chandra + zależności
RUN pip install chandra-ocr

# RunPod Serverless handler
COPY handler.py /app/handler.py

EXPOSE 8000

# Uruchamiamy przez RunPod handler (nie bezpośrednio vllm)
CMD ["python", "/app/handler.py"]
