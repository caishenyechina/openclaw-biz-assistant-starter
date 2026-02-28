# API Examples

Base URL: `http://127.0.0.1:8011`

## Health
```bash
curl http://127.0.0.1:8011/health
```

## Summarize
```bash
curl -X POST http://127.0.0.1:8011/summarize \
  -H "Content-Type: application/json" \
  -d '{"text":"今天完成客户跟进，发布新仓库，准备明日计划。"}'
```

## Review
```bash
curl -X POST http://127.0.0.1:8011/review \
  -H "Content-Type: application/json" \
  -d '{"done":["发版"],"pending":["录演示"],"tomorrow":["客户A部署"]}'
```

## Voice Script
```bash
curl -X POST http://127.0.0.1:8011/voice-script \
  -H "Content-Type: application/json" \
  -d '{"text":"今天完成了客户跟进和报价模板。"}'
```
