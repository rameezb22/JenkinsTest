FROM docker.io/bitnami/jenkins:2.387.3-debian-11-r6
USER root
RUN apt-get update && apt-get install python3-pip toilet curl awscli jq  -y && pip install --upgrade pip