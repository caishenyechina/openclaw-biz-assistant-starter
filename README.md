# OpenClaw Biz Assistant Starter

> 10 分钟搭好你的「老板助手」：消息汇总 + 提醒 + 日报。

一个面向个体创业者/小团队的 OpenClaw 模板仓库。
目标是：**先跑起来，再逐步升级**。

---

## 你会得到什么（MVP）

- ✅ 每日摘要（把当天关键消息压缩成一段）
- ✅ 定时提醒（支持一次性与周期提醒）
- ✅ 语音播报（TTS）
- ✅ 可扩展结构（后续接 Telegram/飞书/企业微信）

---

## 适合谁

- 想把“零碎提醒 + 日报”自动化的人
- 不想从零配置 OpenClaw 的人
- 想做自己的 AI 助手产品雏形的人

---

## 3 分钟跑起来（最小流程）

1. 在 EasyClaw Desktop 打开本项目目录
2. 把 `docs/SETUP-CHECKLIST.md` 从上到下做一遍
3. 用 `docs/OPS-RUNBOOK.md` 里的“日常命令清单”测试

> 你不需要先理解全部原理，先让它跑起来。

---

## 代码能力（已内置）

### 启动 API（本地）

```powershell
pip install -r requirements.txt
uvicorn src.api:app --reload --port 8011
```

- 健康检查：`GET http://127.0.0.1:8011/health`
- Swagger：`http://127.0.0.1:8011/docs`


- `src/biz_assistant.py`
  - `summarize`：把日志压缩成重点
  - `review`：从 JSON 生成复盘文本
  - `reminder`：输出提醒 payload
  - `voice-script`：生成语音播报稿
- `scripts/run-demo.ps1`：一键演示命令

示例：

```powershell
python .\src\biz_assistant.py summarize --input .\examples\day-log.example.txt --max 3
python .\src\biz_assistant.py review --input .\examples\review-data.example.json
```

---

## 项目结构

```txt
openclaw-biz-assistant-starter/
├─ README.md
├─ docs/
│  ├─ SETUP-CHECKLIST.md
│  ├─ OPS-RUNBOOK.md
│  └─ SALES-PAGE-COPY.md
├─ examples/
│  ├─ reminder-prompts.md
│  └─ daily-summary-template.md
└─ scripts/
   └─ quickstart-notes.md
```

---

## 免费版 vs Pro（规划）

| 功能 | Free | Pro |
|---|---|---|
| 每日摘要 | ✅ | ✅ |
| 基础提醒 | ✅ | ✅ |
| 语音播报 | ✅ | ✅ |
| 多渠道推送（Telegram/飞书） | ❌ | ✅ |
| 高级重试/日志看板 | ❌ | ✅ |
| 代部署服务 | ❌ | ✅ |

---

## 交付/变现建议（你可以直接照做）

- 模板包：¥99
- Pro 模板：¥299
- 代部署：¥999
- 顾问服务：¥1999/2小时

---

## Roadmap（接下来 14 天）

- Day 1-2：跑通提醒 + 日报 + TTS
- Day 3-4：补文档和演示截图
- Day 5-7：发布 V0.1
- Day 8-10：做 Pro 清单页
- Day 11-14：拿第一个付费用户

---

## 现在就开始（按这个顺序）

1. 看 `docs/SETUP-CHECKLIST.md`（先跑起来）
2. 看 `docs/OFFER-PACKAGES.md`（直接报价）
3. 看 `docs/LAUNCH-POSTS.md`（直接发内容）
4. 看 `docs/7DAY-EXECUTION.md`（每天执行）

---

## 快速部署（Docker）

```bash
docker build -t biz-assistant-starter .
docker run --rm -p 8011:8011 biz-assistant-starter
```

更多 API 调用示例见：`docs/API-EXAMPLES.md`

成交资料：
- `docs/QUOTE-TEMPLATE.md`
- `docs/CONTRACT-LITE.md`
- `docs/DELIVERY-REPORT.md`

自动成交推进：
- `docs/LEAD-TRACKER.md`
- `docs/FOLLOW-UP-MESSAGES.md`
- `docs/NO-REPLY-NUDGE.md`

转化增强：
- `docs/FAQ.md`
- `docs/COOP-FLOW.md`

销售中控（半自动）：
- `docs/LEAD-TRACKER.csv`
- `scripts/followup_engine.py`
- `scripts/run-sales-control.ps1`
- `docs/DAILY-SALES-REPORT-TEMPLATE.md`

---

## 关联仓库（推荐一起看）

- China Market Watchdog  
  https://github.com/caishenyechina/china-market-watchdog
- Content Automation Pipeline CN  
  https://github.com/caishenyechina/content-automation-pipeline-cn

---

## 联系方式 / 购买

- Email：4553377@qq.com
- QQ：4553377

可直接邮件/QQ 留言：
- 你要模板版 / Pro 版 / 代部署
- 你的使用场景（个人、团队、客户交付）

---

## License

MIT（如需商用部署支持，联系作者）。
