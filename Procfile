web: python manage.py migrate && python manage.py collectstatic --noinput && gunicorn agreeddating.wsgi:application --bind 0.0.0.0:$PORT
