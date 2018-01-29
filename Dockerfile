FROM ubuntu:16.04

RUN mkdir /opt/workspace
WORKDIR /opt/workspace
ADD firmware /opt/workspace/firmware

RUN apt-get update && apt-get install -y wget unzip git make \
 srecord bc xz-utils gcc python curl python-pip python-dev build-essential \
 && python -m pip install --upgrade pip \
 && pip install -U platformio \
 && platformio platform install espressif8266 --with-package framework-arduinoespressif8266

WORKDIR /opt/workspace/firmware
