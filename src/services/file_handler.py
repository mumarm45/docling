from core.text_splitter import Splitter
class FileHandler:
    """ FileHandler class is used to handle file operations """
    def __init__(self):
        self.splitter = Splitter()

    def get_file_content(self, file_path):
        """ Get file content """
        with open(file_path, 'r') as file:
            return file.read()
    def split_text(self, text, chunk_size, chunk_overlap):
        """ Split text into chunks """
        return self.splitter.chunk_transcript(text, chunk_size, chunk_overlap)
    def get_file_chunks(self, file_path, chunk_size, chunk_overlap):
        """ Get file chunks """
        text = self.get_file_content(file_path)
        return self.split_text(text, chunk_size, chunk_overlap)            