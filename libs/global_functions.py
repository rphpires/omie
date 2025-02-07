import sys
import platform
import traceback
import threading
import os

from time import sleep
from datetime import datetime, timedelta


class GlobalInfo:
    gmt_timedelta = timedelta(hours=0)
    gmt_offset = -180


def str_truncate(s, max_len):
    if type(s) is str and len(s) > max_len:
        return f"{s[:max_len-5]}...[{len(s)}]"
    else:
        return s


def remove_accents_from_string(s):
    chars_table = {}

    if not s:
        return ''

    if not isinstance(s, str):
        error(f'remove_special_characters_from_string: not string= {s}')
        return ''

    chars_table = {
        192: 'A', 193: 'A', 194: 'A', 195: 'A', 196: 'A', 197: 'A', 199: 'C', 200: 'E', 201: 'E', 202: 'E',
        203: 'E', 204: 'I', 205: 'I', 206: 'I', 207: 'I', 210: 'O', 211: 'O', 212: 'O', 213: 'O', 214: 'O',
        217: 'U', 218: 'U', 219: 'U', 220: 'U', 224: 'a', 225: 'a', 226: 'a', 227: 'a', 228: 'a', 229: 'a',
        231: 'c', 232: 'e', 233: 'e', 234: 'e', 235: 'e', 236: 'i', 237: 'i', 238: 'i', 239: 'i', 240: 'o',
        241: 'n', 242: 'o', 243: 'o', 244: 'o', 245: 'o', 246: 'o', 249: 'u', 250: 'u', 251: 'u', 252: 'u',
        253: 'y', 255: 'y', 160: ' ',
    }

    e = ''
    for c in s:
        if ord(c) <= 128:
            e += c
        else:
            e += chars_table.get(ord(c), '_')
    return e


## Datetime

def get_localtime():
    if is_windows():
        return datetime.utcnow() + GlobalInfo.gmt_timedelta
    else:
        return datetime.today() + GlobalInfo.gmt_timedelta


def get_utctime():
    if is_windows():
        return datetime.utcnow()
    else:
        return datetime.today() - GlobalInfo.gmt_timedelta


def format_date(x: datetime) -> str:
    if not x:
        return "-"
    return "%04d-%02d-%02d %02d:%02d:%02d.%03d" % (x.year, x.month, x.day, x.hour, x.minute, x.second, x.microsecond / 1000)

## Check OS Plataform

def is_windows():
    return True if platform.system() == "Windows" else False


def is_linux():
    return True if platform.system() == "Linux" else False


def check_os():
    os_type = platform.system()
    if os_type == "Windows":
        return "Windows"
    elif os_type == "Linux":
        return "Linux"
    elif os_type == "Darwin":
        return "MacOS"
    else:
        return f"Unknown: {os_type}"


from .tracer import Tracer
tracer = Tracer()


def trace(msg):
    tracer.trace_message(remove_accents_from_string(msg))


def trace_elapsed(msg, reference_utc_time):
    delta = datetime.utcnow() - reference_utc_time
    if 'total_seconds' not in dir(delta):
        tracer.trace_message(msg)
        return
    elapsed_ms = int((delta).total_seconds() * 1000)
    msg += " (%d ms)" % (elapsed_ms)
    tracer.trace_message(msg)


def info(msg):
    tracer.trace_message(msg)


def error(msg):
    tracer.trace_message("****" + msg)
    x = get_localtime()
    d = "%04d/%02d/%02d %02d:%02d:%02d.%06d " % (x.year, x.month, x.day, x.hour, x.minute, x.second, x.microsecond)
    sys.stderr.write("ERROR" + d + msg + '\n')
    sys.stdout.write("ERROR" + d + msg + '\n')


try:
    ERROR_LOG_FILE = "logs/ErrorLog.txt"
    # if not os.path.exists(ERROR_LOG_FILE):
    #     with open(ERROR_LOG_FILE, 'w') as arquivo:
    #         pass
except Exception as ex:
    print(ex)


def report_exception(e, do_sleep=True):
    x = get_localtime()
    header = "\n\n************************************************************************\n"
    header += "Exception date: %04d/%02d/%02d %02d:%02d:%02d.%06d \n" % (x.year, x.month, x.day, x.hour, x.minute, x.second, x.microsecond)
    # header += f"Version {CONTROLLER_VERSION}\n"
    header += "\n"

    sys.stdout.write(header)
    sys.stderr.write(header)
    traceback.print_exc(file=sys.stdout)
    if is_windows():
        f = open(ERROR_LOG_FILE, 'a')
        f.write(header)
        traceback.print_exc(file=f)
        f.close()
    else:
        traceback.print_exc(file=sys.stderr)

    try:
        t = "{}".format(type(threading.currentThread())).split("'")[1].split('.')[1]
    except IndexError:
        t = 'UNKNOWN'

    error("Bypassing exception at %s (%s)" % (t, e))
    error("**** Exception: <code>%s</code>" % (traceback.format_exc(), ))
    if do_sleep:
        error("Sleeping 2 seconds")
        sleep(2.0)


## Comm

def cleanup_mei_temporary_path():
    ...
