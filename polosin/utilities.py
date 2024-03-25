from sqlalchemy import select, create_engine, Column, PrimaryKeyConstraint, String, Integer, CHAR, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from cryptography.fernet import Fernet

KEY = b'4bZCJ0pWMDgVco8ejOR-L9UDMUVEbBjxLCQc5E7t4mY='
print("key:")
print(KEY)

class EncDecPass:
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
        return self.fernet.decrypt(encoded_password)


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String, unique=True)
    password = Column('password', String)
    role = Column('role', String)

    def __init__(self, username, password, role):
        self.username = username
        self.password = EncDecPass().encrypt_password(password)
        self.role = role

    def __repr__(self):
        return f"({self.id}) {self.username} {self.role}"


class Chanel(Base):
    __tablename__ = 'chanel'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    width = Column('width', Float)
    depth = Column('depth', Float)
    length = Column('length', Float)

    def __init__(self, width, depth, length):
        self.width = width
        self.depth = depth
        self.length = length

    def __repr__(self):
        return f"({self.width}) {self.depth} {self.length}"


class Material(Base):
    __tablename__ = 'material'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    density = Column('density', Integer)
    heat_capacity = Column('heat_capacity', Integer)
    melting_temperature = Column('melting_temperature', Integer)

    def __init__(self, density, heat_capacity, melting_temperature):
        self.density = density
        self.heat_capacity = heat_capacity
        self.melting_temperature = melting_temperature

    def __repr__(self):
        return f"({self.density}) {self.heat_capacity} {self.melting_temperature}"


class ProcessParams(Base):
    __tablename__ = 'process_params'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    cover_speed = Column('cover_speed', Float)
    cover_temperature = Column('heat_capacity', Integer)

    def __init__(self, cover_speed, cover_temperature):
        self.cover_speed = cover_speed
        self.cover_temperature = cover_temperature

    def __repr__(self):
        return f"({self.cover_speed}) {self.cover_temperature}"


class MathModel(Base):
    __tablename__ = 'math_model'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    consistency_coefficient = Column('consistency_coefficient', Integer)
    temp_viscosity_coefficient = Column('temp_viscosity_coefficient', Float)
    casting_temperature = Column('casting_temperature', Integer)
    flow_index = Column('flow_index', Float)
    cover_heat_transfer_coefficient = Column('cover_heat_transfer_coefficient', Integer)

    def __init__(self, consistency_coefficient, temp_viscosity_coefficient, casting_temperature, flow_index,
                 cover_heat_transfer_coefficient):
        self.consistency_coefficient = consistency_coefficient
        self.temp_viscosity_coefficient = temp_viscosity_coefficient
        self.casting_temperature = casting_temperature
        self.flow_index = flow_index
        self.cover_heat_transfer_coefficient = cover_heat_transfer_coefficient

    def __repr__(self):
        return (f"({self.consistency_coefficient}) {self.temp_viscosity_coefficient}{self.casting_temperature}"
                f"{self.flow_index}{self.cover_heat_transfer_coefficient}")


class Database:
    def __init__(self):
        # Creating the database file
        self.engine = create_engine("sqlite:///chemresearch.db", echo=True)

        # Take all the classes that extends from base and create the tables
        Base.metadata.create_all(bind=self.engine)

        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def select_user(self, user: User, username):

        row = self.session.query(User).filter(User.username == username).first()
        print(f"All users {self.get_users()}")
        return row

    def get_users(self):
        # # query the data from the table
        # users = session.query(User).all()
        # for user in users:
        #     print(user.id, user.name, user.age)
        users = self.session.query(User).all()
        print(users)
        return users

