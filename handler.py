print("🚀 BOOT: handler.py started")

import sys
sys.stdout.flush()  # Good for seeing early prints

import os
import time
import runpod

def handler(event):
    inp = event.get("input", {}) or {}
    prompt = (inp.get("prompt") or "").strip()

    if not prompt:
        return {"ok": False, "error": "Missing prompt"}

    # For now: test response only (no video yet)
    return {
        "ok": True,
        "mode": "text2video",
        "message": "Text-to-video worker online (test mode)",
        "prompt": prompt,
        "pod_id": os.environ.get("RUNPOD_POD_ID"),
        "ts": int(time.time())
    }

if __name__ == "__main__":
    print("✅ BOOT: calling runpod.serverless.start")
    sys.stdout.flush()
    runpod.serverless.start({"handler": handler})
runpod.serverless.start({"handler": handler})
