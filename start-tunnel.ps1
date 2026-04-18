# start-tunnel.ps1
# Usage: powershell -ExecutionPolicy Bypass -File .\start-tunnel.ps1

# Ensure user bin is in PATH for this run
$env:PATH += ";" + $env:USERPROFILE + "\bin"

# settings
$APP_DIR = "C:\Users\walki\OneDrive\Desktop\PXL"
$STREAMLIT_CMD = "streamlit"
$STREAMLIT_ARGS = "run app.py --server.address=0.0.0.0 --server.port=8501"
$CLOUDFLARED_EXE = Join-Path $env:USERPROFILE "bin\cloudflared.exe"
$CLOUDFLARED_ARGS = "tunnel --url http://localhost:8501"

# move to project directory
Set-Location $APP_DIR

# start Streamlit in a new window (detached)
Write-Output "Starting Streamlit..."
Start-Process -FilePath $STREAMLIT_CMD -ArgumentList $STREAMLIT_ARGS -WorkingDirectory $APP_DIR

Start-Sleep -Seconds 2

# start cloudflared (detached)
Write-Output "Starting cloudflared tunnel..."
Start-Process -FilePath $CLOUDFLARED_EXE -ArgumentList $CLOUDFLARED_ARGS -WorkingDirectory $APP_DIR

Write-Output 'Started. Give Streamlit ~5-10s to boot, then visit the cloudflared URL printed in the cloudflared terminal (or check cloudflared logs).'
Write-Output 'To stop: use Task Manager or run `Get-Process cloudflared,streamlit | Stop-Process`'
