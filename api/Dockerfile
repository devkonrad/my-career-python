FROM python:3.6.3

# set working directory
RUN mkdir -p /usr/src/api
WORKDIR /usr/src/api

# add requirements
ADD ./requirements.txt /usr/src/api/requirements.txt

# Upgrade pip
RUN pip install --upgrade pip

# install requirements
RUN pip install -r requirements.txt

# add app
ADD . /usr/src/api