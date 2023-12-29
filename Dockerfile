<<<<<<< HEAD
# start by pulling the python image
FROM python:latest

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

COPY . /app
# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# configure the container to run in an executed manner
ENTRYPOINT [ "python" , "main.py" ]
=======
# start by pulling the python image
FROM python:latest

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

COPY . /app
# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# configure the container to run in an executed manner
ENTRYPOINT [ "python" , "main.py" ]
>>>>>>> 5410bbe3f002be90cae88810be2ccf7818176a63
