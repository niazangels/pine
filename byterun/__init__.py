class VMException(Exception):
    pass


class VirtualMachine:
    def __init__(self):
        self.frame = None  # current frame
        self.frames = []  # call stack
        self.return_value = None
        self.last_exception = None

    def run_code(self, code, global_names=None, local_names=None):
        frame = self.make_frame(
            code, global_names=global_names, local_names=local_names
        )
        self.run_frame(frame)

    def make_frame(self, code, call_args={}, global_names=None, local_names=None):
        if globals is not None and local_names is not None:
            local_names = global_names
        elif self.frames:
            global_names = self.frame.global_names
            local_names = {}
        else:
            local_names = global_names = {
                "__builtins__": __builtins__,
                "__name__": "__main__",
                "__doc__": None,
                "__package__": None,
            }
        local_names.update(call_args)
        frame = Frame(code, global_names, local_names, self.frame)
        return frame

    def push_frame(self, frame):
        self.frames.append(frame)
        self.frame = frame

    def pop_frame(self):
        self.frames.pop()
        if self.frames:
            self.frame = self.frames[-1]
        else:
            self.frame = None

    def run_frame(self):
        pass


class Frame:
    def __init__(self, code_obj, global_names, local_names, prev_frame):
        self.code_obj = code_obj
        self.global_names = global_names
        self.local_names = local_names
        self.prev_frame = prev_frame
        self.stack = []
        self.block_stack = []
        self.last_instruction = 0
        if prev_frame:
            self.builtin_names = prev_frame.builtin_names
        else:
            self.builtin_names = local_names["__builtins__"]
            if hasattr(self.builtin_names, "__dict__"):
                self.builtin_names = self.builtin_names.__dict__

