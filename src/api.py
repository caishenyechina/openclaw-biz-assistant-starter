from pathlib import Path
import json

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator

from src.biz_assistant import summarize, build_daily_review, voice_script

app = FastAPI(title="Biz Assistant API", version="0.3.0")


class TextRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=5000)

    @field_validator("text")
    @classmethod
    def text_not_blank(cls, v: str):
        if not v.strip():
            raise ValueError("text must not be blank")
        return v


class ReviewRequest(BaseModel):
    done: list[str] = Field(default_factory=list)
    pending: list[str] = Field(default_factory=list)
    tomorrow: list[str] = Field(default_factory=list)


@app.get("/health")
def health():
    return {"ok": True, "service": "biz-assistant", "version": "0.3.0"}


@app.post("/summarize")
def summarize_text(req: TextRequest):
    try:
        tmp = Path("output/tmp_input.txt")
        tmp.parent.mkdir(parents=True, exist_ok=True)
        tmp.write_text(req.text, encoding="utf-8")
        return {"points": summarize(tmp, 5)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"summarize failed: {e}")


@app.post("/review")
def review(req: ReviewRequest):
    try:
        tmp = Path("output/tmp_review.json")
        tmp.parent.mkdir(parents=True, exist_ok=True)
        tmp.write_text(json.dumps(req.model_dump(), ensure_ascii=False), encoding="utf-8")
        return {"review": build_daily_review(tmp)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"review failed: {e}")


@app.post("/voice-script")
def voice(req: TextRequest):
    try:
        tmp = Path("output/tmp_voice.txt")
        tmp.parent.mkdir(parents=True, exist_ok=True)
        tmp.write_text(req.text, encoding="utf-8")
        return {"script": voice_script(tmp)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"voice-script failed: {e}")
