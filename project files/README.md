# Electric Motor Temperature Prediction — Run Instructions

From the project root (c:\Users\sreen\Downloads\Electric_Motor_Temperature_Prediction) use PowerShell.

Quick start (recommended):

```powershell
# runs the script that creates the venv, installs dependencies, and starts the app
.\run.ps1
```

Manual steps if you prefer:

```powershell
# create venv
python -m venv .venv

# activate (PowerShell)
.venv\Scripts\Activate.ps1

# upgrade pip and install deps
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# run the app
python Flask\app.py
```

Open http://127.0.0.1:5000/ in your browser.

If you see errors about `python` not found, install Python from https://www.python.org/ and enable "Add to PATH" during installation.