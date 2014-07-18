import os
from com import codesode

class FileWalker:
    def __init__(self):
        self.logger = TreeLogger()
        self.logger.debug("Initializing FileWalker.....")

    def execute(self, location):
        if location is None:
            self.logger.debug("Can not execute on empty location :")
        else:
            self.walk_directory(location)

    def walk_directory(self, location):
        #load list of directory in location
        for root, dirs, files in os.walk(location):
            location_logger = self.logger.branch("Root Directory : " + str(root))
            self.process_files(files, root, location_logger)


    def process_files(self, files, root, logger):
        """

        @param files:
        @param root:
        @param logger:
        """
        file_logger = logger.branch("Root Directory : " + str(root))

        for file in files:
            file_logger.debug("File : " + str(file))
            self.read_file(os.path.join(root, file), file_logger)

    def read_file(self, file, file_logger):
        """
        Read content of the file only if the file type is 'txt'.
        @param file: file to read
        """
        file_name, file_extension = os.path.splitext(file)
        if file_extension == '.txt':
            try:
                ofile = open(file, encoding="utf-8")

                file_content = ofile.read()
                output = open("C:/Users/vdube4/IdeaProjects/metapy/main/src/merged.log", 'a')
                output.write(file_content)

                output.close()
                ofile.close()
            except UnicodeDecodeError:
                file_logger.debug("Error in reading file " + file)


fw = FileWalker()
fw.execute("F:/me/recover")
fw.logger.show_tree()