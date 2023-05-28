FROM ubuntu

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ=Asia/Krasnoyarsk
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY . /code
WORKDIR /code

COPY requirements.txt requirments.txt

RUN apt update -y && apt upgrade -y

RUN apt install libpq-dev -y
RUN apt install build-essential -y
RUN apt install gdal-bin libgdal-dev -y
RUN apt install python3-gdal python3-dev python3-pip -y
RUN apt install binutils libproj-dev gcc -y

RUN pip3 install -r requirments.txt
RUN pip3 install gdal==3.4.0
CMD ["python3", "manage.py", "migrate", "--no-input"]
