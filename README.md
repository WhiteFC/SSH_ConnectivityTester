# SSH_ConnectivityTester
This script allows testing SSH connectivity to a list of servers specified in a file, logging the results of each connection attempt in a JSON file for further analysis. 

ConnectWithPlink.py: This is the main script that performs the SSH connection to the servers specified in the servers.txt file using the credentials provided in the credentials.txt file. It logs the results of connection attempts in a JSON file named connection_log.json.

privatekey.pem: This file contains the private key to be used for SSH authentication. You can generate it using PuTTYgen

credentials.txt: In this file the login credentials required for each server must be provided in the appropriate format. For example:

{
    "UserName": "your_username",
    "Password": "your_password"
}

servers.txt: Here you must list the servers to which the script will try to connect. Each server should be on a separate line. 

Make sure you have the “paramiko” library installed
