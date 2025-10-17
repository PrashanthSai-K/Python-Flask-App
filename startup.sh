#!/bin/bash
# Startup script for Azure App Service Python app
gunicorn --bind=0.0.0.0:$PORT app:app
