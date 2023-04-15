"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__ (self, path_to_file):
        """Reads dictionary and reports # items read"""
        dict_file = open(path_to_file)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")

    def __repr__ (self):
        return f"Words in this finder are: {self.words}"

    def parse (self, dict_file):
        """Parses dict_file for list of words"""
        return [word.strip() for word in dict_file]

    def random (self):
        """Returns random word"""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    4 words read

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True
    """

    def parse (self, dict_file):
        return [word.strip() for word in dict_file if word.strip() and not word.startswith('#')]
