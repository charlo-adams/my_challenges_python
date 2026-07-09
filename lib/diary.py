class DiaryEntry:
    def __init__(self, title=None, contents=None):
        self.title = title
        self.contents = contents
        # Parameters:
        #   title: string
        #   contents: string
       

    def format(self):
        if self.contents is None or self.title is None:
            raise ValueError("nothing entered")
        formated = self.title + ": " + self.contents
        return formated
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        

    def count_words(self):
        length = len(self.format().split())
        return length
        # Returns:
        #   int: the number of words in the diary entry
        

    def reading_time(self, wpm):
        words = self.contents.split()
        word_count = len(words)
        return int(word_count / wpm)
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        words_can_read = wpm * minutes
        words = self.contents.split()
        chunk_words = words[:words_can_read]
        return " ".join(chunk_words)
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        pass
