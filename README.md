# Whales


This repository contains all the code we wrote for completing coursework and 
cyberstorm for CSC-442/CYEN-301 Intro to Cyber Security at Louisiana Tech 
University.

# Programs and Cyberstorm

In this repo, each directory represents a separate program.

# Installing dependencies

To install dependencies, execute `pip install -r requirements.txt` inside the
project root.

# Testing

Install dependencies: `pip install -r requirements.txt`

To test our code, you can simply run `pytest` to run any defined unit tests.

To view test coverage, you can execute the following:

```bash
pytest --doctest-modules --cov=. --cov-report=html
```

You will find the generated HTML report in `htmlcov/index.html`.

