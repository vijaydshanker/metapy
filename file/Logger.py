__project__ = "metapy"
__author__ = 'Vijay Shanker Dubey'

__name__ = "logger"

class TreeLogger:
    def __init__(self):
        self.logs = []
        self.log_label = "Root Log"
        self.branches = []
        self.indent = ""

    def show_tree(self):
        print(self.indent + self.log_label)

        for log in self.logs:
            print(self.indent + log)

        for branch in self.branches:
            branch.show_tree()

    def debug(self, message):
        self.logs.append(message)

    def branch(self, branch_label):
        #create new tree logger
        branch = TreeLogger()
        branch.log_label = branch_label
        branch.indent = self.indent + "\t"

        #update the tree; add new branch
        self.branches.append(branch)

        return branch
