import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")

def log_trace(event: str, **kwargs):
    msg = f"{event} | " + " | ".join(f"{k}={v}" for k, v in kwargs.items())
    logging.info(msg)
