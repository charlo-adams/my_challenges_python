class ToyStore:
    def __init__(self):
        self.toy_list = []
 

    def add(self, text):
        if not isinstance(text, str):
            raise Exception("toy must be a string")
        self.toy_list.append(text)

    def see_toys(self):
        return self.toy_list