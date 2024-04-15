from sqlalchemy import select,create_engine, Column, PrimaryKeyConstraint, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session
from cryptography.fernet import Fernet
from sqlalchemy.engine import reflection
import customtkinter as c

KEY = b'4bZCJ0pWMDgVco8ejOR-K9UDMUVEbBjxLCQc5E7t4mY='

class EncDecPass():
    def __init__(self):
        # generate a key for encryption and decryption
        # You can use fernet to generate the key or use random key generator
        # here I'm using fernet to generate key
        self.key = KEY
        # Instance the Fernet class with the key
        self.fernet = Fernet(self.key)

    def encrypt_password(self, password):
        # then use the Fernet class instance
        # to encrypt the string string must
        # be encoded to byte string before encryption
        return self.fernet.encrypt(password.encode())

    def decrypt_password(self, encoded_password):
        return self.fernet.decrypt(encoded_password)#.decode()

Base = declarative_base()

class User_Table:

    def __init__(self, root,table,columns:int):

        self.root = root
        self.users_dict = {}
        # Header row
        self.label = c.CTkLabel(self.root, width=100, height=30, text='id', fg_color='grey',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=0, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(self.root, width=300, height=30, text='Username', fg_color='grey',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=1, padx=1, pady=1)  # position the entry within the frame

        self.label = c.CTkLabel(self.root, width=300, height=30, text='Role', fg_color='grey',
                              text_color='white', font=('Arial', 16, 'bold'))
        self.label.grid(row=0, column=2, padx=1, pady=1)  # position the entry within the frame

        username_label_list: list[c.CTkLabel] = []
        role_label_list: list[c.CTkLabel] = []
        id_label_list: list[c.CTkLabel] = []


        # code for creating table
        for i in range(len(table)):
            for j in range(columns + 1):
                if j == 1:
                    self.label1 = c.CTkLabel(root, width=300, height=30,text=f'{table[i].username}', fg_color='grey',
                                          text_color='white',font=('Arial', 16, 'bold'),)
                    self.label1.grid(row=i+1, column=j, padx=1, pady=1)  # position the entry within the frame
                    # self.label.user = table[i]  # add a new attribute to the label to store the user object
                    username_label_list.append(self.label1)
                    # self.label1.bind('<Button-1>',lambda e,label = self.label1: self.on_label_click(self.label1))
                    # users_dict[table[i].username] = self.label # associate the user object with the label
                elif j == 2:
                    self.label2 = c.CTkLabel(root, width=300, height=30, text=f'{table[i].role}',fg_color='grey',
                                          text_color='white',font=('Arial', 16, 'bold'))
                    self.label2.grid(row=i+1, column=j, padx=1, pady=1)  # position the entry within the frame
                    # users_dict[table[i].username] = self.label # associate the user object with the label
                    role_label_list.append(self.label2)
                else:
                    self.label3 = c.CTkLabel(root, width=100, height=30, text=f'{i+1}', fg_color='grey',
                                          text_color='white', font=('Arial', 16, 'bold'))
                    self.label3.grid(row=i+1, column=j, padx=1, pady=1)  # position the entry within the frame
                    id_label_list.append(self.label3)

        for i in range(len(username_label_list)):
            self.users_dict[i] = {
                'username': username_label_list[i].cget('text'),
                'role': role_label_list[i].cget('text'),
                'id':id_label_list[i].cget('text'),
            }
        print(self.users_dict)

        for label in username_label_list:
            label.bind('<Button-1>',lambda e,label = label: self.on_label_click(label))

    def on_label_click(self,label:c.CTkLabel):
        username = label.cget('text')
        role = ' '
        id = ' '
        print(username)
        for key in self.users_dict:
            value = self.users_dict[key]
            if value['username'] == username:
                id = value['id']
                role = value['role']


        self.root.winfo_toplevel().table_id.configure(text=id, text_color='black')
        # Username
        entry:c.CTkEntry = self.root.winfo_toplevel().table_username
        entry.delete(0,c.END)
        entry.insert(0,username)

        # role
        role_entry:c.CTkEntry = self.root.winfo_toplevel().table_role
        role_entry.delete(0,c.END)
        role_entry.insert(0,role)
        # self.root.winfo_toplevel().table_username.configure(text=username, text_color='black',width=100)
        # self.root.winfo_toplevel().table_role.configure(text=role, text_color='black',width=100)





class User(Base):
    __tablename__ = 'users'

    id = Column('id',Integer, primary_key=True,autoincrement=True)
    username = Column('username',String,unique=True)
    password = Column('password',String)
    role = Column('role', String)

    def __init__(self,username,password,role):
        self.username = username
        self.password = EncDecPass().encrypt_password(password)
        self.role = role

    def __repr__(self):
        return f"({self.id}) {self.username} {self.role}"


class SolutionMethods(Base):
    __tablename__ = 'solution_methods'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('method', String, unique=True)
    password = Column('password', String)
    role = Column('role', String)





class Database():
    def __init__(self):
        # Creating the database file
        self.engine = create_engine("sqlite:///optimization.db", echo=True)

        # Take all the classes that extends from base and create the tables
        Base.metadata.create_all(bind=self.engine)

        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def select_user(self, user: User,username):
        row = self.session.query(User).filter(User.username == username).first()
        print(f"All users {self.get_users()}")
        return row

    def get_users(self):
        # # query the data from the table
        # users = session.query(User).all()
        # for user in users:
        #     print(user.id, user.name, user.age)
        users = self.session.query(User).all()
        return [users,2]

    def get_tables(self):
        insp = reflection.Inspector.from_engine(self.engine)
        # Return the table names
        return insp.get_table_names()
