import os


class CSVWriter:
    def __init__(self, filename="result.csv", directory="./output"):
        if not os.path.exists(directory):
            os.makedirs(directory)

        file_url = os.path.join(directory, filename)
        self.csv_file = open(file_url, "w")

    def write(self, data_to_write, end="\n"):
        data_in_string = [str(data) for data in data_to_write]
        concatenated_string_data = ",".join(data_in_string)
        self.csv_file.write("{}{}".format(concatenated_string_data, end))

    def write_2d(self, data_to_write):
        for data_row in data_to_write:
            self.write(data_row, end="\n")
