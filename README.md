# spekit-workflow-test

A minimal Python web application that serves a "Hello, World!" greeting.

## Prerequisites

- Python 3.8+
- pip

## Installation

Install dependencies:

```bash
pip install flask
```

Or install all project dependencies:

```bash
pip install -r requirements.txt
```

## Running the App

```bash
python app.py
```

Then open your browser at <http://localhost:5000>.

To use a custom port, set the `PORT` environment variable:

```bash
PORT=8080 python app.py
```

## Running Tests

```bash
pytest tests/
```
