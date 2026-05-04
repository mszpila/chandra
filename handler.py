import runpod
import base64
from PIL import Image
from io import BytesIO
import logging
from chandra.model import InferenceManager
from chandra.model.schema import BatchInputItem

logging.basicConfig(level=logging.INFO)

manager = None

async def handler(job):
    global manager
    try:
        if manager is None:
            manager = InferenceManager(method="vllm")

        input_data = job["input"]

        # Obsługa base64 (tak jak w Twoim kodzie)
        if "base64" in input_data or "image" in input_data:
            b64 = input_data.get("base64") or input_data.get("image")
            if b64.startswith("data:"):
                b64 = b64.split(",")[1]
            img_bytes = base64.b64decode(b64)
            image = Image.open(BytesIO(img_bytes))
        else:
            return {"error": "No image/base64 provided"}

        # Prompt typu ocr_layout – najlepszy do struktury
        batch = [BatchInputItem(image=image, prompt_type="ocr_layout")]
        
        results = manager.generate(batch)
        result = results[0]

        # Zwracamy OBIE wersje
        return {
            "markdown": result.markdown,           # czytelny tekst + layout
            "json": result.to_dict(),              # pełna struktura (blocks, coords itd.)
            "raw": result.raw,                     # jak chcesz
            "status": "success"
        }

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return {"error": str(e)}

runpod.serverless.start({"handler": handler})
