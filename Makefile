ifeq ($(OS),Windows_NT)
    PYTHON := venv\Scripts\python.exe
    PIP := venv\Scripts\pip.exe
    RM := del /Q
else
    PYTHON := venv/bin/python
    PIP := venv/bin/pip
    RM := rm -f
endif

.PHONY: all venv install preprocess classify predict clean help
all: venv install preprocess classify predict
venv:
	@echo "============================================================"
	@echo "Setting up virtual environment..."
	@echo "============================================================"
	@if [ ! -d "venv" ]; then \
		echo "Creating virtual environment..."; \
		python -m venv venv; \
		echo "✓ Virtual environment created"; \
	else \
		echo "✓ Virtual environment already exists"; \
	fi

install: venv
	@echo "============================================================"
	@echo "Installing dependencies..."
	@echo "============================================================"
	@$(PYTHON) -m pip install --upgrade pip
	@$(PYTHON) -m pip install -r requirements.txt
	@echo "✓ Dependencies installed"

preprocess: install
	@echo "============================================================"
	@echo "Running: Data Preprocessing"
	@echo "============================================================"
	@$(PYTHON) src/preprocessor.py

classify: preprocess
	@echo "============================================================"
	@echo "Running: SVM Classification"
	@echo "============================================================"
	@$(PYTHON) src/svn.py

predict: classify
	@echo "============================================================"
	@echo "Running: Random Forest Prediction"
	@echo "============================================================"
	@$(PYTHON) src/predictor.py

clean:
	@echo "Cleaning generated files..."
ifeq ($(OS),Windows_NT)
	@if exist output\processed_data.csv $(RM) output\processed_data.csv
	@if exist output\roc_curve.png $(RM) output\roc_curve.png
	@if exist output\prediction_comparison.png $(RM) output\prediction_comparison.png
else
	@$(RM) output/processed_data.csv output/roc_curve.png output/prediction_comparison.png
endif
	@echo "Clean complete!"

clean-venv:
	@echo "Removing virtual environment..."
ifeq ($(OS),Windows_NT)
	@if exist venv rmdir /s /q venv
else
	@rm -rf venv
endif
	@echo "Virtual environment removed!"

help:
	@echo "Network Threat Classifier - Makefile"
	@echo ""
	@echo "Available targets:"
	@echo "  make all         - Setup venv, install deps, and run complete pipeline (default)"
	@echo "  make venv        - Create virtual environment"
	@echo "  make install     - Install dependencies from requirements.txt"
	@echo "  make preprocess  - Run data preprocessing only"
	@echo "  make classify      - Run preprocessing + SVM classification"
	@echo "  make predict     - Run complete pipeline (preprocess + classify + predict)"
	@echo "  make clean       - Remove generated files"
	@echo "  make clean-venv  - Remove virtual environment"
	@echo "  make help        - Show this help message"
	@echo ""
	@echo "Note: On Windows, you may need to install Make or use 'python run.py' instead"
