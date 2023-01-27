import elasticsearch
import json
import requests

def es_create_index_if_not_exists(es, index):
    """Create the given ElasticSearch index and ignore error if it already exists"""
    try:
        es.indices.create(index=index)
    except elasticsearch.exceptions.RequestError as ex:
        if ex.error == 'resource_already_exists_exception':
            pass # Index already exists. Ignore.
        else: # Other exception - raise it
            raise ex

def insert_code():
    for name in code_content:
        code = {
            "name": name,
            "content": code_content[name]
        }
        es.index(index="github", body=code)

code_content = {}
with open('data/text_code_pairs_test.jsonl') as f:
    for line in f:
        data = json.loads(line)
        code_content[data["target_fqn"]] = data["pairs"][1]

es = elasticsearch.Elasticsearch(["http://localhost:9200"])
#es.indices.delete(index="github")
es_create_index_if_not_exists(es,"github")
insert_code()