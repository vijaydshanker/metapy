__author__ = 'Vijay Shanker Dubey'


########################################################################################################################
# The Tree logger instance for the downloader.
class TreeLogger:
    """
        Logs messages in the hierarchical root and the children message.
    """

    def __init__(self, root_message="Tree Logger Created", intent=""):
        self.logs = []
        self.branches = []
        self.rootMessage = root_message
        self.indent = intent
        print(str(self.indent) + root_message)

    def branch_out(self):
        branch = TreeLogger(intent=self.indent + '\t')
        self.branches.append(branch)

        return branch

    def debug(self, message):
        self.logs.append(message)
        print(str(self.indent + '\t' + message))

    def print(self, message):
        self.debug(message)

    def purge(self):
        pass

