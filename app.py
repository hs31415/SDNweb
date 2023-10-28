from flask import Flask, render_template, request
import requests
import json
import subprocess


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_switch_info', methods=['GET'])
def get_switch_info():
    url = 'http://localhost:8080/stats/switches'
    headers = {'Content-Type': 'application/json'}
    resp = requests.get(url=url, headers=headers, auth=requests.auth.HTTPBasicAuth('admin', 'admin'))
    data = json.loads(resp.text)
    return data
    
@app.route('/get_flow_info', methods=['GET'])  
def get_flow_info():
    url = 'http://localhost:8080/stats/flow/1'
    headers = {'Content-Type': 'application/json'}
    resp = requests.get(url=url, headers=headers, auth=requests.auth.HTTPBasicAuth('admin', 'admin'))
    data = json.loads(resp.text)
    return data
    
@app.route('/get_host_info', methods=['GET'])  
def get_host_info():
    url = 'http://localhost:8080/v1.0/topology/hosts'
    headers = {'Content-Type': 'application/json'}
    resp = requests.get(url=url, headers=headers, auth=requests.auth.HTTPBasicAuth('admin', 'admin'))
    data = json.loads(resp.text)
    return data

@app.route('/get_link_info', methods=['GET'])  
def get_link_info():
    url = 'http://localhost:8080/v1.0/topology/links'
    headers = {'Content-Type': 'application/json'}
    resp = requests.get(url=url, headers=headers, auth=requests.auth.HTTPBasicAuth('admin', 'admin'))
    data = json.loads(resp.text)
    return data

@app.route('/post_timeout', methods=['POST'])
def post_timeout():
    url = 'http://127.0.0.1:8080/stats/flowentry/add'
    headers = {'Content-Type': 'application/json'}
    data = {
        "dpid": 1,
        "cookie": 1,
        "cookie_mask": 1,
        "table_id": 0,
        "hard_timeout": 20,
        "priority": 65535,
        "flags": 1,
        "match":{
            "in_port":1
        },
        "actions":[]
    }
    
    requests.post(url=url, json=data, headers=headers, auth=requests.auth.HTTPBasicAuth('admin','admin'))

@app.route('/post_vlan', methods=['POST'])
def post_vlan():
    url = 'http://127.0.0.1:8080/stats/flowentry/add'
    headers = {'Content-Type': 'application/json'}
    data1 = {
         "dpid": 1,
         "priority": 65535,
         "match": {
                  "in_port": 1
         },
         "actions": [{
         "type": "PUSH_VLAN",
         "ethertype": 33024
         },
         {
         "type": "SET_FIELD",
         "field": "vlan_vid",
         "value": 4096
         },
         {
         "type": "OUTPUT",
         "port": 3
        }
        ]
   }
   
    data2 = {
         "dpid": 1,
         "priority": 65535,
         "match": {
                  "in_port": 2
         },
         "actions": [{
         "type": "PUSH_VLAN",
         "ethertype": 33024
         },
         {
         "type": "SET_FIELD",
         "field": "vlan_vid",
         "value": 4097
         },
         {
         "type": "OUTPUT",
         "port": 3
        }
        ]
   }
    data3 = {
         "dpid": 1,
         "priority": 65535,
         "match": {
                  "vlan_vid": 0
         },
         "actions": [{
         "type": "POP_VLAN",
         "ethertype": 33024
         },
         {
         "type": "OUTPUT",
         "port": 1
         },
        ]
   }
    data4 = {
         "dpid": 1,
         "priority": 65535,
         "match": {
                  "vlan_vid": 1
         },
         "actions": [{
         "type": "POP_VLAN",
         "ethertype": 33024
         },
         {
         "type": "OUTPUT",
         "port": 2
         },
        ]
   }
    data5 = {
         "dpid": 2,
         "priority": 65535,
         "match": {
                  "in_port": 1
         },
         "actions": [{
         "type": "PUSH_VLAN",
         "ethertype": 33024
         },
         {
         "type": "SET_FIELD",
         "field": "vlan_vid",
         "value": 4096
         },
         {
         "type": "OUTPUT",
         "port": 3
        }
        ]
   }
   
    data6 = {
         "dpid": 2,
         "priority": 65535,
         "match": {
                  "in_port": 2
         },
         "actions": [{
         "type": "PUSH_VLAN",
         "ethertype": 33024
         },
         {
         "type": "SET_FIELD",
         "field": "vlan_vid",
         "value": 4097
         },
         {
         "type": "OUTPUT",
         "port": 3
        }
        ]
   }
    data7 = {
         "dpid": 2,
         "priority": 65535,
         "match": {
                  "vlan_vid": 0
         },
         "actions": [{
         "type": "POP_VLAN",
         "ethertype": 33024
         },
         {
         "type": "OUTPUT",
         "port": 1
         },
        ]
   }
    data8 = {
         "dpid": 2,
         "priority": 65535,
         "match": {
                  "vlan_vid": 1
         },
         "actions": [{
         "type": "POP_VLAN",
         "ethertype": 33024
         },
         {
         "type": "OUTPUT",
         "port": 2
         },
        ]
   }
   
    requests.post(url=url, json=data1, headers=headers, auth=requests.auth.HTTPBasicAuth('admin','admin'))
    requests.post(url=url, json=data2, headers=headers, auth=requests.auth.HTTPBasicAuth('admin','admin'))
    requests.post(url=url, json=data3, headers=headers, auth=requests.auth.HTTPBasicAuth('admin','admin'))
    requests.post(url=url, json=data4, headers=headers, auth=requests.auth.HTTPBasicAuth('admin','admin'))
    requests.post(url=url, json=data5, headers=headers, auth=requests.auth.HTTPBasicAuth('admin','admin'))
    requests.post(url=url, json=data6, headers=headers, auth=requests.auth.HTTPBasicAuth('admin','admin'))
    requests.post(url=url, json=data7, headers=headers, auth=requests.auth.HTTPBasicAuth('admin','admin'))
    requests.post(url=url, json=data8, headers=headers, auth=requests.auth.HTTPBasicAuth('admin','admin'))
    
@app.route('/delete_flow', methods=['Post'])  
def delete_flow():
    url = 'http://localhost:8080/stats/flowentry/clear/1'
    headers = {'Content-Type': 'application/json'}
    resp = requests.post(url=url, headers=headers, auth=requests.auth.HTTPBasicAuth('admin', 'admin'))
    data = json.loads(resp.text)
    return data
if __name__ == '__main__':
    app.run()
