import csv
import datetime as dt
from pathlib import Path

CSV_PATH = Path('docs/LEAD-TRACKER.csv')
OUT_PATH = Path('output/today-followups.md')


def load_rows(path: Path):
    if not path.exists():
        return []
    with path.open('r', encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


def due_today(rows):
    today = dt.date.today().isoformat()
    out = []
    for r in rows:
        if (r.get('status') or '').lower() == 'closed':
            continue
        nxt = (r.get('next_followup') or '').strip()
        if nxt and nxt <= today:
            out.append(r)
    return out


def render(rows):
    lines = [f"# 今日应跟进线索（{dt.date.today().isoformat()}）", ""]
    if not rows:
        lines.append("今天无到期跟进。")
        return '\n'.join(lines)

    for i, r in enumerate(rows, 1):
        lines.append(f"{i}. {r.get('lead_name','')} | {r.get('project','')} | 阶段: {r.get('stage','')}")
        lines.append(f"   - 需求: {r.get('need','')}")
        lines.append(f"   - 预算: {r.get('budget','')}")
        lines.append(f"   - 建议动作: 发送 Day1/Day3/Day7 跟进模板")
        lines.append(f"   - 备注: {r.get('notes','')}")
        lines.append("")
    return '\n'.join(lines)


def main():
    rows = load_rows(CSV_PATH)
    due = due_today(rows)
    content = render(due)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(content, encoding='utf-8')
    print(content)


if __name__ == '__main__':
    main()
