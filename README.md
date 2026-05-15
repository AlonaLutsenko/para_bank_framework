# ParaBank Test Framework

UI test automation for [ParaBank](https://parabank.parasoft.com/) using **Python 3.11**, **pytest**, and **Selenium**. The codebase separates core helpers (`framework/`), page objects and components (`ui/`), and automated tests (`tests/`).

## Requirements

- Python **3.11**
- **Google Chrome** (for local runs; CI uses the Selenium Chrome standalone image)
- ParaBank test credentials via environment variables (see below)

## Setup

```bash
python -m venv .venv
```

Activate the virtual environment (Windows PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Optional (matches CI HTML reporting):

```bash
pip install pytest-html
```

Create a `.env` file in the **project root** for local runs (see [Credentials](#credentials)).

## Running tests

**Local Chrome** (browser window):

```bash
pytest -v
```

**Headless**:

```bash
pytest -v --headless
```

**Remote WebDriver** (e.g. local Selenium Grid or Docker):

```bash
set SELENIUM_REMOTE_URL=http://localhost:4444/wd/hub
pytest -v --remote --headless --browser=chrome
```

On Linux/macOS, use `export SELENIUM_REMOTE_URL=...` instead of `set`.

**Useful pytest options**

| Option | Description |
|--------|-------------|
| `--browser=chrome` \| `firefox` | Browser (default: `chrome`) |
| `--headless` | Run without a visible window |
| `--remote` | Use `SELENIUM_REMOTE_URL` instead of a local driver |

**Chrome paths (optional)**

If Chrome or ChromeDriver are non-standard, you can set:

- `CHROME_BIN` — path to the Chrome binary  
- `CHROMEDRIVER_PATH` — path to `chromedriver` (when not using `--remote`)

## Reports

- **pytest-html**: add `--html=reports/report.html` (install `pytest-html` first).
- **JUnit**: `--junitxml=pytest-junit.xml`
- **Coverage**: `--cov=framework --cov=ui --cov-report=term`
- **Allure**: `--alluredir=allure-results`, then serve with the [Allure CLI](https://github.com/allure-framework/allure2): `allure serve allure-results`

CI uploads `reports/report.html` and `allure-results` as workflow artifacts.

## Project layout

| Path | Role |
|------|------|
| `framework/` | Configuration, driver factory, wrappers, utilities |
| `ui/` | Page objects and reusable UI components |
| `tests/` | Pytest modules and fixtures |

## Linting and pre-commit

CI runs **black**, **isort**, and **flake8** (see `pyproject.toml` / `.flake8`).

Locally:

```bash
pip install black isort flake8
black --check .
isort --check-only .
flake8 .
```

Optional [pre-commit](https://pre-commit.com/):

```bash
pip install pre-commit
pre-commit install
```

## CI (GitHub Actions)

Workflow **`.github/workflows/ci.yml`** runs on pushes and pull requests to `main`:

1. Lint job: black, isort, flake8  
2. Test job: pytest against **Chrome** via **remote** Selenium (`SELENIUM_REMOTE_URL`), with coverage, JUnit, HTML, and Allure output  

Configure repository secrets (**Settings → Secrets and variables → Actions**) as described in [Credentials](#credentials).

## Credentials

**Never commit real credentials.** Use environment variables or CI secrets only.

Supported user types (each pair is optional; whatever you define becomes available): **`default`**, **`admin`**, **`guest`**.

Environment variable pattern:

- `PARABANK_USERNAME_<TYPE>` and `PARABANK_PASSWORD_<TYPE>` where `<TYPE>` is `DEFAULT`, `ADMIN`, or `GUEST` (uppercase).

Examples:

```env
PARABANK_USERNAME_DEFAULT=your_username
PARABANK_PASSWORD_DEFAULT=your_password
```

Local development: put these in `.env` at the project root (`.env` is gitignored).

GitHub Actions: add secrets **`PARABANK_USERNAME_DEFAULT`** and **`PARABANK_PASSWORD_DEFAULT`** (these are mapped in the workflow). For **`admin`** / **`guest`** users in CI, extend `.github/workflows/ci.yml` to pass the corresponding secret names into the job `env` block.
