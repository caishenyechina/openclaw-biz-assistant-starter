$date = Get-Date -Format "yyyy-MM-dd"
$out = "RELEASE-NOTES-$date.md"
$log = git log --pretty=format:"- %s" -n 15
$content = @"
# Release Notes ($date)

## Highlights
$log

## Verification
- [ ] tests passed
- [ ] API health checked
- [ ] README updated
"@
Set-Content -Path $out -Value $content -Encoding UTF8
Write-Host "Generated $out"
