$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $root

$venv = Join-Path $root '.venv'
$py = Join-Path $venv 'Scripts\python.exe'

if (-not (Test-Path $py)) {
    if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
        Write-Error "Python executable not found. Install Python from https://www.python.org/ and ensure 'python' is in PATH."
        exit 1
    }
    Write-Host "Creating virtualenv..."
    python -m venv .venv
}

if (-not (Test-Path $py)) {
    Write-Error "Virtual environment python not found at $py"
    exit 1
}

Write-Host "Upgrading pip and installing requirements..."
& "$py" -m pip install --upgrade pip
& "$py" -m pip install -r requirements.txt

Write-Host "Starting Flask app..."
& "$py" Flask\app.py