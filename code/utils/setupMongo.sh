#!/bin/bash

REPO_PATH="/etc/yum.repos.d/mongodb-org-7.0.repo"

# Check if the repo file already exists
if [ ! -f "$REPO_PATH" ]; then
    echo "Adding MongoDB 7.0 repository..."
    sudo sh -c "echo '[mongodb-org-7.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/9/mongodb-org/7.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-7.0.asc' > $REPO_PATH"
else
    echo "Repository file already exists."
fi

sudo dnf makecache
echo "Installing MongoDB..."
sudo dnf install mongodb-org -y

echo "Starting MongoDB..."
sudo systemctl start mongod

echo "Enabling MongoDB to start on boot..."
sudo systemctl enable mongod

echo "Current status of MongoDB:"
sudo systemctl status mongod

mongod --config /etc/mongod.conf
