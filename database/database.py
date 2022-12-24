

class Database:

    def __init__(self):
        self.tables = {}

    def create_table(self, table_name, column_map, index_map):
        if table.table_name in self.tables:
            raise Exception("Table_already_Exists")
        self.tables[table.table_name] = table

    def delete_table(self, table_name):
        if table_name not in self.tables:
            raise Exception(f"no_such_table_{table_name}")
        del self.tables[table_name]
