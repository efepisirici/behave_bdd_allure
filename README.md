# Automated Testing Framework

This repository contains an automated testing framework designed for web and mobile application testing. It utilizes GitHub Actions for CI/CD integration and BrowserStack for real device and emulator testing. The framework is structured using coding principles like **Conventional Commits**, **Gherkin Scenarios**, **Page Object Model (POM)**, and **Arch-42** design.

## Key Features

- **CI/CD Integration with GitHub Actions:**
  - Automated tests are triggered on pushes and pull requests to the `master` branch.
  - Multi-stage workflow including Docker build, testing, and deployment.
- **Dockerized Testing Environment:**
  - Ensures consistent test environments.
  - Tests are executed inside Docker containers.
- **Cross-Platform Testing:**
  - Supports testing on real devices and emulators via BrowserStack.
  - Ensures compatibility across various devices and browsers.
- **Allure Reporting with History Tracking:**
  - Generates detailed test reports using Allure.
  - Maintains historical data for trend analysis.
- **Continuous Deployment of Test Reports:**
  - Allure reports are automatically deployed to the `main` branch.
  - Utilizes GitHub Pages for easy access to the latest test results.
- **Manual and Automated Tests Management:**
  - Manual tests are tracked and managed through Jira and Zephyr.
  - Supports behavior-driven development (BDD) with Gherkin Scenarios.

## Framework Structure

The framework adheres to best practices and design principles:

- **Conventional Commits:** Ensures consistent and meaningful commit messages.
- **Gherkin Scenarios:** Tests are written in Gherkin syntax for clarity.
- **Page Object Model (POM):** Enhances maintainability and scalability.
- **Arch-42 Design:** Provides a structured approach to architecture documentation.
- **Test Management:** Jira and Zephyr are used for managing manual tests and reporting.

## Technologies Used

- **Python 3.9:** Primary programming language.
- **Behave:** BDD framework for Python.
- **Selenium WebDriver:** For browser automation.
- **BrowserStack:** Cloud platform for cross-browser testing.
- **GitHub Actions:** For CI/CD automation.
- **Docker:** Containerization of the test environment.
- **Allure Framework:** For generating test reports.

## Continuous Integration and Deployment (CI/CD)

The CI/CD pipeline is defined in the `.github/workflows/ci.yaml` file. It is triggered on every push and pull request to the `master` branch.

### Pipeline Overview

1. **Docker Build Job (`docker_build`):**
   - **Checkout Code:** Retrieves the latest code from the repository.
   - **Build Docker Image:** Builds an image tagged `ci-pipeline` from the Dockerfile.
   - **Run Tests in Docker:** Executes tests inside the Docker container, exporting results to `features/reports`.

2. **Test Job (`test`):**
   - **Environment Setup:**
     - Sets up Python 3.9.
     - Installs Chrome dependencies for Selenium.
   - **Install Python Dependencies:** Installs required Python packages.
   - **Install Allure CLI Manually:** Downloads and sets up Allure for report generation.
   - **Prepare Allure Directories:** Creates directories for results and history.
   - **Retrieve Allure History:**
     - Fetches previous history from `allure-history-branch`.
     - Merges it to maintain historical trends.
   - **Run Tests and Generate Results:**
     - Executes tests using Behave.
     - Generates Allure results.
   - **Generate Allure Report:** Produces the HTML report.
   - **Upload Report Artifact:** Saves the report as a GitHub Actions artifact.
   - **Update Allure History Branch:**
     - Commits and pushes updated history to `allure-history-branch`.

3. **Deploy Job (`deploy`):**
   - **Dependencies:** Waits for the `test` job to complete.
   - **Download Report Artifact:** Retrieves the Allure HTML report.
   - **Deploy to GitHub Pages:**
     - Uses `peaceiris/actions-gh-pages` action.
     - Deploys the report to the `main` branch.
     - Configured for GitHub Pages hosting.

### Accessing Test Reports

The latest Allure test reports are automatically deployed to the `main` branch and can be accessed via GitHub Pages at:
https://efepisirici.github.io/behave_bdd_allure/

**Note:** Ensure that GitHub Pages is enabled for the `main` branch in your repository settings.

## Project Workflow

1. **Code Changes:**
   - Developers push code or open pull requests against the `master` branch.
   - Commits should follow the **Conventional Commits** standard.

2. **CI Pipeline Triggers:**
   - The GitHub Actions workflow is triggered.
   - **Docker Build Job** starts and builds the testing environment.

3. **Test Execution:**
   - Tests run inside a Docker container and directly on the GitHub runner.
   - Tests are written in **Gherkin Scenarios** and follow the **POM** structure.

4. **Allure Report Generation:**
   - Test results are generated using Allure.
   - Historical data is merged for comprehensive reporting.

5. **Report Deployment:**
   - The Allure HTML report is deployed to the `main` branch.
   - Accessible via GitHub Pages for stakeholders.

6. **Manual Testing (if applicable):**
   - Managed through Jira and Zephyr.
   - Bugs and test scenarios are tracked for continuous improvement.

## Setup Instructions

### Prerequisites

- **Python 3.9**
- **Docker**
- **Git**
- **BrowserStack Account** (for real device testing)
- **Jira Account** (for manual test management)
- **Allure CLI** (if generating reports locally)
- **Chrome WebDriver** (for local Selenium tests)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/efepisirici/behave_bdd_allure

2. **Navigate to the Project Directory:**

   ```bash
    cd behave_bdd_allure

3. **Install Python Dependencies:**

   ```bash
    pip install -r requirements.txt

4. **Set Up Environment Variables:**

   ```bash
    export BROWSERSTACK_USERNAME=<your_browserstack_username>
    export BROWSERSTACK_ACCESS_KEY=<your_browserstack_access_key>
    export JIRA_API_TOKEN=<your_jira_api_token>

## Running Tests Locally

### Using Docker

1. **Build Docker Image:**

   ```bash
    docker build -t ci-pipeline .

2. **Run Tests Inside Docker Container:**

   ```bash
    docker run -v $(pwd)/features/reports:/app/features/reports ci-pipeline

### Without Docker

1. **Install Chrome Dependencies:**

   ```bash
    sudo apt-get update
    sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4
    sudo apt-get --only-upgrade install google-chrome-stable

2. **Install Allure CLI Manually (if not already installed):**

   ```bash
    wget https://github.com/allure-framework/allure2/releases/download/2.20.1/allure-2.20.1.tgz
    tar -zxvf allure-2.20.1.tgz
    sudo mv allure-2.20.1 /opt/allure
    sudo ln -s /opt/allure/bin/allure /usr/bin/allure

3. **Run Tests and Generate Allure Results:**

   ```bash
    mkdir -p features/reports/allure-results
    behave -f allure_behave.formatter:AllureFormatter -o features/reports/allure-results

4. **Generate Allure Report:**

   ```bash
    allure generate features/reports/allure-results -o features/allure-report --clean
    allure open features/allure-report

### Manual Tests
- **Managed through Jira and Zephyr.**
- **Execute tests on BrowserStack's emulators or real devices.**
- **Update test scenarios and log bugs as needed.**

## Reporting

Allure reports provide a comprehensive view of test execution and results.

- **Generate Reports Locally:**

   ```bash
    allure generate features/reports/allure-results -o features/allure-report --clean
    allure open features/allure-report

- **Accessing CI Reports:**
    - **Reports are automatically deployed to GitHub Pages.**
    - **Navigate to https://efepisirici.github.io/behave_bdd_allure/**

## Commit Guidelines

This repository uses Conventional Commits for standardized commit messages.

**Format:**

    <type>(<scope>): <subject>
    

**Types:**

- **feat: New feature**
- **fix: Bug fix**
- **docs: Documentation changes**
- **style: Code style changes (formatting, etc.)**
- **refactor: Code changes that neither fix a bug nor add a feature**
- **test: Adding or correcting tests**

## Contribution Guidelines

1. **Fork the Repository.**


2. **Create a New Branch:**
   ```bash
    git checkout -b feature/your-feature-name

3. **Make Your Changes and Commit:**

   ```bash
    git commit -m "feat(scope): description of the feature"

4. **Push to Your Branch:**

   ```bash
    git push origin feature/your-feature-name

5. **Open a Pull Request.**

##  License

This project is licensed under the MIT License. See the LICENSE file for details.
