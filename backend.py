import elasticsearch
import json
import requests
import csv
from flask import Flask, request, jsonify
from flask_cors import CORS
import traceback

app = Flask(__name__)
CORS(app)

es = elasticsearch.Elasticsearch(["http://localhost:9200"])

def es_create_index_if_not_exists(es, index):
    """Create the given ElasticSearch index and ignore error if it already exists"""
    try:
        es.indices.create(index)
    except elasticsearch.exceptions.RequestError as ex:
        if ex.error == 'resource_already_exists_exception':
            pass # Index already exists. Ignore.
        else: # Other exception - raise it
            raise ex

def filter_apis(name):
  query = {
    "query": {
      "bool": {
        "must": []
      }
    }
  }
  headers={
    "Content-Type": "application/json"
  }

  if name:
    query["query"]["bool"]["must"].append({
      "match": {
        "name": name
      }
    })

  all_res = {}

  res = es.search(index="stackoverflow", body=query, headers={
    "Content-Type": "application/json"
  })
  all_res["stackoverflow"] = res["hits"]["hits"]

  res = es.search(index="github", body=query, headers={
    "Content-Type": "application/json"
  })
  all_res["github"] = res["hits"]["hits"]

  res = es.search(index="tweet", body=query, headers={
    "Content-Type": "application/json"
  })
  all_res["tweet"] = res["hits"]["hits"]

  res = es.search(index="cve", body=query, headers={
    "Content-Type": "application/json"
  })
  all_res["cve"] = res["hits"]["hits"]

  # res = es.search(index="youtube", body=query, headers={
  #   "Content-Type": "application/json"
  # })
  # all_res["youtube"] = res["hits"]["hits"]

  return all_res

@app.route("/search", methods=["GET"])
def search():
  name = request.args.get("name")
  print("in search")
  apis = filter_apis(name)
  print(apis)
  return jsonify({
    "hits": {
      "hits": apis
    }
  })

@app.route("/insert", methods=["POST"])
def insert():
  api_data = request.json

  res = es.index(index="api", body=movie_data)

  return jsonify({
    "result": "success",
    "id": res["_id"]
  })

@app.route("/filter", methods=["POST"])
def filter():
  data = request.get_json()
  name = data.get("name")

  apis = filter_apis(name, actors, genre, date)
  return jsonify(apis)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
