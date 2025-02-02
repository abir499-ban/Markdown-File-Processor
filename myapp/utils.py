from datetime import datetime
import re


def extract_datetime_fromFileName(filename):
    match = re.search(r'_(\d{8}_\d{6})\.md$', filename)
    if match:
        datetime_str = match.group(1)
        extracted_date = datetime.strptime(datetime_str , "%Y%m%d_%H%M%S") 
        return extracted_date
    else:
        return None