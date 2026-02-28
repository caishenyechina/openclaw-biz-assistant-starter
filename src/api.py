from fastapi import FastAPI
from pydantic import BaseModel

from biz_assistant import summarize, build_daily_review, voice_script
from pathlib import Path

app = FastAPI(title="Biz Assistant API", version="0.2.0")


class TextRequest(BaseModel):
    text: str


class ReviewRequest(BaseModel):
    done: list[str] = []
    pending: list[str] = []
    tomorrow: list[str] = []


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/summarize")
def summarize_text(req: TextRequest):
    tmp = Path("output/tmp_input.txt")
    tmp.parent.mkdir(parents=True, exist_ok=True)
    tmp.write_text(req.text, encoding="utf-8")
    return {"points": summarize(tmp, 5)}


@app.post("/review")
def review(req: ReviewRequest):
    import json
    tmp = Path("output/tmp_review.json")
    tmp.parent.mkdir(parents=True, exist_ok=True)
    tmp.write_text(json.dumps(req.model_dump(), ensure_ascii=False), encoding="utf-8")
    return {"review": build_daily_review(tmp)}


@app.post("/voice-script")
def voice(req: TextRequest):
    tmp = Path("output/tmp_voice.txt")
    tmp.parent.mkdir(parents=True, exist_ok=True)
    tmp.write_text(req.text, encoding="utf-8")
    return {"script": voice_script(tmp)}
