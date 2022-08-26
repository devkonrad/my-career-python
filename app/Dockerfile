FROM python:3.6.3

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add requirements
ADD ./requirements.txt /usr/src/app/requirements.txt

# Upgrade pip
RUN pip install --upgrade pip

# install requirements
RUN pip install -r requirements.txt

# add app
ADD . /usr/src/app