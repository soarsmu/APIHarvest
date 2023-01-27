import elasticsearch
import json
import requests
import os

def es_create_index_if_not_exists(es, index):
    """Create the given ElasticSearch index and ignore error if it already exists"""
    try:
        es.indices.create(index=index)
    except elasticsearch.exceptions.RequestError as ex:
        if ex.error == 'resource_already_exists_exception':
            pass # Index already exists. Ignore.
        else: # Other exception - raise it
            raise ex

def insert_cve():
    for i in range(len(cve_labels)):
        for cve_label in cve_labels[i].split(" "):
            cve = {
                "name": cve_label,
                "content": cve_texts[i]
            }
            es.index(index="cve", body=cve)

cve_texts = open("data/test_texts.txt").read().splitlines()
cve_labels = open("data/test_labels.txt").read().splitlines()
es = elasticsearch.Elasticsearch(["http://localhost:9200"])
es.indices.delete(index="cve")
es_create_index_if_not_exists(es,"cve")
insert_cve()