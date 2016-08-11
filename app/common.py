import os
import json

def process_data(data):
    dict_obj = json.loads(data)
   
    #print dict_obj["payload"]["app"]["name"]

    if dict_obj["event"] == "issue_impact_change":
        with open("/tmp/" + dict_obj["payload"]["app"]["name"]  + ".log", "a+") as myfile:
            myfile.write(data + "\n")
    return 
