# Cluster Health Check

This repository provides a tool to perform a **cluster health check** for Cisco Unified Communications Manager (CUCM). The tool connects to CUCM servers via SSH, executes a set of commands, and saves the output for further analysis.

---

## **Features**
- Automates SSH connections to CUCM servers.
- Executes a customizable list of commands.
- Saves command outputs to text files for each server.
- Includes basic analysis of CUCM database replication status.

---

## **Requirements**
To use this tool, you need to install the following Python libraries:
- **paramiko**: `pip install paramiko`
- **paramiko_expect**: `pip install paramiko_expect`

---

## **Setup**
1. **Server List**:
   - Edit the `uc_server.json` file to provide the CUCM server details:
     - IP address
     - OS Admin username
     - Password

2. **Command List**:
   - Edit the `commandList.txt` file to include the commands you want to execute on the CUCM servers.

---

## **Usage**
1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
