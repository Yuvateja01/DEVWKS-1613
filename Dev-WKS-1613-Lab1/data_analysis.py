import re
import logging

logging.basicConfig(level=logging.INFO)

class DataAnalysis:
    """
    A class used to perform data analysis on command outputs from a text file.

    Attributes
    ----------
    file_path : str
        The path to the text file containing command outputs.
    commands : list
        A list to store the commands extracted from the text file.
    outputs : list
        A list to store the outputs corresponding to the commands.

    Methods
    -------
    read_cmd_output():
        Reads the text file and separates commands and outputs using regex.
    
    analyze_dbreplication_output():
        Analyzes the output of the 'utils dbreplication runtimestate' command.
    
    _parse_rows(rows):
        Parses the rows of the table content to extract server information.
    
    _check_server(server, errors, tests_performed):
        Checks the server's ping, DB/RPC/mon status, and replication setup status.
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.commands = []
        self.outputs = []


    def read_cmd_output(self):
        """Reads the text file and separates commands and outputs using regex."""
        with open(self.file_path, 'r') as file:
            content = file.read()
            # Updated regex to find commands and their outputs
            command_pattern = r':::Command:::(.*?)\n(.*?)(?=\n={2,}|$)'
            matches = re.findall(command_pattern, content, re.DOTALL)
            # print(f"Found {len(matches)} matches.")
            # print(matches)
            for command, output in matches:
                self.commands.append(command.strip())
                self.outputs.append(output.strip())


    def analyze_dbreplication_output(self):
        """Analyzes the output of the 'utils dbreplication runtimestate' command."""
        command = "utils dbreplication runtimestate"
        print(f"Analyzing output for command(s): {self.commands}")
        if command not in self.commands:
            return f"Command '{command}' not found."

        output = self.outputs[self.commands.index(command)]
        # print(f"Output:\n{self.outputs}")
        errors, tests_performed = [], []

        # Extract the table content
        table_start = output.find("SERVER-NAME")
        if table_start == -1:
            return "No table found in the output."

        table_content = output[table_start:].strip()
        rows = table_content.splitlines()[2:]  # Skip the header rows

        servers = self._parse_rows(rows)
        if not servers:
            return "No servers found in the output."

        for server in servers:
            self._check_server(server, errors, tests_performed)

        if errors:
            return "\n".join(errors)
        else:
            return "All checks passed successfully. Tests performed:\n" + "\n".join(tests_performed)

    def _parse_rows(self, rows):
        """
        Parses a list of rows containing server information and extracts relevant data.

        Args:
            rows (list of str): A list of strings, each representing a row of server data.

        Returns:
            list of tuple: A list of tuples, each containing the extracted data from a row.
                           The tuple contains the following elements:
                           - Server name (str)
                           - IP address 1 (str)
                           - IP address 2 (str)
                           - Status flags (str)
                           - Numeric value or '--' (str)
                           - Group identifier or '-' (str)
                           - Numeric value or '-' (str)
                           - Status message (str)

        Logs:
            A warning message if a row cannot be parsed.
        """
        servers = []
        for row in rows:
            if not row.strip():
                continue
            match = re.match(
                r'(\S+)\s+([\d.]+)\s+([\d.]+)\s+([Y/N]/[Y/N]/[Y/N])\s+(\d+|--)\s+\((g_\d+|-)\)\s+\((\d+|-)\)\s+(Setup Completed|Out Of Sync)',
                row
            )
            if match:
                servers.append(match.groups())
            else:
                logging.warning(f"Could not parse row: {row}")
        return servers

    def _check_server(self, server, errors, tests_performed):
        """
        Checks the status of a server and records any errors or successful tests performed.

        Parameters:
        server (tuple): A tuple containing the server details in the following order:
            - server_name (str): The name of the server.
            - ip_address (str): The IP address of the server.
            - ping (str): The ping time to the server in milliseconds.
            - db_rpc_mon (str): The status of the DB/RPC/mon services.
            - queue (str): The queue status (not used in this function).
            - group_id (str): The group ID of the server (not used in this function).
            - details (str): Additional details about the server (not used in this function).
            - replication_setup (str): The status of the replication setup.

        errors (list): A list to which any error messages will be appended.
        tests_performed (list): A list to which any successful test messages will be appended.

        Returns:
        None
        """
        server_name, ip_address, ping, db_rpc_mon, queue, group_id, details, replication_setup = server

        # Check ping
        try:
            if float(ping) >= 80:
                errors.append(f"Error: Ping for {server_name} is {ping} msec, should be less than 80 msec.")
            else:
                tests_performed.append(f"Ping for {server_name} is {ping} msec (PASS).")
        except ValueError:
            errors.append(f"Error: Invalid ping value for {server_name}: {ping}")

        # Check DB/RPC/mon status
        if db_rpc_mon != "Y/Y/Y":
            errors.append(f"Error: DB/RPC/mon for {server_name} is {db_rpc_mon}, should be Y/Y/Y.")
        else:
            tests_performed.append(f"DB/RPC/mon for {server_name} is {db_rpc_mon} (PASS).")

        # Check replication setup status
        if replication_setup != "Setup Completed":
            errors.append(f"Error: Replication setup for {server_name} is '{replication_setup}', should be 'Setup Completed'.")
        else:
            tests_performed.append(f"Replication setup for {server_name} is '{replication_setup}' (PASS).")