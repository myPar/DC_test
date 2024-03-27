# Start from the official Python base image.
FROM python:3.11
# set main dir
WORKDIR /get_city_service
# copy requirements
COPY ./requirements.txt /get_city_service/requirements.txt

# install requirements (don't use --no-cache-dir because of build time increasing)
RUN pip install --no-cache-dir --upgrade -r /get_city_service/requirements.txt

# copy sources
COPY ./main.py /get_city_service/
COPY ./tools.py /get_city_service/
COPY ./data /get_city_service/data
