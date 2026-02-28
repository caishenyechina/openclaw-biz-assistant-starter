param(
  [ValidateSet('test','run-api','run-cli')]
  [string]$Task = 'test'
)

if ($Task -eq 'test') {
  python -m pytest -q
}
elseif ($Task -eq 'run-api') {
  python -m uvicorn src.api:app --host 0.0.0.0 --port 8011 --reload
}
elseif ($Task -eq 'run-cli') {
  powershell -ExecutionPolicy Bypass -File .\scripts\run-demo.ps1
}
