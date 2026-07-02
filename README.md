# Python Playwright BDD Framework

This repository contains a production-ready Python automation framework built with Playwright, pytest, and Behave using a Page Object Model (POM) design.

## Project Goals
- Support UI automation with Playwright.
- Use Behave for BDD-style feature files and step definitions.
- Keep reusable page-object logic in one place.
- Produce HTML reports, screenshots, and logs automatically.
- Support QA/UAT/PROD-style environment configuration.

## Folder Structure
- config/: environment configuration and shared settings.
- features/: feature files and step definitions.
- locators/: locator definitions for pages.
- pages/: page object classes.
- testdata/: input files and sample data.
- utils/: reusable helpers.
- reports/: generated HTML and XML reports.
- screenshots/: failure and validation screenshots.
- logs/: runtime logs.
- hooks/: custom hooks for Behave (if needed later).
- tests/: pure pytest-based tests.

## Key Files
- requirements.txt: Python dependencies.
- pytest.ini: pytest defaults and reporting.
- behave.ini: Behave execution options.
- playwright.config.py: Playwright defaults.
- environment.py: Behave hooks.
- base_page.py: reusable page actions.
- browser_manager.py: browser lifecycle management.
- config_reader.py: environment-aware config loading.
- logger.py: centralized logging.
- constants.py: shared constants.
- helpers.py: utility helpers.
- conftest.py: pytest fixtures.

## Environment Support
Create environment files in config/environments/ such as:
- qa.env
- uat.env
- prod.env

Example:
```env
BASE_URL=https://www.saucedemo.com
PLAYWRIGHT_BROWSER=chromium
HEADLESS=true
DEFAULT_TIMEOUT=15000
```

## Running Tests
### Behave
```bash
behave
```

### Pytest
```bash
pytest
```

## Reports
- HTML report: reports/pytest-report.html
- Behave XML report: reports/behave-report.xml
- Screenshots: screenshots/
- Logs: logs/

## Adding New Tests
1. Add a feature file under features/.
2. Create or update the matching step definition under features/steps/.
3. Add page-object methods in pages/.
4. Keep test data in testdata/.
5. Run the suite again.

## GitHub Actions CI
A sample workflow is available in .github/workflows/ci.yml.
