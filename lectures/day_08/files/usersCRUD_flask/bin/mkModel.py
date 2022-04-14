import os, sys

# params = sys.argv

def make_model(schema_name, table_name, params):
    filename = f"./{table_name}.py"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'a') as f:
        f.write('from mysqlconnection import connectToMySQL\n\n')
        f.write(f'DATABASE = "{schema_name}"\n\n')
        f.write(f"class {table_name.capitalize()}:\n\n")
        f.write("    def __init__(self, data):\n")
        f.write("        self.id = data['id']\n")
        for val in params:
            f.write(f"        self.{val} = data['{val}']\n")
        f.write("        self.created_at = data['created_at']\n")
        f.write("        self.updated_at = data['updated_at']\n\n")
        f.write("    @classmethod\n")
        f.write("    def get_all(cls):\n")
        f.write(f"        query = 'SELECT * FROM {table_name}s;'\n")
        f.write("        results = connectToMySQL(DATABASE).query_db(query)\n")
        f.write("        return [cls(result) for result in results]\n\n")
        f.write("    @classmethod\n")
        f.write("    def save(cls, data):\n")
        f.write(f'        query = "INSERT INTO {table_name}s (')
        for val in params:
            f.write(val)
            if val == params[-1]:
                f.write(")")
            else:
                f.write(", ")
        f.write(' values (')
        for val in params:
            f.write(f"%({val})s")
            if val == params[-1]:
                f.write(")")
            else:
                f.write(", ")
        f.write(';"\n')
        f.write("        return connectToMySQL(DATABASE).query_db(query,data)\n\n")
        f.write("    @classmethod\n")
        f.write(f'    def get_one(cls, data:dict) -> object:\n')
        f.write(f"        query = 'SELECT * FROM {table_name}s")
        f.write(" WHERE id = %(id)s;'\n")
        f.write('        result = connectToMySQL(DATABASE).query_db(query, data)\n')
        f.write('        return cls(result[0])\n\n')
        f.write("    @classmethod\n")
        f.write(f'    def update(cls, data:dict) -> object:\n')
        f.write(f"        query = 'UPDATE {table_name}s SET ")
        for val in params:
            f.write(f"{val}=%({val})s")
            f.write(", ")
        f.write("updated_at=NOW() WHERE id = %(id)s")
        f.write(";'\n")
        f.write('        return connectToMySQL(DATABASE).query_db(query, data)\n\n')
        f.write("    @classmethod\n")
        f.write(f'    def destroy(cls, data:dict) -> object:\n')
        f.write(f"        query = 'DELETE FROM {table_name}s")
        f.write(" WHERE id = %(id)s;'\n")
        f.write('        return connectToMySQL(DATABASE).query_db(query, data)\n')







make_model('users', sys.argv[1], sys.argv[2:])
