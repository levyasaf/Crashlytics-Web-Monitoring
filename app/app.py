from flask import Flask, request, jsonify
from rq import Queue
from redis import Redis
from common import *

redis_conn = Redis()
q = Queue(connection=redis_conn)

app = Flask(__name__)

@app.route('/cwm', methods=['POST'])
def get_data():
    data = request.get_data()
    print data
    job = q.enqueue(process_data, data, result_ttl=86400)
    return jsonify({"job": job.id}), 200

@app.route('/result/<job_id>', methods=['GET'])
def get_job(job_id):
    job = q.fetch_job(job_id)
    try:
        return jsonify(job.result)
    except:
        return jsonify({"answer": "None"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
