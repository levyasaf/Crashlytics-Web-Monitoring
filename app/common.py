import os
import json
import datetime

def process_data(data):
    dict_obj = json.loads(data)
    now = datetime.datetime.now()   
    event_type = dict_obj["event"]
    app_name = dict_obj["payload"]["app"]["name"]
    
    if event_type == "issue_impact_change":
        with open("/tmp/" + app_name  + ".log", "a+") as myfile:
            myfile.write(now.strftime("%Y-%m-%d %H:%M") + ";" + app_name + ";" + data + "\n")
    return 
