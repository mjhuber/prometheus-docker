FROM alpine:latest
EXPOSE 8983
RUN apk update --no-cache && apk add --no-cache bash unzip wget git openjdk8 && wget https://github.com/ChronixDB/chronix.server/releases/download/v0.4/chronix-0.4.zip
ENV JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk
RUN unzip /chronix-0.4.zip && apk del unzip wget git
WORKDIR /chronix-solr-6.3.0
CMD ["sh","-c","/chronix-solr-6.3.0/bin/solr start -force -f"]
