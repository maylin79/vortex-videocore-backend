import os
import time
import requests
import runpod

VULTR_UPLOAD_URL = os.getenv("VULTR_UPLOAD_URL")  # ex: https://vortexai.studio/upload
VULTR_UPLOAD_KEY = os.getenv("VORTEX_UPLOAD_KEY") # same key as Vultr env var

def handler(event):
    inp = event.get("input", {}) or {}

    # You will send these from Base44/Vultr when real engine is ready
    video_url = inp.get("video_url")   # where to download from
    job_id = inp.get("job_id", str(int(time.time())))

    if not video_url:
        return {"ok": False, "error": "missing video_url"}

    # download
    tmp_path = f"/tmp/{job_id}.mp4"
    r = requests.get(video_url, stream=True, timeout=600)
    r.raise_for_status()
    with open(tmp_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024*1024):
            if chunk:
                f.write(chunk)

    # upload to Vultr
    with open(tmp_path, "rb") as f:
        files = {"file": (f"{job_id}.mp4", f, "video/mp4")}
        resp = requests.post(
            VULTR_UPLOAD_URL,
            files=files,
            params={"key": VULTR_UPLOAD_KEY},
            timeout=600,
        )
    resp.raise_for_status()
    data = resp.json()

    return {"ok": True, "job_id": job_id, "url": data.get("url")}

runpod.serverless.start({"handler": handler})
