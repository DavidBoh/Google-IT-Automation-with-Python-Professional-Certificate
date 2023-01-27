#!/usr/bin/env python3
import emails2
import reports
import psutil
import shutil
import time
import socket
import os

sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
body = "Please check your system and resolve the issue as soon as possible"

def cpu_usage():

    cpu_percent = psutil.cpu_percent()
    if cpu_percent > 80:
        subject = "Error - CPU usage is over 80%"

        message = emails2.generate(sender, receiver, subject, body)
        emails2.send(message)


def available_disk():

    disk_usage = shutil.disk_usage("/")
    if disk_usage.percent < 20:
        subject = "Error - Available disk space is less than 20%"

        message = emails2.generate(sender, receiver, subject, body)
        emails2.send(message)
    
def available_memory():

    memory = psutil.virtual_memory()
    if memory.available < 500 * 1024 * 1024:
        subject = "Error - Available memory is less than 500MB"

        message = emails2.generate(sender, receiver, subject, body)
        emails2.send(message)

def hostname_error():

    try:
        hostname = "localhost"
        ip = socket.gethostbyname(hostname)
        if ip != "127.0.0.1":
            subject = "Error - localhost cannot be resolved to 127.0.0.1"

            message = emails2.generate(sender, receiver, subject, body)
            emails2.send(message)
    except socket.gaierror:
            subject = "Error - localhost cannot be resolved to 127.0.0.1"

            message = emails2.generate(sender, receiver, subject, body)
            emails2.send(message)

def main():
    while True:
        cpu_usage()
        available_disk()
        available_memory()
        hostname_error()
        time.sleep(60)
