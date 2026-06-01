class ConversionRecord:
    def __init__(self, input_unit, input_value, output_unit, result):
        self.input_unit = input_unit
        self.input_value = float(input_value)
        self.output_unit = output_unit
        self.result = float(result)

    def to_list(self):
        return [self.input_unit, self.input_value, self.output_unit, self.result]

    # def print_record(self):
    #     print(f'{self.input_value} {self.input_unit} = {self.result} {self.output_unit}')

    def __str__(self):
        return f'{self.input_value} {self.input_unit} = {self.result} {self.output_unit}'