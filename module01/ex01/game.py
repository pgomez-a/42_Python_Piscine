class GotCharacter:
    def __init__(self, first_name, is_alive = True):
        """Initialize GotCharacter class"""
        self.first_name = first_name
        self.is_alive = is_alive
        return

class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good people."""
    def __init__(self, first_name = None, is_alive = True):
        """Initializes Stark class that inherits from GotCharacter class"""
        super().__init__(first_name = first_name, is_alive = is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"
        return

    def print_house_words(self):
        """Prints the House words"""
        print(self.house_words)
        return

    def die(self):
        """Changes the value of is_alive to False"""
        self.is_alive = False
        return
