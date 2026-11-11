## Neural Avalanches
Analysis of neuronal avalanches and criticality in in vitro neural networks.

## Goal
Investigate whether in vitro neural cultures operate near a critical point, by:

    1. Detecting avalanches from multielectrode array (MEA) recordings.
    2. Estimating critical exponents (size and duration distributions).
    3. Comparing with theoretical universality classes (Manna, directed percolation, mean-field).

## Status
🚧 Work in progress. Project setup phase.

## Setup
git clone git@github.com:danielfdez-ds/neural-avalanches.gitcd neural-avalanchesuv sync

## Project structure
```
neural-avalanches/├── data/           # raw + processed (not in git)
                  ├── notebooks/      # exploratory analysis
                  ├── src/neural_avalanches/  # importable package
                  ├── tests/          # unit tests
                  ├── scripts/        # CLI entry points
                  └── pyproject.toml  # dependencies and config
```
## License
MIT — see [LICENSE](LICENSE).