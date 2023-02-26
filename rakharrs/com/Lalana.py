import Helper


class Lalana:
    __name = ''
    __geom = ''
    __length = 0
    __width = 0

    def set_name(self, new_name):
        self.__name = str(new_name)

    def set_geom(self, geometry):
        self.__geom = str(geometry)

    def set_length(self, new_length):
        self.__length = Helper.validnumber(new_length)

    def set_width(self, new_width):
        self.__width = Helper.validnumber(new_width)

    def get_name(self):
        return self.__name

    def get_geom(self):
        return self.__geom

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width
