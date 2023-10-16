```python
import time
from prometheus_client import start_http_server, Summary, Counter, Gauge

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
REQUEST_COUNTER = Counter('requests_total', 'Total requests')
ERROR_COUNTER = Counter('errors_total', 'Total errors')
ACTIVE_USERS = Gauge('active_users', 'Number of active users')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request():
    """A dummy function that takes some time."""
    time.sleep(1)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request()
        REQUEST_COUNTER.inc()  # Increment by 1
        ERROR_COUNTER.inc(2)  # Increment by given value
        ACTIVE_USERS.set(7)  # Set to a given value
        time.sleep(1)
```