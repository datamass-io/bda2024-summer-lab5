import os
import json
import uuid

import psutil
import time

from azure.identity import DefaultAzureCredential
from azure.cosmos import CosmosClient

# for database management use azure-mgmt-cosmosdb

database_name = "iot"
container_name = "monitoring"
database_endpoint = "https://mdtest4321.documents.azure.com:443/"
try:
    print("Hello, Azure CosmosDB!")
    # credential = DefaultAzureCredential()
    # client = CosmosClient(url=database_endpoint, credential=credential)

    # or use connection string
    cosmos_key = os.getenv('COSMOS_KEY')
    client = CosmosClient(url=database_endpoint, credential=cosmos_key)

    database = None  # TODO create database client
    container = None  # TODO create container client
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    data = {
        "id": str(uuid.uuid4()),
        "system": "work",  # try to create data for other system, e.g. "work"
        "timestamp": timestamp,
        "cpu_usage": cpu,
        "mem_usage": mem,
    }

    print("Creating item...")
    # TODO create the item

    QUERY = None  # TODO write the SQL QUERY WITH @systemID parameter
    SYSTEMID = "home"
    params = [dict(name="@systemID", value=SYSTEMID)]
    results = None  # TODO query the container, use parameters, experiment with enable_cross_partition_query flag

    items = [item for item in results]
    output = json.dumps(items, indent=True)
    print("Result list\t", output)

except Exception as ex:
    print("Exception: ")
    print(ex)
