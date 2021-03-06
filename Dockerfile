# inherit from the flaskbase
FROM tapis/flaskbase:latest

# set the name of the api, for use by
ENV TAPIS_API streams


# install additional requirements for the service
COPY requirements.txt /home/tapis/requirements.txt
#RUN pip install --upgrade --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org
RUN pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org -r /home/tapis/requirements.txt

# copy service source code
COPY configschema.json /home/tapis/configschema.json
COPY config-local.json /home/tapis/config.json
COPY service /home/tapis/service

#COPY tapy/tapy /home/tapis/tapy

# run service as non-root tapis user
RUN chown -R tapis:tapis /home/tapis
USER tapis
