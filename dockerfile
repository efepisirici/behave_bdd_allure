FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

# Update the package list and install necessary dependencies
RUN apt-get update && apt-get install -y \
    unzip \
    xvfb \
    libxi6 \
    libgconf-2-4 \
    wget \
    curl \
    gnupg \
    python3.9 \
    python3-pip \
    git \
    openjdk-11-jre-headless \
    sudo && \
    apt-get clean

# Install Google Chrome
RUN curl -sSL https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add - && \
    sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
    sudo apt-get update && \
    sudo apt-get install -y google-chrome-stable

# Set Python 3.9 as the default Python version
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.9 1
RUN python -m pip install --upgrade pip

# Install Python dependencies
RUN pip install behave selenium webdriver-manager pytest pyhamcrest allure-behave allure-python-commons

# Install Allure CLI
RUN wget https://github.com/allure-framework/allure2/releases/download/2.20.1/allure-2.20.1.tgz && \
    tar -zxvf allure-2.20.1.tgz && \
    mv allure-2.20.1 /opt/allure && \
    ln -s /opt/allure/bin/allure /usr/bin/allure

# Create directories for Allure results and history
RUN mkdir -p /app/features/reports/allure-results/history

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Define the command to run tests, generate Allure results, and produce the HTML report
CMD mkdir -p features/reports/allure-results && \
    behave -f allure_behave.formatter:AllureFormatter -o features/reports/allure-results || true && \
    allure generate features/reports/allure-results -o features/allure-report --clean && \
    echo "Allure report generated at: /app/features/allure-report"
