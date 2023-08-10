class NeuroNetLibrary:
    def __init__(self):
        self.counter_msg = {"hello": 0, "hello_null": 0, "recommend_null": 0, 'recommend_default': 0}

    def counter(self, name, op=None):
        if op == "+":
            self.counter_msg[name] += 1
        if str(op).isdigit():
            self.counter_msg[name] = op
        return self.counter_msg[name]