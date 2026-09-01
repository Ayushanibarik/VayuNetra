"""
VayuNetra (वायुNetra) - Hugging Face Free Space Entrypoint
Wraps and mounts the FastAPI AI C2 Backend for 100% Free Hosting
"""

import os
import sys
import uvicorn
import gradio as gr

# Ensure root workspace is in sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from backend.main import app as fastapi_app

# Gradio interface for status monitoring on Hugging Face
with gr.Blocks(title="VayuNetra (वायुNetra) AI Backend") as demo:
    gr.Markdown("# 🛡️ VayuNetra (वायुNetra) AI C2 Cloud Backend")
    gr.Markdown("### Tactical Drone Detection, Sensor Fusion & Telemetry WebSocket Hub")
    gr.Markdown("✅ **Status:** Active & Ready for C2 Telemetry Stream")
    gr.Markdown("🌐 **Frontend Console:** [https://vayunetra-eta.vercel.app](https://vayunetra-eta.vercel.app)")

# Mount Gradio interface onto FastAPI app
app = gr.mount_gradio_app(fastapi_app, demo, path="/gradio")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    uvicorn.run(app, host="0.0.0.0", port=port)
