class Messages():
    def __init__(self):
        self.errors = []
        self.warnings = []

    def push_error(self, error):
        self.errors.append(error)

    def push_warning(self, warning):
        self.warnings.append(warning)
