FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/rladlsrua8/radcrews.git

WORKDIR /home/radcrews/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN echo "SECRET_KEY=django-insecure-wfq&s#=)l&0%ake0aiey@x7!+ij*zi1#b(&!f(fdb$p+m1hw=k" > .env

RUN export DJANGO_SETTINGS_MODULE=radcrews.settings

RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "radhelper.wsgi", "--bind", "0.0.0.0:8000"]