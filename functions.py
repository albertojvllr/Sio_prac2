
def execute_query(cursor, query):
        cursor.execute(query)
        result = cursor.fetchall()

        for row in result:
            print(row)
        return result

def read_sql_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()