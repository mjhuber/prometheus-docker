FROM alpine:latest
COPY ["./grafana-plugins.py", "./requirements.txt", "/tmp/"]
RUN apk update --no-cache && apk add python3 && pip3 install -r /tmp/requirements.txt
CMD ["/usr/bin/python3", "/tmp/grafana-plugins.py"]
