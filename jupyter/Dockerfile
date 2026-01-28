FROM jupyter/pyspark-notebook:latest

USER root

# Install Java and other dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    openjdk-11-jdk \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER ${NB_UID}

# Install Python packages for Spark, ML, and MongoDB
RUN pip install --no-cache-dir \
    pyspark==3.0.0 \
    pymongo==4.3.3 \
    numpy==1.23.5 \
    pandas==1.5.3 \
    matplotlib==3.7.1 \
    seaborn==0.12.2 \
    scikit-learn==1.2.2 \
    jupyter-contrib-nbextensions \
    findspark

# Install MongoDB Spark Connector JARs
RUN mkdir -p /home/jovyan/.ivy2/jars && \
    cd /home/jovyan/.ivy2/jars && \
    wget https://repo1.maven.org/maven2/org/mongodb/spark/mongo-spark-connector_2.12/3.0.1/mongo-spark-connector_2.12-3.0.1.jar && \
    wget https://repo1.maven.org/maven2/org/mongodb/mongodb-driver-sync/4.0.5/mongodb-driver-sync-4.0.5.jar && \
    wget https://repo1.maven.org/maven2/org/mongodb/bson/4.0.5/bson-4.0.5.jar && \
    wget https://repo1.maven.org/maven2/org/mongodb/mongodb-driver-core/4.0.5/mongodb-driver-core-4.0.5.jar

# Set environment variables
ENV PYSPARK_PYTHON=/opt/conda/bin/python
ENV PYSPARK_DRIVER_PYTHON=jupyter
ENV PYSPARK_DRIVER_PYTHON_OPTS='notebook'

# Create startup script for Spark configuration
RUN mkdir -p /home/jovyan/.jupyter
COPY jupyter_notebook_config.py /home/jovyan/.jupyter/

WORKDIR /home/jovyan/work
