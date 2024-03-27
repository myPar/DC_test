# Start from the official Python base image.
FROM python:3.11
# set main dir
WORKDIR /congrat-service
# copy requirements
COPY ./requirements.txt /congrat-service/requirements.txt

# install requirements (don't use --no-cache-dir because of build time increasing)
#RUN pip install --no-cache-dir --upgrade -r /ml-service/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /congrat-service/requirements.txt

# copy sources
COPY ./dto /congrat-service/dto
COPY ./services /congrat-service/services
COPY ./tools /congrat-service/tools
COPY ./main.py /congrat-service/

# start app command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]