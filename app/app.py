import logging
import random
import time
from flask import Flask

app = Flask(__name__)

logging.basicConfig(
    filename='/var/log/app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

@app.route('/')
def home():
    return "Log Monitoring App Running"

def generate_logs():
    while True:
        log_type = random.choice(['INFO', 'WARNING', 'ERROR'])
        
        if log_type == 'INFO':
            logging.info("This is an INFO log")
        elif log_type == 'WARNING':
            logging.warning("This is a WARNING log")
        else:
            logging.error("This is an ERROR log")

        time.sleep(5)

if __name__ == '__main__':
    import threading
    t = threading.Thread(target=generate_logs)
    t.start()
    app.run(host='0.0.0.0', port=5000)

    