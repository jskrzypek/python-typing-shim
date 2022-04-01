# Python Package Template

Template git repository for creating Python packages. Includes the a sample project structure, linting, type checks, unit tests, formatting, and continuous integration.

## Installation

Clone the repository.

```bash
git clone https://github.com/f4str/python-package-template
```

Change directories into the cloned repository.

```bash
cd python-package-template
```

Install Python and create a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dev dependencies using pip.

```bash
pip install -e .[dev]
```

## Development

The `tox` library is used to run all tests and code formatting. This is automatically installed with the dev requirements. The available options are as follows.

* Run linting checks using `flake8`.

    ```bash
    tox -e lint
    ```

* Run type checks using `mypy`.

    ```bash
    tox -e type
    ```

* Run unit tests `pytest`.

    ```bash
    tox -e test
    ```

* Run all three of the tests above.

    ```bash
    tox
    ```

* Format the code using `black` and `isort` to comply with linting conventions.

    ```bash
    tox -e format
    ```

Upon pull request, merge, or push to the `master` branch, the three tests with `tox` will be run using GitHub Actions. The workflow will fail if any of the tests fail. See `.github/workflows/python-package.yml` for more information on how the CI works.
