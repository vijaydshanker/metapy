__project__ = "metapy"
__author__ = 'Vijay Shanker Dubey'

import os
import shutil

from file.Logger import TreeLogger


class GroupPolicy(object):
    default = "Default"
    copy_by_extension = "Group"

    def __init__(self):
        pass


class FileGroup:
    def __init__(self):
        #prepare logger.
        self.logger = TreeLogger()
        self.data = dict()

    def run(self, target_dir, policy=GroupPolicy.default):
        self.logger.debug("Executing file group operation.")

        #walk through directory.
        self.walk_directory(target_dir)

        #Prepare the report
        self.report(policy, target_dir="C:/Users/vdube4/IdeaProjects/metapy/data")

    def report(self, policy, target_dir):
        print_format = "{0:20} ==> {1:20}"

        if policy is GroupPolicy.default:
            print("==============================================================")
            print(print_format.format("File Extension", "File Count"))

            for ext in self.data.keys():
                print(print_format.format(ext, len(self.data.get(ext))))

            print("==============================================================")
        if policy is GroupPolicy.copy_by_extension:
            print("Copy file by extension group.")

            for ext in self.data.keys():
                target_path = target_dir + "/" + ext
                if not os.path.exists(target_path):
                    os.makedirs(target_path)

                for file in self.data.get(ext):
                    shutil.copy(file, target_path)

    def walk_directory(self, location):
        #load list of directory in location
        for root, dirs, files in os.walk(location):
            location_logger = self.logger.branch("Root Directory : " + str(root))
            self.process_files(files, root, location_logger)

    def process_files(self, files, root, logger):
        file_logger = logger.branch("Root Directory : " + str(root))

        for file in files:
            file_logger.debug("File : " + str(file))
            file_name, file_extension = os.path.splitext(file)

            files = self.data.get(file_extension)

            if files is None:
                files = list()

            files.append(os.path.join(root, file))

            self.data[file_extension] = files


fg = FileGroup()
fg.run(target_dir="F:/me/recover/", policy=GroupPolicy.copy_by_extension)