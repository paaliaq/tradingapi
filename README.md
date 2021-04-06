# tradingapi

This repo defines classes for placing trades through various trading apis, among others
Alpaca and Interactive brokers.

## Project Organization

```
├── notebooks               <- Notebooks used for demo purposes
├── src                     <- Source for project
│    └──┰── tradingapi      <- Package of this project
│       ├── base            <- Subpackage defining the contract with all trading APIs
│       ├── alpaca          <- Subpackage for Alpaca trading API
│       └── ig              <- Subpackage for Interactive broker trading API
├── tests                   <- Unit tests for src/
├── .config                 <- All config.json files belong in this folder
├── README.md               <- The top-level README for developers using this project
├── pyproject.toml          <- Specifies all requirements for this project using poetry
├── .gitlab-ci.yml          <- CI pipeline for code and documentation format checks
└── setup.cfg               <- Config file for pipeline
```

## How to run the pipeline linters locally

The pipeline (`.gitlab-ci.yml`) also contains some checks to ensure code quality. You can run these checks locally with the following commands from the main directory. You can also run the commands separately if that's what you prefer.

```shell
poetry run black --check src/ && flake8 src/ && mypy src/ && pydocstyle src/ && darglint src/
```
