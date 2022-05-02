FROM python:3.9.0

WORKDIR /home/

RUN echo "test1233"

RUN git clone https://github.com/rladlsrua8/radcrews.git

WORKDIR /home/radcrews/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=radhelper.settings.deploy && python manage.py migrate --settings=radhelper.settings.deploy && gunicorn radhelper.wsgi --env DJANGO_SETTINGS_MODULE=radhelper.settings.deploy --bind 0.0.0.0:8000"]