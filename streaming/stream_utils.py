# streaming/stream_utils.py
import time

def stream_text(text):
    for word in text.split():
        yield word + " "
        time.sleep(0.05)
