from elasticsearch import Elasticsearch

es_hosts = [
    "http://localhost:9200",
]


def elastic_upload():
    es = Elasticsearch(
        es_hosts
    )
    return es
