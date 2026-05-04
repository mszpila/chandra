FROM vllm/vllm-openai:latest

# Install Chandra package
RUN pip install chandra-ocr

# Optional: pre-install other dependencies if needed
# RUN pip install chandra-ocr[hf]

EXPOSE 8000

# This command starts the vLLM server (same as chandra_vllm)
CMD ["python", "-m", "vllm.entrypoints.openai.api_server", \
     "--model", "datalab-to/chandra-ocr-2", \
     "--host", "0.0.0.0", \
     "--port", "8000", \
     "--dtype", "bfloat16", \
     "--gpu-memory-utilization", "0.85", \
     "--max-model-len", "16384"]
