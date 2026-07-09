class GrammarStats:
    def __init__(self):
        self.text = None
        self.percentage = 0

    def check(self, text):
        ending_grammar = ['!', '.', '?']
        if any(char in ending_grammar for char in text[-1]) and text[0].isupper():
            self.percentage = 100
            return True
        elif any(char in ending_grammar for char in text[-1]) or text[0].isupper():
            self.percentage = 50
            return "Your grammar is a bit off"
        else:
            self.percentage = 0
            return False
         # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        

    def percentage_good(self):
        return self.percentage

        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        
