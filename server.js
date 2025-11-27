// server.js
const express = require("express");
const cors = require("cors");
const dotenv = require("dotenv");

dotenv.config();

const app = express();
const PORT = process.env.PORT || 4000;

// middleware
app.use(cors());
app.use(express.json({ limit: "10mb" }));

// health check
app.get("/", (req, res) => {
  res.json({
    ok: true,
    message: "Vortex VideoCore backend is alive 👋",
  });
});

// MAIN ROUTE: generate video
app.post("/api/generate-video", async (req, res) => {
  try {
    const { prompt, durationSeconds, resolution } = req.body || {};

    if (!prompt || !prompt.trim()) {
      return res.status(400).json({ error: "Prompt is required." });
    }

    const safeDuration = Number(durationSeconds) || 5;
    const safeResolution = resolution || "720p";

    console.log("🎬 Incoming video request:", {
      prompt,
      duration: safeDuration,
      resolution: safeResolution,
    });

    // 🔧 TODO: plug your REAL video model here (RunPod, Docker, Replicate, etc.)
    // For now we return a dummy clip so frontend works. Later:
    // - Call your model URL
    // - Get back a video URL
    // - Set videoUrl = that URL

    const videoUrl =
      "https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4";

    if (!videoUrl) {
      return res
        .status(500)
        .json({ error: "No video URL returned from video engine." });
    }

    return res.json({
      ok: true,
      videoUrl,
      prompt,
      durationSeconds: safeDuration,
      resolution: safeResolution,
    });
  } catch (err) {
    console.error("❌ Error in /api/generate-video:", err);
    return res.status(500).json({
      error: "Internal server error in videocore backend.",
      details: String(err),
    });
  }
});

app.listen(PORT, () => {
  console.log(
    `✅ Vortex VideoCore backend running on http://localhost:${PORT}`
  );
});