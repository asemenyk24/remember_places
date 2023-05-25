FROM python:3

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /code
WORKDIR /code

COPY requirements.txt requirments.txt

RUN apt-get update -y && apt-get upgrade -y

RUN apt-get install -y gdal-bin libgdal-dev
RUN apt-get install -y python3-gdal
RUN apt-get install -y binutils libproj-dev
RUN apt-get install -y postgresql postgresql-contrib

RUN pip3 install -r requirments.txt

CMD ["python", "manage.py", "migrate", "--no-input"]
