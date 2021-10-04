import pytz
from datetime import datetime


def get_current_date():
    return datetime.now(pytz.timezone("America/Sao_Paulo"))
