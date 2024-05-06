import optimization_methods.windows.Login as Login
# import optimization_methods.windows.UserWin as UserWindow
from PyQt6.QtGui import QAction, QKeySequence
from PyQt6.QtCore import QCoreApplication

def connect_signals(main_window_ui):

    # Calculate signal
    main_window_ui.calculate_btn.clicked.connect(calculate)

    # Change user signal
    main_window_ui.changeUser_menu.triggered.connect(change_user)
    main_window_ui.changeUser_menu.setShortcut(QKeySequence("Ctrl+c"))

    # Help signal
    main_window_ui.help_menu.triggered.connect(help)

    # Exit signal
    main_window_ui.exit_menu.triggered.connect(exit)
    main_window_ui.exit_menu.setShortcut(QKeySequence("Esc"))



def change_user(main_window_ui):
    QCoreApplication.instance().quit()
    app = Login.Login()
    app.mainloop()




def help(main_window_ui):
    print('helping...')

def exit(main_window_ui):
    QCoreApplication.instance().quit()


def calculate(main_window_ui):
    print('calculating...')