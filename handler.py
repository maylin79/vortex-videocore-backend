import os
import time
import runpod

def handler(event):
    inp = event.get("input", {}) or {}
    prompt = inp.get("prompt", "")

    time.sleep(1)

    return {
        "ok": True,
        "message": "VortexAI serverless worker online",
        "prompt": prompt,
        "pod_id": os.environ.get("RUNPOD_POD_ID"),
    }

runpod.serverless.start({"handler": handler})
