# -*- coding: utf-8 -*-
import json
from urllib import response
import requests
from contextlib import closing
import sqlite3

# prefect
from prefect import task, Flow, Parameter

# elasticsearch
from elasticsearch import helpers


# custom
from es import elastic_upload
from utils import save_to_json
from sql_helpers import sql_connector

es_ = elastic_upload()
mycursor, mydb = sql_connector()


def fetch_data_from_id(id, query):
    response = requests.get(
        'https://www.osti.gov/api/v1/records/{}'.format(id))
    if response.status_code == 400:
        raise RuntimeError("Invalid PMID/Search Query ({})".format(query))
    result = response.json()
    return result[0]


@task
def fetch_data_from_query(query):
    query_response = requests.get(
        'https://www.osti.gov/api/v1/records?q=%s' % str(query)).json()

    # Save OSTI IDs
    osti_ids = []
    for q in query_response:
        osti_ids.append(q['osti_id'])
    osti_id_json = dict()
    osti_id_json[query] = osti_ids
    save_to_json('osti_id_data.json', osti_id_json)

    # Query each osti id and return their json values
    osti_body = []
    osti_body_dict = []
    for i in osti_ids:
        res = fetch_data_from_id(i, query)
        osti_url = 'https://www.osti.gov/api/v1/records/%s' % str(i)
        osti_body_dict.append([res['osti_id'], res['title'], osti_url])
        osti_body.append(res)
        es_.index(index="osti-data", document=res, id=res['id'])
    save_to_json('osti_data.json', osti_body)
    return osti_body_dict


@task
def store_osti_data(json_data):
    create_script = 'CREATE TABLE IF NOT EXISTS osti_table (osti_id INT, title TEXT, osti_url TEXT)'
    insert_cmd = "INSERT INTO osti_table VALUES (?, ?,?)"

    with closing(sqlite3.connect("osti_data.db")) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.executescript(create_script)
            cursor.executemany(insert_cmd, json_data)
            conn.commit()


with Flow("osti-flow") as f:
    query = Parameter('search_paramenter', default='G20f')
    response_json = fetch_data_from_query(query)
    store_osti_data(response_json)

f.run()
