from sqlalchemy import create_engine, Column, PrimaryKeyConstraint, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from cryptography.fernet import Fernet


class EncDecPass():
    def __init__(self):
        # generate a key for encryption and decryption
        # You can use fernet to generate the key or use random key generator
        # here I'm using fernet to generate key
        self.key = Fernet.generate_key()

        # Instance the Fernet class with the key
        self.fernet = Fernet(self.key)

    def encrypt_password(self, password):
        # then use the Fernet class instance
        # to encrypt the string string must
        # be encoded to byte string before encryption
        return self.fernet.encrypt(password.encode())

    def decrypt_password(self, encoded_password):
        return self.fernet.decrypt(self.encoded_password).decode()

Base = declarative_base()

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

class Database():
    def __init__(self):
        # Creating the database file
        self.engine = create_engine("sqlite:///optimization.db", echo=True)

        # Take all the classes that extends from base and create the tables
        Base.metadata.create_all(bind=self.engine)

        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()







