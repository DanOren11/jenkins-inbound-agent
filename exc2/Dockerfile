FROM jenkins/inbound-agent:latest


USER root

RUN apt-get update && apt-get install -y npm docker.io

COPY package*.json ./

RUN npm install

COPY . .
EXPOSE 3000

USER jenkins