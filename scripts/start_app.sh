# start_app.sh

#!/usr/bin/env bash
set -e

PROJECT_MAIN_DIR_NAME="growupmore_django_api"

# Validate variables
if [ -z "$PROJECT_MAIN_DIR_NAME" ]; then
    echo "Error: PROJECT_MAIN_DIR_NAME is not set. Please set it to your project directory name." >&2
    exit 1
fi

# Create the .env file at the root if not already created
echo "Creating .env file at the root for Supabase database connection..."
cat <<EOT > "/home/ubuntu/$PROJECT_MAIN_DIR_NAME/.env"
# Database connection string
DATABASE_URL=postgresql://postgres.pfdgzhiuibsnpbznasxl:WM08IriQxsIG2jfh@aws-0-ap-south-1.pooler.supabase.com:6543/growupmore_db
EOT

# Change ownership to ubuntu user
sudo chown -R ubuntu:ubuntu "/home/ubuntu/$PROJECT_MAIN_DIR_NAME"

# Change directory to the project main directory
cd "/home/ubuntu/$PROJECT_MAIN_DIR_NAME"

# Activate virtual environment
echo "Activating virtual environment..."
source "/home/ubuntu/$PROJECT_MAIN_DIR_NAME/venv/bin/activate"

# Make migrations for all apps
# echo "Making migrations for all apps..."
# python manage.py makemigrations admin
# python manage.py makemigrations auth
# python manage.py makemigrations contenttypes
# python manage.py makemigrations sessions

# python manage.py migrate admin
# python manage.py migrate auth
# python manage.py migrate contenttypes
# python manage.py migrate sessions

# python manage.py makemigrations master
# python manage.py makemigrations hr
# python manage.py makemigrations learn

# python manage.py migrate master
# python manage.py migrate hr
# python manage.py migrate learn

# Apply the migrations
# echo "Applying migrations..."
# python manage.py migrate

# Run collectstatic command
echo "Running collectstatic command..."
python manage.py collectstatic --noinput

# Restart Gunicorn and Nginx services
echo "Restarting Gunicorn and Nginx services..."
sudo service gunicorn restart
sudo service nginx restart

echo "Application started successfully."

