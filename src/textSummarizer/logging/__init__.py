import os
import sys
import logging

logging_str = '[%(asctime)s - %(levelname)s - %(module)s - %(message)s]'
log_dir = 'logs'
log_filepath = os.path.join(log_dir, 'text_summarizer.log')
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(filename=log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logging = logging.getLogger('text_summarizer')