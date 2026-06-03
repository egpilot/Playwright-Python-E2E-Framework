# Enterprise Playwright Python E2E Framework

Production-grade UI + API automation built on **Playwright Python**, **Pytest**, and the **Page Object Model**.

## Features

- Page Object Model with `BasePage` abstraction
- Centralized locator strategy & explicit waits
- Cross-browser: **Chromium / Firefox / WebKit**
- Parallel execution (`pytest-xdist`)
- Auto retries on failure (`pytest-rerunfailures`)
- HTML report (`pytest-html`) + **Allure** reporting
- Screenshot, **video**, and **Playwright trace** capture on failure
- API testing with `requests` + shared auth fixture
- Multi-environment via `dotenv` (`dev / qa / prod`)
- Data-driven via `data/test_data.json`
- CI/CD via GitHub Actions
- Dockerized execution

## Project layout

```
project/
├── pages/        # Page Objects (BasePage + concrete pages)
├── tests/        # smoke / regression / api
├── fixtures/     # browser & api fixtures
├── utils/        # logger, api_client, screenshot, waits
├── config/       # *.env per environment + settings.py
├── data/         # test data (JSON)
├── reports/      # html, allure, screenshots, videos, traces
├── conftest.py
├── pytest.ini
├── requirements.txt
├── Dockerfile / docker-compose.yml
└── .github/workflows/tests.yml
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install --with-deps
```

## Run tests

```bash
pytest                                   # default (qa, chromium, headless)
pytest -n auto                           # parallel
pytest --headed                          # headed mode
pytest --browser-name chromium           # pick a browser
pytest --browser-name firefox
pytest --browser-name webkit
pytest --env qa                          # switch environment (dev/qa/prod)
pytest -m smoke                          # run only smoke
pytest -m regression
pytest tests/smoke/test_google_search.py # single file
pytest tests/smoke/test_duck_duck_search.py # screenshot single file
```

## Reports

- HTML: `reports/report.html`
- Allure raw: `reports/allure-results` → serve with `allure serve reports/allure-results`
- Screenshots: `reports/screenshots/`
- Videos: `reports/videos/`
- Traces (failures): `reports/traces/` → view with `playwright show-trace reports/traces/<file>.zip`

## Docker

```bash
docker compose build
docker compose up
```

## CI

See `.github/workflows/tests.yml` — runs the suite across Chromium, Firefox, WebKit on every push.

## Adding a new page

1. Create `pages/my_page.py` extending `BasePage`.
2. Declare locators as class constants.
3. Expose user-level actions (`login()`, `add_to_cart()`), not raw clicks.
4. Write tests under `tests/smoke/` or `tests/regression/`.
