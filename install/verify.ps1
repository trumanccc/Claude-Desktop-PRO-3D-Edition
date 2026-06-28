Write-Host ""
Write-Host "Claude Desktop PRO 3D"
Write-Host "======================"
function Test-Program {
    param($Program)
    if (Get-Command $Program -ErrorAction SilentlyContinue) {
        Write-Host "[ OK ] $Program"
    } else {
        Write-Host "[FAIL] $Program"
    }
}
Test-Program git
Test-Program python
Test-Program node
Test-Program npm
Test-Program npx
