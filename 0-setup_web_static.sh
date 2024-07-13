#!/usr/bin/env bash
# This script sets up web servers for the deployment of web_static

# Exit immediately if a command exits with a non-zero status
set -e

# Install Nginx if it is not already installed
if ! dpkg -l | grep -q nginx; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file to test Nginx configuration
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link, if it already exists, delete and recreate it
if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve the content
nginx_conf="/etc/nginx/sites-available/default"
if ! grep -q "location /hbnb_static/" $nginx_conf; then
    sudo sed -i "/server_name _;/a \tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n/t}\n" $nginx_conf
    sudo systemctl restart nginx
fi

# Exit successfully
exit 0
