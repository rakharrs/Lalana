from ..database import Connection


def validnumber(value):
    try:
        temp_value = float(value)
        if temp_value < 0:
            raise Exception("new length has to be positive !")
        else:
            return temp_value
    except ValueError:
        raise Exception("Length need to be a number !")


def get_kp_percent(road_length, kilometer_point):
    return (100 * kilometer_point) / road_length


def get_gis_length(connection, geometry):
    query = "SELECT ST_Length('" + geometry + "'::geography)"
    return Connection.select_first(connection, query)


def get_subline(connection, road_geometry, percent1, percent2):
    geom = str(road_geometry)
    pk1 = validnumber(percent1)/100
    pk2 = validnumber(percent2)/100
    query = "SELECT " \
            "ST_astext(ST_LineSubstring(ST_LineMerge(the_line), " + str(pk1) + ", " + str(pk2) + ")) " \
            "FROM (SELECT ST_GeomFromEWKT('" + road_geometry + "') as the_line) As foo"
    return Connection.select_first(connection, query)


def get_coords(connection, road_geometry, percent):
    geom = str(road_geometry)
    pk = validnumber(percent)/100
    query = "SELECT " \
            "ST_AsEWKT(ST_LineInterpolatePoint(ST_LineMerge(the_line), " + str(pk) + ")) FROM " \
            "(SELECT ST_GeomFromEWKT('" + road_geometry + "') as the_line) As foo"
    return Connection.select_first(connection, query)
