# -*- coding: utf-8 -*-

import subprocess
import paramiko
import json

private_key_path = "./privatekey.pem"
credentials_file = "./credentials.txt"
servers_file = "./servers.txt"
log_file = "./connection_log.json"
password = "username"
username = "pw"

print("Using the following private key:", private_key_path)
print("Credentials file:", credentials_file)
print("Servers file:", servers_file)
print("Log file:", log_file)
print("Provided password:", password)
print("Provided username:", username)

# Read credentials from the file
with open(credentials_file, "r") as file:
    credentials = file.read()
    print("Read credentials from file:", credentials)

# Read the list of servers from the file
with open(servers_file, "r") as file:
    servers = file.readlines()
    print("Read servers from file:", servers)

# List to store the records
connection_records = []

# Iterate over each server and establish an SSH connection
for server in servers:
    server = server.strip()
    try:
        print("Trying to connect to", server, "as", username + "...")
        
        # Build the SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect with private key or password
        try:
            client.connect(server, username=username, password=password, key_filename=private_key_path)
            status = "SSH connection established successfully to {0} as {1}.".format(server, username)
            print(status)  # Display success message in the console
            connection_records.append({"server": server, "username": username, "status": status, "connection_successful": True})
        except paramiko.AuthenticationException as auth_error:
            status = "Authentication error: {0}".format(auth_error)
            print(status)
            connection_records.append({"server": server, "username": username, "status": status, "connection_successful": False})
            continue  # Continue with the next server if there's an authentication error
        except Exception as e:
            status = "Error establishing SSH connection to {0} as {1}: {2}".format(server, username, e)
            print(status)
            connection_records.append({"server": server, "username": username, "status": status, "connection_successful": False})
            continue  # Continue with the next server if there's a connection error

        # Close the SSH connection
        client.close()
        
    except Exception as e:
        status = "Error establishing SSH connection to {0} as {1}: {2}".format(server, username, e)
        print(status)
        connection_records.append({"server": server, "username": username, "status": status, "connection_successful": False})

# Save the records to the JSON file
with open(log_file, "w") as f:
    json.dump(connection_records, f, indent=4)

print("Records saved in:", log_file)