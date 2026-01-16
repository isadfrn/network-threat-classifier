# Network threat classifier

![Languages used](https://img.shields.io/github/languages/count/isadfrn/network-threat-classifier?style=flat-square)
![Repository size](https://img.shields.io/github/repo-size/isadfrn/network-threat-classifier?style=flat-square)
![Last commit](https://img.shields.io/github/last-commit/isadfrn/network-threat-classifier?style=flat-square)

## About

This repository contains Python scripts for analyzing network traffic data to classify IPs as compromised or non-compromised using a Support Vector Machine (SVM) model and to predict network traffic flows using a Random Forest Regressor model.

This was a project for a Machine Learning class during my Master's degree. The presentation is written in Portuguese and can be accessed [here](./docs/slides.pdf).

## Project Structure

```
network-threat-classifier/
├── src/                    # Python source code
│   ├── preprocessor.py     # Data preprocessing
│   ├── svn.py              # SVM classification
│   └── predictor.py        # Random Forest prediction
├── data/                   # Input data
│   └── data.csv
├── output/                 # Generated files (ignored by git)
│   ├── processed_data.csv
│   ├── roc_curve.png
│   └── prediction_comparison.png
├── docs/                   # Documentation
│   └── slides.pdf
├── run.py                  # Main runner script
├── Makefile                # Makefile for automation
├── requirements.txt        # Python dependencies
└── README.md
```

## Run

Run the complete pipeline with a single command. The script will automatically create a virtual environment, install dependencies, and execute all steps.

**Using Python script (works on all platforms):**

```shell
python run.py
```

**Using Makefile (Linux/Mac, or Windows with Make installed):**

```shell
make
```

Both commands will automatically:

- Create a virtual environment if it doesn't exist
- Install all dependencies from `requirements.txt`
- Run the complete pipeline (preprocessing → classification → prediction)

**Additional Makefile commands:**

```shell
make preprocess  # Data preprocessing only
make classify    # Preprocessing + SVM classification
make predict     # Complete pipeline
make clean       # Remove generated files
make clean-venv  # Remove virtual environment
make help        # Show all available commands
```

## Contributing

This repository is using [Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) and [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/), so if you want to contribute:

- create a branch from develop branch;
- make your contributions;
- open a [Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) to develop branch;
- wait for discussion and future approval;

I thank you in advance for any contribution.

## Status

Finished

## License

[MIT](./LICENSE)
