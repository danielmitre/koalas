
class table:
    """
    This class abstracts a table of some data
    The first line should be table's head
    Each line of data is a table line
    """

    def __init__(self, data):
        """
        Args:
            data (iterable of iterable): the values that you want to plot in the table
        """
        self.data = data
        self.sizes = [0 for _ in data[0]]
        self._calculate_sizes()

    def _calculate_sizes(self):
        for line in self.data:
            for col in range(len(line)):
                self.sizes[col] = max(self.sizes[col], len(str(line[col])))
        #self.sizes[0] += 1

    def _show(self, line):
        for col in range(len(self.data[line])):
            formatter = "{0:^%d}" % (self.sizes[col])
            if col == 0:
                formatter = " "+formatter
            print formatter.format(self.data[line][col]),
            print '|',
        if line>0:
            print ""
        else:
            n_lines = len(self.data[0])
            print "\n"+"="*(sum(self.sizes))+"==="*len(self.sizes)


    def show(self):
        for line in range(len(self.data)):
            self._show(line)

    @staticmethod
    def show_from_data(data):
        temp = table(data)
        temp.show()



'''
### Example of usage of table
info = [
        ["Nome", "Idade", "Curso"],
        ["Fulano", 20, "Engenharia"],
        ["Cicrano", 31, "Letras"],
        ["Genoveva Antao Bezerra", float('inf'), "Biologia"]
       ]
table.show_from_data(info)
'''
