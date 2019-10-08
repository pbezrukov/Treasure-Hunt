class Cell:
    """Class of cells values"""
    def __init__(self, value):
        """Initialize value of cell"""
        self.value = value
        self.__x = value // 10 - 1
        self.__y = value % 10 - 1

    @property
    def coordinates(self):
        """Coordinates of next cell"""
        return self.__x, self.__y
