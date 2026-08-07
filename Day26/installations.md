# Building a Flask Application with a Virtual Environment

## 1. Install `virtualenv` (if not already installed)

```bash
pip install virtualenv
```

## 2. Verify the installation

```bash
python -m pip show virtualenv
```

## 3. Create a project directory

```bash
mkdir python_for_web
cd python_for_web
```

## 4. Create a virtual environment

### Windows

```bash
python -m virtualenv venv
```

### macOS / Linux

```bash
virtualenv venv
```

## 5. Activate the virtual environment

### Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
source venv/bin/activate
```

## 6. Check installed packages

```bash
pip freeze
```

The output will be empty because no packages have been installed yet.

## 7. Install Flask

```bash
pip install Flask
```

## 8. Verify installed packages

```bash
pip freeze
```

You should now see Flask and its dependencies listed.

---

## Summary

- Created a project directory named `python_for_web`.
- Created a virtual environment named `venv`.
- Activated the virtual environment.
- Verified that no packages were initially installed using `pip freeze`.
- Installed Flask.
- Confirmed the installation by running `pip freeze` again.
-The Flask project is present on 'python_for_web' folder 
