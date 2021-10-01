from flask import Flask
from redis import Redis
import socket


app = Flask(__name__)
redis = Redis(host='redis', port=6379)
redis.set('hits', 0)

@app.route('/')
def hello():

    number = redis.get('hits')
    return 'Current counter number = {} \n'.format(number.decode('utf-8'))
        
@app.route('/stat')
def stat():
    count = redis.incr('hits')
    return 'Current counter number +1 = {} \n'.format(count)
    

@app.route("/about")
def about():
    
    html = "<h3>Hello, Nikita P!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)


