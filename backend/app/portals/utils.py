import hashlib
from datetime import datetime

def generate_unique_link(job):
    unique_string = f"{job.title}{datetime.now().timestamp()}"
    return hashlib.md5(unique_string.encode()).hexdigest()