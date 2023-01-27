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

def insert_tweet():
    for name in tweets:
        for text in tweets[name]:
            tweet = {
                "name": name,
                "content": text
            }
            es.index(index="tweet", body=tweet)

tweets = {}
for fname in os.listdir('data/tweets'):
    data = eval(open('data/tweets/'+fname).read())
    name = fname.split(".")[0]
    tweets[name] = []
    for arr in data:
        if arr[1] == "Lib":
            tweets[name].append(arr[0])

es = elasticsearch.Elasticsearch(["http://localhost:9200"])
#es.indices.delete(index="tweet")
es_create_index_if_not_exists(es,"tweet")
insert_tweet()