# Log Data Analysis and CSV Export Tool

## Overview
This project is a Python-based tool designed to **analyze log data** and export the results into a **CSV file**. It provides a streamlined way to process log files, extract meaningful insights, and save the analyzed data in a structured format for further use.

The tool is composed of two main components:
1. **Data Analysis**: Processes log files to extract relevant information.
2. **Data Representation**: Writes the processed data into a CSV file with specified headers.

---

## Features
- **Log File Analysis**: Automatically scans a specified directory for log files and extracts key information such as timestamps, device names, IP addresses, and more.
- **CSV Export**: Saves the analyzed data into a CSV file with customizable column headers.
- **Modular Design**: The project is divided into reusable modules for data analysis and data representation.

---

## File Structure
- **`main.py`**: The entry point of the application. It orchestrates the log data analysis and CSV export process.
- **`data_analysis.py`**: Contains the `analyseLogData` function, which handles the log file analysis.
- **`data_representation.py`**: Contains the `writeToCSV` function, which writes the analyzed data to a CSV file.

---

## How It Works
The `main.py` script performs the following steps:
1. **Define Log Path**: Specifies the directory containing the log files (`logs` by default).
2. **Analyze Log Data**: Calls the `analyseLogData` function to process the log files and extract relevant information.
3. **Export to CSV**: Calls the `writeToCSV` function to save the analyzed data into a CSV file named `sysLogAnalysis-ccm32.csv`.

---

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
