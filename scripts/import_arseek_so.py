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

def insert_SO(filename):
  with open(filename, "r") as file:
    so_dict = json.load(file)
    for name in so_dict:
        for item in so_dict[name]:
            post = {
                "name": name,
                "title": item["title"],
                "link": item["link"],
                "content": thread_content[item["thread_id"]]
            }
            es.index(index="stackoverflow", body=post)

thread_content = {}
with open('data/text_code_pairs_test.jsonl') as f:
    for line in f:
        data = json.loads(line)
        thread_content[data["thread_id"]] = data["pairs"][0]

es = elasticsearch.Elasticsearch(["http://localhost:9200"])
#es.indices.delete(index="stackoverflow")
es_create_index_if_not_exists(es,"stackoverflow")
insert_SO("data/threads_to_index.json")