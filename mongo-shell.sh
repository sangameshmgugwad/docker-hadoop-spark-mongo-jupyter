#!/bin/bash

# MongoDB Shell Access Script
# This script provides easy access to MongoDB shell

echo "Connecting to MongoDB..."
echo "Database: mongodb-dba"
echo "Port: 27018 (host) / 27017 (container)"
echo "Username: admin"
echo ""

docker exec -it mongodb-dba mongosh --host localhost --port 27017 -u admin -p admin --authenticationDatabase admin
