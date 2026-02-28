from pathlib import Path
import tempfile
import json

from src.biz_assistant import summarize, build_daily_review, reminder_payload, voice_script


def test_summarize_basic():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "in.txt"
        p.write_text("第一句。第二句。第三句。", encoding="utf-8")
        out = summarize(p, max_points=2)
        assert len(out) == 2


def test_review_basic():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "r.json"
        p.write_text(json.dumps({"done": ["A"], "pending": ["B"], "tomorrow": ["C"]}, ensure_ascii=False), encoding="utf-8")
        out = build_daily_review(p)
        assert "已完成" in out and "未完成" in out and "明日优先" in out


def test_reminder_payload():
    payload = reminder_payload("喝水", "2026-03-01T10:00:00+08:00")
    assert payload["kind"] == "systemEvent"
    assert "提醒" in payload["text"]


def test_voice_script():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "v.txt"
        p.write_text("今天完成了报价。明天交付。", encoding="utf-8")
        out = voice_script(p)
        assert "今日重点如下" in out
