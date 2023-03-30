from time import sleep
from threading import Thread
from threading import Event
from .producer import TripProducer


class TripThread(Thread):
  def __init__(self, minio_access_key = None, minio_secret_key = None):
    super().__init__()
    self._stop = Event()
    self.producer = TripProducer(minio_secret_key, minio_access_key)

  def stop(self):
    self._stop.set()

  def stopped(self):
    return self._stop.is_set()

  def run(self):
    while True:
      if self.stopped():
        return
      self.producer.send()
      sleep(1)
