import sqlite3
from main import Interface

boolElem = None
def login(login, passw, signal):
    con = sqlite3.connect('datebase/SystemSecurity.db')
    cur = con.cursor()

    # Проверяем есть ли такой пользователь
    cur.execute(f'SELECT * FROM user WHERE lagin="{login}";')
    value = cur.fetchall()
    
    if value != [] and value[0][2] == passw:
        # signal.emit("Access")
        boolElem = 1
    else:
        signal.emit('Проверьте правильность ввода данных!')
        boolElem = 0

    cur.close()
    con.close()
    return boolElem

# def register(login, passw, signal):
#     con = sqlite3.connect('handler/users')
#     cur = con.cursor()

#     cur.execute(f'SELECT * FROM users WHERE name="{login}";')
#     value = cur.fetchall()

#     if value != []:
#         signal.emit('Такой ник уже используется!')

#     elif value == []:
#         cur.execute(f"INSERT INTO users (name, password) VALUES ('{login}', '{passw}')")
#         signal.emit('Вы успешно зарегистрированы!')
#         con.commit()

#     cur.close()
#     con.close()