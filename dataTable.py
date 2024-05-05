class DataTable:
    def __init__(self, csv_file):
        self.data = []
        self.load_data(csv_file)

    def load_data(self, csv_file):
        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                self.data.append(row)

    def get_data(self):
        return self.data