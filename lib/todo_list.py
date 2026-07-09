class ToDo_list:
    def __init__(self, my_list=None):
        self.my_list = []

    def add(self, text):
        self.my_list.append(text)
        return self.my_list

    def mark_complete(self, text):
        self.my_list.remove(text)
        return self.my_list
