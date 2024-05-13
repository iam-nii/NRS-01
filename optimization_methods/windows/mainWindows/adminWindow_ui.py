import sys
from PyQt6 import QtWidgets as qw, uic
from sqlalchemy import func
from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex
from optimization_methods.windows.utils import Database,User
from optimization_methods.windows.rootentry import RootEntry
import optimization_methods.windows.mainWindows.loginWindow_ui as Login
from PyQt6.QtWidgets import QApplication, QTableView, QVBoxLayout, QWidget, QLineEdit, QItemDelegate,QMessageBox,QDialog

edit_data = []
delete_data = []
table_ = ''

def editData(old,new,column):
    return [old,new,column]

class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data[1:] # Remove the first row from the data list
        self._headers = data[0] # Store the first row as the headers
    def rowCount(self, parent=QModelIndex()):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        # The length of the longest list
        return len(max(self._data,key=len))

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        # Display data
        if role == Qt.ItemDataRole.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            try:
                return self._data[index.row()][index.column()]
            except IndexError:
                return ''
    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        global edit_data
        try:
            if role == Qt.ItemDataRole.EditRole:
                edit_id = index.row()
                print('Edit role: ', index.row(), index.column())
                # old_value = self._data[index.row()][index.column()]
                # print('Old value: ', old_value)
                if not value:
                    return False
                try:
                    if index.column() != 0:
                        self._data[index.row()][index.column()] = value
                        self.dataChanged.emit(index, index)
                        row = index.row()
                        # print(self._data[row1])
                        column = self._headers[index.column()]
                        print('New value: ', value)
                        # print('Corresponding header: ', column)
                        edit_data = self._data[row]
                        print(edit_data)
                        # edit_data = editData(old=old_value,new=value,column=column)


                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
        return True

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return self._headers[section]

    def flags(self, index):
        if index.column() == 0:
            return super().flags(index)
        else:
            return super().flags(index) | Qt.ItemFlag.ItemIsEditable


class CustomDelegate(QItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def editorEvent(self, event, model, option, index):
        global delete_data
        if index.column() == 0:  # Check if the cell is in the first column
            value = model.data(index, Qt.ItemDataRole.DisplayRole)
            print('Cell clicked in the first column:', value)
            delete_data = [value]

        return super().editorEvent(event, model, option, index)

class AdminWindow(RootEntry):
    def __init__(self, app):
        super().__init__(app)
        self.app = app
        self.init_ui()
        self.database = Database()

    def init_ui(self):
        try:
            # self.window = uic.loadUi("./adminWindow_ui.ui")
            self.window = uic.loadUi("./windows/mainWindows/adminWindow_ui.ui")

            # Menu options
            self.change_user_menu: qw.QWidgetAction = self.window.change_user_menu.triggered.connect(self.change_user)
            self.exit: qw.QWidgetAction = self.window.exit_menu.triggered.connect(self.exit_menu_click)

            # Select Tables
            self.users_table:qw.QWidgetAction = self.window.select_users_tables_menu.triggered.connect(lambda: self.select_table("users"))
            self.tasks_table:qw.QWidgetAction = self.window.tasks_table_menu.triggered.connect(lambda: self.select_table("tasks"))
            self.solution_methods_table:qw.QWidgetAction = self.window.select_methods_table.triggered.connect(lambda: self.select_table("methods"))

            # Table view
            self.TABLE:qw.QTableView = self.window.table

            # Buttons
            self.edit_btn:qw.QPushButton = self.window.edit_btn
            self.edit_btn.clicked.connect(self.edit_btn_clicked)

            self.add_btn:qw.QPushButton = self.window.add_btn
            self.add_btn.clicked.connect(self.add_btn_clicked)

            self.delete_btn:qw.QPushButton = self.window.delete_btn
            self.delete_btn.clicked.connect(self.delete_btn_clicked)


            # Warning
            self.role_warning:qw.QLabel = self.window.role_warning
            self.role_warning.setStyleSheet("color: red")
            self.role_warning.setHidden(True)


        except Exception as e:
            print(e)

    def select_table(self,table):

        global table_

        if table == "users":
            table_ = 'users'

            users = [[user.id, user.username, user.role] for user in self.database.get_users()]
            if len(users) == 0:
                users.insert(0,[' ', ' '])
            users.insert(0,["id","Username","role"])

            print(users)

            delegate = CustomDelegate(self.TABLE)
            self.TABLE.setItemDelegate(delegate)
            data_model = TableModel(users)

            try:
                self.TABLE.setModel(data_model)
                self.TABLE.setColumnWidth(0, 100)  # Set the width of the first column to 100 pixels
                self.TABLE.setColumnWidth(1, 200)
                self.TABLE.setColumnWidth(2, 200)
            except Exception as e:
                print(e)


        if table == "tasks":
            table_ = "tasks"
            tasks = [[task.id, task.text] for task in self.database.get_tasks()]
            if len(tasks) == 0:
                tasks.insert(0,[' ',' '])
            tasks.insert(0,["ID","Task"])
            print(tasks)

            try:
                delegate = CustomDelegate(self.TABLE)
                self.TABLE.setItemDelegate(delegate)
                data_model = TableModel(tasks)
            except Exception as e:
                print(e)
            try:
                self.TABLE.setModel(data_model)
                self.TABLE.setColumnWidth(0, 100)  # Set the width of the first column to 100 pixels
                self.TABLE.setColumnWidth(1, 400)
            except Exception as e:
                print(e)

        if table == "methods":
            table_ = "methods"
            methods = [[method.id, method.text] for method in self.database.get_solution_methods()]
            if len(methods) == 0:
                methods.insert(0,[' ',' '])
            methods.insert(0,['ID',"Method"])
            print(methods)

            delegate = CustomDelegate(self.TABLE)
            self.TABLE.setItemDelegate(delegate)
            data_model = TableModel(methods)

            try:
                self.TABLE.setModel(data_model)
                self.TABLE.setColumnWidth(0, 100)  # Set the width of the first column to 100 pixels
                self.TABLE.setColumnWidth(1, 300)
            except Exception as e:
                print(e)



    def edit_btn_clicked(self):
        print("Editing...")
        try:
            print(edit_data)
            id = edit_data[0]
            username = edit_data[1]
            role = edit_data[2]

            session = self.database.session
            row = session.query(User).filter(User.id == id).first()
            if row:
                dlg = QMessageBox()
                dlg.setWindowTitle("Update user")
                dlg.setText(f"Are you sure you want to update the user with id: {id} ?")
                dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
                dlg.setIcon(QMessageBox.Icon.Question)
                button = dlg.exec()

                if button == QMessageBox.StandardButton.Yes:
                    print("Yes!")
                    row.username = username
                    if role.lower() != "пользователь" or role.lower() != "админ":
                        self.role_warning.setHidden(False)
                    else:
                        self.role_warning.setHidden(True)
                        row.role = role

                    session.commit()
                    # Refresh the table
                    users = [[user.id, user.username, user.role] for user in self.database.get_users()]
                    users.insert(0, ["id", "Username", "role"])
                    print(users)
                    data_model = TableModel(users)
                else:

                    print(button)

        except Exception as e:
            print(e)
    def add_btn_clicked(self):
        if table_ == 'users':
            try:
                self.add_user_dialog:qw.QDialog = uic.loadUi('./windows/mainWindows/add_user_dialog_ui.ui')
                self.add_user_dialog.setWindowTitle("Add a new User")

                self.username = self.add_user_dialog.findChild(QLineEdit, "username_txt")
                self.password = self.add_user_dialog.findChild(QLineEdit, "password_txt")
                self.role = self.add_user_dialog.findChild(qw.QComboBox, "role_cbx")

                # print((self.username, self.password, self.role))

                button = self.add_user_dialog.exec()
                try:
                    if button == 1:
                            username = self.username.text()
                            password = self.password.text()
                            role = self.role.currentText()
                            print((username,password,role))
                            if username or password != ' ':
                                print("adding...")
                                user = User(username,password,role)
                                self.database.session.add(user)
                                self.database.session.commit()
                                print('User successfully added...')

                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
        elif table_ == 'tasks':
            pass
        elif table_ == 'methods':
            pass
        else:
            return

    def delete_btn_clicked(self):
        global table_
        try:
            print("Deleting...")
            print(delete_data)
            id = delete_data[0]
            session = self.database.session
            row = session.query(User).filter(User.id == id).first()

            print(row)
            if table_ == "users":
                dlg = QMessageBox()
                dlg.setWindowTitle("Delete user")
                dlg.setText(f"Are you sure you want to delete the user with id: {id} ?")
                dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
                dlg.setIcon(QMessageBox.Icon.Question)
                button = dlg.exec()

                if button == QMessageBox.StandardButton.Yes:
                    if row:
                        session.delete(row)
                        session.commit()

                        # Find the maximum id value in the table
                        max_id = session.query(func.max(User.id)).scalar()

                        # Update the id values of all the rows with id values greater than the deleted row's id
                        try:
                            if max_id is not None:
                                for i in range(int(id), int(max_id)):
                                    row = session.query(TableName).filter(TableName.id == i + 1).first()
                                    if row:
                                        row.id = i
                                        session.commit()
                        except Exception as e:
                            print(e)

                    users = [[user.id, user.username, user.role] for user in self.database.get_users()]
                    users.insert(0, ["id", "Username", "role"])
                    print(users)
                    data_model = TableModel(users)

        except Exception as e:
            print(e)



    def change_user(self):
        print("Changin user...")
        self.login_window = Login.LoginWindow(self.app)
        self.login_window.window.show()
        self.window.close()

    def exit_menu_click(self):
        print("Exiting...")
        self.window.close()


# app = qw.QApplication(sys.argv)
# window = AdminWindow(app)
# window.window.show()
# app.exec()