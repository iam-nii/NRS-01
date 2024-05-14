from polosin.windows.Login import Login

try:
    app = Login()
except Exception as e:
    print(e)
else:
    app.mainloop()