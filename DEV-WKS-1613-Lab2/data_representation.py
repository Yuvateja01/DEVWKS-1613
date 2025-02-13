import csv

def writeToCSV(query, file_name, headers):
    """
    Writes the provided query data to a CSV file.

    Args:
        query (list of dict): A list of dictionaries containing the data to be written to the CSV file.
        file_name (str): The name of the CSV file to write to.
        headers (list of str): A list of strings representing the header row for the CSV file.

    Returns:
        None
    """
    with open(file_name, 'w', newline='') as myFile:
        writer = csv.writer(myFile)
        writer.writerow(headers)
        for dictionary in query:
            writer.writerow(dictionary.values())
