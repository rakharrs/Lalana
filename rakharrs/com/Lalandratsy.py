import Helper
from rakharrs.com.Lalana import Lalana


class Lalandratsy(Lalana):
    __kilometer_point1 = 0
    __kilometer_point2 = 0
    __level = 0

    def get_geom_lalandratsy(self, connection):
        percent1 = Helper.get_kp_percent(self.get_length(), self.get_kp1())
        percent2 = Helper.get_kp_percent(self.get_length(), self.get_kp2())
        return Helper.get_subline(connection, self.get_geom(), percent1, percent2)


    def set_level(self, new_level):
        temp = Helper.validnumber(new_level)
        self.__level = temp

    def set_kp1(self, kilometer_point):
        temp = Helper.validnumber(kilometer_point)
        self.__kilometer_point1 = temp

    def set_kp2(self, kilometer_point):
        temp = Helper.validnumber(kilometer_point)
        self.__kilometer_point2 = temp

    def get_kp1(self):
        return self.__kilometer_point1

    def get_kp2(self):
        return self.__kilometer_point2

    def get_level(self):
        return self.__level
