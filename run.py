#!/usr/bin/env python3
import sys
import subprocess
import platform
from pathlib import Path

def get_venv_python(project_root):
    """Get the path to the virtual environment's Python executable."""
    if platform.system() == "Windows":
        return project_root / "venv" / "Scripts" / "python.exe"
    else:
        return project_root / "venv" / "bin" / "python"

def setup_venv(project_root):
    """Create virtual environment if it doesn't exist."""
    venv_path = project_root / "venv"
    venv_python = get_venv_python(project_root)
    
    if venv_path.exists() and venv_python.exists():
        print("[OK] Virtual environment already exists")
        return venv_python
    
    print("Creating virtual environment...")
    try:
        subprocess.run(
            [sys.executable, "-m", "venv", str(venv_path)],
            check=True,
            cwd=project_root
        )
        print("[OK] Virtual environment created successfully")
        return venv_python
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to create virtual environment: {e}")
        sys.exit(1)

def install_dependencies(venv_python, project_root):
    """Install dependencies from requirements.txt."""
    requirements_file = project_root / "requirements.txt"
    
    if not requirements_file.exists():
        print("[ERROR] requirements.txt not found!")
        sys.exit(1)
    
    print("Installing dependencies from requirements.txt...")
    try:
        subprocess.run(
            [str(venv_python), "-m", "pip", "install", "--upgrade", "pip"],
            check=True,
            cwd=project_root
        )
        subprocess.run(
            [str(venv_python), "-m", "pip", "install", "-r", str(requirements_file)],
            check=True,
            cwd=project_root
        )
        print("[OK] Dependencies installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to install dependencies: {e}")
        sys.exit(1)

def run_script(venv_python, script_name, description, project_root):
    """Run a Python script and handle errors."""
    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print(f"Script: {script_name}")
    print(f"{'='*60}\n")
    
    script_path = project_root / 'src' / script_name
    
    if not script_path.exists():
        print(f"ERROR: {script_name} not found!")
        return False
    
    try:
        result = subprocess.run(
            [str(venv_python), str(script_path)],
            check=True,
            cwd=project_root
        )
        print(f"\n[OK] {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n[ERROR] {description} failed with exit code {e.returncode}")
        return False
    except Exception as e:
        print(f"\n[ERROR] {description} failed with error: {e}")
        return False

def main():
    """Main execution function."""
    print("="*60)
    print("Network Threat Classifier - Pipeline Execution")
    print("="*60)
    
    project_root = Path(__file__).parent
    
    print("\n" + "="*60)
    print("Setting up virtual environment...")
    print("="*60)
    venv_python = setup_venv(project_root)
    
    print("\n" + "="*60)
    print("Installing dependencies...")
    print("="*60)
    install_dependencies(venv_python, project_root)
    
    data_file = project_root / 'data' / 'data.csv'
    if not data_file.exists():
        print("\nERROR: data.csv not found!")
        print("Please ensure data.csv is in the data/ directory.")
        sys.exit(1)
    
    print("\n" + "="*60)
    print("Running pipeline...")
    print("="*60)
    
    scripts = [
        ('preprocessor.py', 'Data Preprocessing'),
        ('svn.py', 'SVM Classification'),
        ('predictor.py', 'Random Forest Prediction')
    ]
    
    for script, description in scripts:
        success = run_script(venv_python, script, description, project_root)
        if not success:
            print(f"\nPipeline stopped due to error in {description}")
            sys.exit(1)
    
    print("\n" + "="*60)
    print("Pipeline completed successfully!")
    print("="*60)
    print("\nGenerated files:")
    print("  - output/processed_data.csv")
    print("  - output/roc_curve.png")
    print("  - output/prediction_comparison.png")
    print("="*60)

if __name__ == "__main__":
    main()
