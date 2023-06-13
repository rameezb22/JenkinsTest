FROM docker.io/bitnami/jenkins:2.387.3-debian-11-r6
USER root
RUN apt-get update && apt-get install python3-pip toilet curl awscli jq  -y && pip install --upgrade pip
RUN  pip3 install selenium
RUN apt-get install libnss3 -y

RUN curl -LO https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb
RUN rm google-chrome-stable_current_amd64.deb 
