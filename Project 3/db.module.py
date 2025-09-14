import sqlite3


connection = sqlite3.connect('mft.db')
connection.close()

def save(id, title, teacher, unit):
    connection = sqlite3.connect('mft.db')
    connection.cursor().execute("insert into teachers_manegement (id,title,teacher,unit) values (?,?,?,?)",
                                [id, title, teacher, unit])
    connection.commit()
    connection.close()

def delete(id):
    connection = sqlite3.connect('mft.db')
    connection.cursor().execute("delete from teachers_manegement where id = ?", [id])
    connection.commit()
    connection.close()

def update(id, title, teacher, unit):
    connection = sqlite3.connect('mft.db')
    connection.cursor().execute("update teachers_manegement set teacher=?, title=?", [id])
    connection.commit()
    connection.close()