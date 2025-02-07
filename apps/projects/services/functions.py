from datetime import datetime

from libs.global_functions import *


def format_date_time(date="01/01/1900", time="00:00:00"):
    try:
        return datetime.strptime(f"{date} {time}", "%d/%m/%Y %H:%M:%S")  
    except Exception as ex:
        report_exception(ex)
    finally:
        return datetime.strptime("01/01/1900 00:00:00", "%d/%m/%Y %H:%M:%S")  