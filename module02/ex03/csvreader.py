class CsvReader(object):
    """
    CsvReader is a class that opens, reads and parses a CSV file
    """
    def __init__(self, filename = None, sep = ',', header = False, skip_top = 0, skip_bottom = 0):
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.filename = open(filename, 'r')
        self.content = list()
        for line in self.filename:
            split_line = line.rstrip().split(self.sep)
            self.content.append(split_line)
        return

    def __enter__(self):
        records_len = len(self.content[0])
        if records_len <= 3 or records_len >= 9:
            return None
        for item in self.content:
            if len(item) != records_len:
                return None
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_value != None:
            print("{}: {}".format(exception_type, exception_value))
        self.filename.close()
        return True

    def getdata(self):
        """
        Retrieves the data/records from skip_top to skip_bottom.
        Return:
                nested list (list(list, list, ...)) representing the data.
        """
        return self.content[self.skip_top:self.skip_bottom]

    def getheader(self):
        """
        Retrieves the header from csv file.
        Returns:
                list: representing the data (when self.header is True).
                None: (when self.header is False).
        """
        if self.header:
            return self.content[0]
        else:
            return None
