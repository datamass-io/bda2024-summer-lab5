#!/bin/zsh

# create the database account
az cosmosdb create --name mdtest4321 --kind GlobalDocumentDB --resource-group DataAcademy2024

# list accounts (shows document endpoint uri)
az cosmosdb list -g DataAcademy2024 -o table

# create the database
az cosmosdb sql database create --account-name mdtest4321 --name "iot" --resource-group DataAcademy2024

# create the container
az cosmosdb sql container create --account-name mdtest4321 --database-name "iot" --name "monitoring" --partition-key-path "/system" --throughput 400 --resource-group DataAcademy2024

# show the database keys
az cosmosdb keys list --name mdtest4321 --resource-group DataAcademy2024

# show the database connection strings
az cosmosdb keys list --type connection-strings --name mdtest4321 --resource-group DataAcademy2024