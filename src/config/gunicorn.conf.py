import os
import signal


def worker_int(worker):
    os.kill(worker.pid, signal.SIGINT)
