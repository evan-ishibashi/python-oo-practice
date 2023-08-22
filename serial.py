class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Create serial with start and current initialized to start - 1"""
        self.start = start - 1
        self.current = start - 1
    
    def __repr__(self):
        return f"""<Serial Generator, creates unique integer values 
        beginning at start={self.start},
        and tracking current={self.current}>"""

    def generate(self):
        """Increment current value by one"""
        self.current += 1
        return self.current

    def reset(self):
        """Resets current value to start value"""
        self.current = self.start
