FROM ubuntu:18.04

#########################################
### Python                                                               
RUN apt-get update && apt-get -y install git wget build-essential
RUN apt-get install -y python3 python3-pip
RUN ln -s python3 /usr/bin/python
RUN ln -s pip3 /usr/bin/pip
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3-tk

#########################################
### Numpy
RUN pip install numpy

#########################################
### Make sure we have python3 and a working locale
RUN rm /usr/bin/python && ln -s python3 /usr/bin/python && rm /usr/bin/pip && ln -s pip3 /usr/bin/pip
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'
RUN apt-get install -y locales && locale-gen en_US.UTF-8

#########################################
### opengl and other
RUN apt-get update && apt-get install -y libgl1-mesa-glx
RUN apt-get install -y libsm6 libxext6 libxrender-dev

# Pre-install some python packages
RUN pip install jupyter scipy vtk imageio imageio-ffmpeg sklearn h5py pandas ipywidgets
RUN pip install mountaintools
RUN pip install isosplit5 rlcluster
RUN pip install h5_to_json==0.1.5

# python packages
RUN pip install spikeextractors spiketoolkit spikesorters
RUN pip install ephys_viz==0.9.3
RUN pip install ml_ms4alg

COPY spikodrome_sort.py /scripts/spikodrome_sort.py

ENTRYPOINT ["python", "/scripts/spikodrome_sort.py", "--output", "/output"]