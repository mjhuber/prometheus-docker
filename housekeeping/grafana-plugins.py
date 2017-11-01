import os
import json, requests


datasources = {
    "Prometheus": {
        "name": "Prometheus",
        "url": "http://prometheus:9090",
        "type": "prometheus",
        "access": "proxy",
        "basicAuth": False
    },
    "Chronix": {
        "name": "Chronix",
        "url": "http://chronix:8983/solr/chronix",
        "type": "chronix",
        "access": "proxy",
        "basicAuth": False
    }
}


def create_datasources(baseurl):
    existing = get_datasources(baseurl)
    for datasource in [datasources[key] for key,val in datasources.items() if val['url'] not in existing]:
        create_datasource(baseurl,datasource)


def create_datasource(baseurl, datasource):
    try:
        print('Creating datasource for {0}'.format(datasource['url']))
        response = requests.post('{0}/api/datasources'.format(baseurl), data=datasource)
    except Exception as e:
        print('Exception creating datasource {0}: {1}'.format(datasource['name'],e.message))


def get_datasources(baseurl):
    try:
        response = requests.get('{0}/api/datasources'.format(baseurl))
        if response.status_code ==  200:
            data = json.loads(response.text)
            return [d['url'] for d in data]
    except Exception as e:
        print('Exception getting datasources from {}: {}'.format(baseurl,e.message))
    return None




if __name__ == '__main__':
    create_datasources('http://admin:DevOps_2017@jenkins.devlab.mciso.org:3000')
    print('Done!')
