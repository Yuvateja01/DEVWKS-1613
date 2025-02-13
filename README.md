# DEVWKS-1613
 
# Cisco Live DevNet Workshop: CUCM Tools

Welcome to the **Cisco Live DevNet Workshop** repository! This repository contains tools and scripts designed to assist with **Cisco Unified Communications Manager (CUCM)** operations. The workshop focuses on automating CUCM health checks and analyzing log data, providing hands-on experience with Python-based tools.

---

## **Workshop Overview**

This workshop is part of the Cisco Live DevNet Zone, where participants learn how to leverage automation and programmability to streamline CUCM operations. The repository is divided into two main tools:

1. **Cluster Health Check**: Automates health checks for CUCM clusters.
2. **Log Data Analysis and CSV Export Tool**: Analyzes log data and exports results into a structured CSV format.

---

## **Repository Structure**

---

## **Tools Overview**

### 1. **Cluster Health Check**
This tool automates the process of checking the health of CUCM clusters by connecting to servers via SSH, executing commands, and saving the output for analysis. It is particularly useful for monitoring database replication status and other critical metrics.

#### **Key Features**:
- Automates SSH connections to CUCM servers.
- Executes a customizable list of commands.
- Saves command outputs to text files for each server.
- Includes basic analysis of CUCM database replication status.

For detailed setup and usage instructions, refer to the [Cluster Health Check README](./Cluster%20Health%20Check/README.md).

---

### 2. **Log Data Analysis and CSV Export Tool**
This Python-based tool is designed to analyze log files and export the results into a structured CSV format. It simplifies the process of extracting meaningful insights from log data and organizing it for further use.

#### **Key Features**:
- Automatically scans a directory for log files.
- Extracts key information such as timestamps, device names, and IP addresses.
- Exports analyzed data into a CSV file with customizable headers.

For detailed setup and usage instructions, refer to the [Log Data Analysis README](./Log%20Data%20Analysis%20and%20CSV%20Export%20Tool/README.md).

---

## **Getting Started**

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
