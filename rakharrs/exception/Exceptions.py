class PositiveValueException(Exception):
    name = 'value'

    def setName(self, new_value_name):
        self.name = str(new_value_name)

    def __int__(self, value_name):
        self.setName(value_name)
        super().__int__(value_name + ' has to be positive')
