from queue import Queue, Full
from typing import List


class MessageQueue:
    def __init__(self):
        self.clients: List[Queue] = []

    def subscribe(self):
        queue = Queue(maxsize=20)
        self.clients.append(queue)
        return queue

    def publish(self, msg):
        for i, queue in enumerate(self.clients):
            try:
                queue.put_nowait(msg)
            except Full:
                full_queue = self.clients[i]
                self.clients[i] = None
                del full_queue
        self.clients = [c for c in self.clients if c]  # Remove Nones


message_queue = MessageQueue()
temps_message_queue = MessageQueue()
