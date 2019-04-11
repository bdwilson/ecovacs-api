FROM debian:stretch

ARG ECOVACS_USER
ARG ECOVACS_PASS
ARG ECOVACS_COUNTRY=us
ARG ECOVACS_CONTINENT=na
ARG ECOVACS_PORT=5050

RUN mkdir /code
WORKDIR /code

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip git && \
    pip3 install sucks && \
    pip3 install flask && \
    git clone https://github.com/bdwilson/ecovacs-api && \
	sed -i "s/ECOVACS_USER/${ECOVACS_USER}/" /code/ecovacs-api/ecovacs_flask.py && \
	sed -i "s/ECOVACS_PASS/${ECOVACS_PASS}/" /code/ecovacs-api/ecovacs_flask.py && \
	sed -i "s/ECOVACS_COUNTRY/${ECOVACS_COUNTRY}/" /code/ecovacs-api/ecovacs_flask.py && \
	sed -i "s/ECOVACS_CONTINENT/${ECOVACS_CONTINENT}/" /code/ecovacs-api/ecovacs_flask.py && \
	sed -i "s/ECOVACS_PORT/${ECOVACS_PORT}/" /code/ecovacs-api/ecovacs_flask.py

#ADD . /code/
EXPOSE ${ECOVACS_PORT}
CMD [ "python3", "/code/ecovacs-api/ecovacs_flask.py" ]
