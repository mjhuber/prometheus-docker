# Prometheus - Chronix - Grafana Monitoring Stack
This is a monitoring stack used with docker-compose consisting of the following elements:

- prometheus: the main monitoring engine
- pushgateway: metrics can be pushed here and prometheus will scrape and ingest them.
- node-exporter: a worker to collect remote metrics that prometheus will ingest.
- alertmanager: the prometheus alert manager.
- cadvisor: a tool for collecting metrics about running docker containers.
- grafana: an open source dashboard tool with integrations into chronix and prometheus TSDB.
- chronix: an open source TSDB for long term data storage.
- chronix-ingester: A tool to collect metrics and publish them to chronix in batch mode.
- housekeeping: Simple container for running post-build setup tasks.


## How to Run
```
docker-compose up -d
```

## Urls
- Prometheus: http://localhost:9090/
- AlertManager: http://localhost:9093/
- Grafana: http://localhost:3000/
  * To configure ldap auth, edit ./grafana/ldap.toml
  * Admin username: admin password: DevOps_2017
- cAdvisor: http://localhost:8000
- PushGateway: http://localhost:9091/
- Node Exporter: http://localhost:9100/
- Chronix: http://localhost:9094/solr/#/
