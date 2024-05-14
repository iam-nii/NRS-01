from polosin.windows.Login import Login
from polosin.public.Database_root import Database

try:
    database = Database()
    app = Login(database)
except Exception as e:
    print(e)
else:
    app.mainloop()