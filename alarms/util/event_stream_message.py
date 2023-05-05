class EventStreamMessage:
    def __init__(self, msg, event=None) -> None:
        self.msg = msg
        self.event = event

    def __str__(self):
        msg = f"data: {self.msg}\n\n"
        if self.event:
            return f"event: {self.event}\n{msg}"
        return msg
