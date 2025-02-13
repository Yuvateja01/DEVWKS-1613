#Stepwise divide it into text files


#Reading log file
#Split the log data by delimitter
#Define a REGEX to extract data from each line
#For matched pattern lines- do the analysis
#output the data into a more human readable format i.e., Excel


import re
import os
import traceback

def createPacket(head, value):
    """
    Creates a dictionary (packet) from two lists: one containing keys (head) and the other containing values.

    Args:
        head (list): A list of keys for the dictionary.
        value (list): A list of values corresponding to the keys.

    Returns:
        dict: A dictionary where each key from the head list is mapped to the corresponding value from the value list.
    """
    tempDict = {}
    for i in range(len(head)):
        tempDict[head[i]] = value[i]
    return tempDict

def splitSpace(line):
    """
    Splits a log line into a dictionary with predefined keys.

    Args:
        line (str): The log line to be split.

    Returns:
        dict: A dictionary containing the following keys:
            - 'Timestamp': The timestamp extracted from the log line.
            - 'Node': Default value 'Not Recording'.
            - 'Warning Level': Default value 'Not Recording'.
            - 'Process': Default value 'NA'.
            - 'Message': The original log line.
            - 'line No': Default value 'NA'.
    """
    tempDict = {}
    regexGroup = re.split(':   ', line)

    tempDict['Timestamp'] = regexGroup[0]
    tempDict['Node'] = 'Not Recording'
    tempDict['Warning Level'] = 'Not Recording'
    tempDict['Process'] = 'NA'
    tempDict['Message'] = line
    tempDict['line No'] = 'NA'
    return tempDict

def processLogLine(line, headers, query = []):
    def processLogLine(line, headers, query=[]):
        """
        Processes a single log line and extracts relevant information based on the provided headers.

        Args:
            line (str): The log line to be processed.
            headers (list): A list of headers to be used for creating the packet.
            query (list, optional): A list to append the processed packet if certain conditions are met. Defaults to an empty list.

        Returns:
            list: The updated query list with the processed packet if the status is 'EndPointUnregistered'.

        Raises:
            Exception: If the log line does not match the expected format.
        """
    try:
        regexGroup = re.split(',', line)
        if type(regexGroup[-1]) is int: 
            regexGroup = [reg.strip() for reg in regexGroup]
            return createPacket(headers, regexGroup)
        else:
            raise Exception("Simple Message Log") 
    except Exception as e:
        tempRegex = splitSpace(line)

    brack = re.findall(r'\[[^\]]*\]', tempRegex['Message'])
    packetHeader = ['Timestamp','DeviceName','IPAddress','Description','Reason','Status','NodeID']
    tempPacket = {value.strip('[').strip(']').split('=')[0]:value.strip('[').strip(']').split('=')[1] for value in brack}
    # print(tempPacket)
    # tempPacket = {key:tempPacket.get(key) for key in headers}
    # print(tempRegex['Message'].split('%')[1].strip(': ').split('-')[-1])
    # exit()
    splitByPercent = tempRegex['Message'].split('%')
    if len(splitByPercent) > 2:
        tempSplit = ''
        for i in range(1, len(splitByPercent)):
            tempSplit += splitByPercent[i]
        splitByPercent = [splitByPercent[0], tempSplit]
    # print(splitByPercent)
    # exit()
    tempPacket['Timestamp'] = splitByPercent[0].split('.org ')[-1].strip(': ')
    tempPacket['Status'] = splitByPercent[1].split(':')[0].split('-')[-1]

    #Making Orderd dict
    tempPacket = {key:tempPacket.get(key) for key in packetHeader}
    if tempPacket['Status'] == 'EndPointUnregistered':
        query.append(tempPacket)

    return query

def analyseLogData(logPath):
    """
    Analyzes log data from the specified directory.

    This function reads log files from the given directory path, processes each line of the log files,
    and compiles the processed data into a query list.

    Args:
        logPath (str): The path to the directory containing log files.

    Returns:
        list: A list containing processed log data.

    Raises:
        Exception: If an error occurs while reading or processing the log files, the exception is caught,
                   and a traceback is printed.
    """
    headers = ['Timestamp', 'Node', 'Warning Level', 'Process', 'Message', 'line No']
    fileList = os.listdir(logPath)
    query = []

    try:
        for fileName in fileList:
            with open(os.path.join(logPath, fileName), "rt") as txt:
                for line in txt:
                    processLogLine(line, headers, query)
                    # Further processing of tempRegex can be done here
                    # Append to query if needed
    except Exception as e:
        print('In Exception Block')
        traceback.print_exc()
    return query
