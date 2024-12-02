# Network threat classifier

![Languages used](https://img.shields.io/github/languages/count/isadfrn/network-threat-classifier?style=flat-square)
![Repository size](https://img.shields.io/github/repo-size/isadfrn/network-threat-classifier?style=flat-square)
![Last commit](https://img.shields.io/github/last-commit/isadfrn/network-threat-classifier?style=flat-square)

## About

This repository contains Python scripts for analyzing network traffic data to classify IPs as compromised or non-compromised using a Support Vector Machine (SVM) model and predict network traffic flows using a Random Forest Regressor model.

## Run

- Create a virtual env:

```shell
python -m venv venv
```

- Load the virtual env:

```shell
source venv/bin/activate
```

- Install all required packages:

```shell
pip install pandas numpy scikit-learn imbalanced-learn matplotlib seaborn
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
