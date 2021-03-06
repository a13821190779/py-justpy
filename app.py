#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import sys
import time
import subprocess

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def log(s):
    print('[Monitor]', s)


class MyFileSystemEventHander(FileSystemEventHandler):
    def __init__(self, fn):
        super(MyFileSystemEventHander, self).__init__()
        self.restart = fn

    def on_any_event(self, event):
        if event.src_path.endswith('.py'):
            print('\n')
            log('Python source file changed: %s' % event.src_path)
            self.restart()


command = ['echo', 'ok']
process = None


def kill_process():
    global process
    if process:
        log('Kill process [%s]...' % process.pid)
        process.kill()
        process.wait()
        log('Process ended with code %s.' % process.returncode)
        process = None


def start_process():
    global process, command
    log('Start process %s...' % ' '.join(command))
    print('========================================')
    print('========================================')
    print('\n')
    process = subprocess.Popen(
        command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)


def restart_process():
    kill_process()
    start_process()


def start_watch(path, callback):
    observer = Observer()
    observer.schedule(
        MyFileSystemEventHander(restart_process), path, recursive=True)
    observer.start()
    log('Watching directory %s...' % path)
    start_process()
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == '__main__':
    argv = sys.argv[1:]
    print(argv)
    if not argv:
        print('用法：./app.py src/index.py')
        exit(0)
    if argv[0] != 'python':
        argv.insert(0, 'python3')
    command = argv
    path = os.path.abspath('.')
    start_watch(path, None)
