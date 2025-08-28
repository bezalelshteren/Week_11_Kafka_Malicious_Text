


class Cat_data_by_antisemitic:
    def __init__(self,):
        self.data_table = None
        self.antisemitic ,self.not_antisemitic = None,None

    def cat_data(self,df):
        self.data_table = df
        self.antisemitic = self.data_table[self.data_table["Antisemitic"] == 1]
        self.not_antisemitic = self.data_table[self.data_table["Antisemitic"] == 0]
        return self.antisemitic ,self.not_antisemitic