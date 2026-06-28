$Config="$env:APPDATA\Claude\claude_desktop_config.json"
if(Test-Path $Config){
    $Date=Get-Date -Format "yyyyMMdd-HHmmss"
    $Folder="backup\$Date"
    New-Item -ItemType Directory -Force $Folder | Out-Null
    Copy-Item $Config $Folder
    Write-Host "Backup creado."
}
