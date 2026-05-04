import runpod
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("chandra")

logger.info("Handler starting...")

async def handler(job):
    try:
        logger.info(f"Received job: {job['id']}")
        
        input_data = job["input"]
        
        return {
            "status": "success",
            "markdown": "Test OCR - model działa (placeholder). Wyślij prawdziwy obrazek.",
            "json": {"message": "Model Chandra jest gotowy"},
            "raw": "Test"
        }
    except Exception as e:
        logger.error(f"Error: {e}")
        return {"error": str(e)}

runpod.serverless.start({"handler": handler})
