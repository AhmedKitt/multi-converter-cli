import csv
from ConversionRecord import ConversionRecord
class ConversionsHistory:
    FILE_HEADER = ["Input Unit", "Input Value", "Output Unit", "Result"]
    FILE_NAME = "conversions_history.csv"

    def __init__(self):
        self.records_list = self._init_history_file()

    def append_record(self, record: ConversionRecord) -> None:
        self.records_list.append(record)
        self._append_record_to_csv(record)


    def __str__(self):
        if not self.records_list:
            return ("The Conversion History Is Empty")
        data = []
        for index, item in enumerate(self.records_list, start=1):
            data.append(f'{index}. {item.input_value:0.2f} {item.input_unit} '
                        f'= {item.result:0.2f} {item.output_unit}')
        return "\n".join(data)

    def _append_record_to_csv(self, record: ConversionRecord) -> None:
        with open(self.FILE_NAME, "a", newline='') as file:
            writer = csv.writer(file)
            row = record.to_list()
            writer.writerow(row)

    def _init_history_file(self) -> list:
        if self._is_history_file_valid():
            return self._load_conversion_history()
        else:
            self.reset_history_file()
            return []

    def _is_history_file_valid(self) -> bool:
        try:
            with open(self.FILE_NAME, "r", newline='') as file:
                reader = csv.reader(file)
                header = next(reader, None)
                if header != self.FILE_HEADER:
                    return False
                try:
                    for row in reader:
                        float(row[1])
                        float(row[3])
                    return True
                except (ValueError, IndexError):
                    return False
        except FileNotFoundError:
            return False

    def _load_conversion_history(self) -> list:
        conversion_history = []
        with open(self.FILE_NAME, "r", newline='') as file:
            reader = csv.reader(file)
            next(reader) #to skip header of csv file
            for row in reader:
                record = ConversionRecord(*row)
                conversion_history.append(record)
            return conversion_history

    def reset_history_file(self) -> None:
        with open(self.FILE_NAME, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.FILE_HEADER)