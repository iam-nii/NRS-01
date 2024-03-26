from sqlalchemy import select, create_engine, Column, PrimaryKeyConstraint, String, Integer, CHAR, Float
from sqlalchemy.ext.declarative import declarative_base
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
