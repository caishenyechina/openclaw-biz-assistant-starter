import argparse
import datetime as dt
import json
import re
from pathlib import Path


def split_sentences(text: str):
    # Robust split on common sentence punctuation for CN/EN text
    parts = re.split(r"[。！？!?\.]+|\n+", text.strip())
    return [p.strip() for p in parts if p.strip()]


def summarize(input_path: Path, max_points: int = 5):
    if max_points <= 0:
        raise ValueError("max_points must be > 0")
    text = input_path.read_text(encoding="utf-8")
    lines = split_sentences(text)
    points = lines[:max_points]
    return points


def build_daily_review(input_path: Path):
    data = json.loads(input_path.read_text(encoding="utf-8"))
    done = data.get("done", [])
    pending = data.get("pending", [])
    tomorrow = data.get("tomorrow", [])

    out = []
    out.append("# 今日复盘")
    out.append("\n## 已完成")
    out.extend([f"- {x}" for x in done] or ["- 无"])
    out.append("\n## 未完成")
    out.extend([f"- {x}" for x in pending] or ["- 无"])
    out.append("\n## 明日优先")
    out.extend([f"- {x}" for x in tomorrow] or ["- 无"])
    out.append(f"\n生成时间：{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    return "\n".join(out)


def reminder_payload(text: str, fire_at: str):
    if not text.strip():
        raise ValueError("text must not be empty")
    # best-effort validation for ISO datetime
    dt.datetime.fromisoformat(fire_at.replace("Z", "+00:00"))
    return {
        "kind": "systemEvent",
        "text": f"【提醒】{text}",
        "at": fire_at,
    }


def voice_script(input_path: Path):
    points = summarize(input_path, max_points=3)
    body = "；".join(points)
    return f"今日重点如下：{body}。以上，记得按优先级推进。"


def main():
    parser = argparse.ArgumentParser(description="Biz assistant helper scripts")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_sum = sub.add_parser("summarize")
    p_sum.add_argument("--input", required=True)
    p_sum.add_argument("--max", type=int, default=5)

    p_review = sub.add_parser("review")
    p_review.add_argument("--input", required=True)

    p_rem = sub.add_parser("reminder")
    p_rem.add_argument("--text", required=True)
    p_rem.add_argument("--at", required=True, help="ISO time")

    p_voice = sub.add_parser("voice-script")
    p_voice.add_argument("--input", required=True)

    args = parser.parse_args()

    if args.cmd == "summarize":
        points = summarize(Path(args.input), args.max)
        for i, p in enumerate(points, 1):
            print(f"{i}. {p}")
    elif args.cmd == "review":
        print(build_daily_review(Path(args.input)))
    elif args.cmd == "reminder":
        print(json.dumps(reminder_payload(args.text, args.at), ensure_ascii=False, indent=2))
    elif args.cmd == "voice-script":
        print(voice_script(Path(args.input)))


if __name__ == "__main__":
    main()
