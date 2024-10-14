# nginx.sh

#!/usr/bin/bash

# Replace {YOUR_PROJECT_MAIN_DIR_NAME} with your actual project directory name
PROJECT_MAIN_DIR_NAME="growupmore_django_api"

# Replace {FOLDER_NAME_WHERE_SETTINGS_FILE_EXISTS} with the folder name where your nginx configuration file exists
FOLDER_NAME_WHERE_SETTINGS_FILE_EXISTS="GrowUpMore"

# Reload systemd daemon
sudo systemctl daemon-reload

# Remove default Nginx site if exists
sudo rm -f /etc/nginx/sites-enabled/default

# Copy Nginx configuration file
sudo cp "/home/ubuntu/$PROJECT_MAIN_DIR_NAME/nginx/nginx.conf" "/etc/nginx/sites-available/$FOLDER_NAME_WHERE_SETTINGS_FILE_EXISTS"

# Remove previous symbolic link
sudo rm /etc/nginx/sites-enabled/GrowUpMore

# Create symbolic link to enable Nginx site
sudo ln -s "/etc/nginx/sites-available/$FOLDER_NAME_WHERE_SETTINGS_FILE_EXISTS" "/etc/nginx/sites-enabled/"

# Add www-data user to ubuntu group
sudo gpasswd -a www-data ubuntu

# Restart Nginx service
sudo systemctl restart nginx
