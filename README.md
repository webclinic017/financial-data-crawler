<div align="center">

  ![logo](https://github.com/eshinhw/financial-data-crawler/assets/41933169/82a0940b-697c-4a29-9dc5-e26756720e15)

</div>

<div align="center">
  
  ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/eshinhw/financial-data-crawler)
  ![GitHub issues](https://img.shields.io/github/issues/eshinhw/financial-data-crawler)
  ![GitHub pull requests](https://img.shields.io/github/issues-pr/eshinhw/financial-data-crawler)

</div>

# Available Data

- Global Stock Tickers
  - USA: NYSE, NASDAQ, AMEX

# Project Development Setup

## Virtual Environment Setup

Install `virtualenv` if not installed in your machine.

```
pip install virtualenv
```

Go to the project directory and initialize it.

```
cd my-project
virtualenv venv
```

Activate the virtual environment.

```
source venv/bin/activate
```

Deactivate the virtual environment.

```
deactivate
```

**Important**: Remember to add venv to your project's `.gitignore` file so you don't include all of that in your source code.

## Database Setup

If running the project locally, local DB setup should be completed in `database.ini`.

Run `python tickers.py` to retrieve US ticker data and store them inside the local database set up above.
