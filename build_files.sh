#!/bin/bash

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Collect static files (Whitenoise or for admin)
python manage.py collectstatic --noinput

# Run migrations (optional – better to run manually first time or use external DB tool)
# python manage.py migrate