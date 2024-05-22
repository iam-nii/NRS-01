from sqlalchemy import select, create_engine, Column, PrimaryKeyConstraint, String, Integer, CHAR, Float
from sqlalchemy.ext.declarative import declarative_base
from polosin.public.Encryption import EncDecPass

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String, unique=True)
    password = Column('password', String)
    material_id = Column('material_id',Integer)
    role = Column('role', String)

    def __init__(self, username, password, role):
        try:
            self.username = username
            self.password = EncDecPass().encrypt_password(password)
            self.role = role
        except Exception as e:
            print(e)

    def __repr__(self):
        return f"({self.id}) {self.username} {self.role}"


# class Chanel(Base):
#     __tablename__ = 'chanel'
#     id = Column('id', Integer, primary_key=True, autoincrement=True)
#     width = Column('width', Float)
#     depth = Column('depth', Float)
#     length = Column('length', Float)
#
#     def __init__(self, width, depth, length):
#         self.width = width
#         self.depth = depth
#         self.length = length
#
#     def __repr__(self):
#         return f"({self.width}) {self.depth} {self.length}"


class Material(Base):
    __tablename__ = 'material'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    material = Column('material',String)
    density = Column('density', Float)
    heat_capacity = Column('heat_capacity', Float)
    melting_temperature = Column('melting_temperature', Float)

    def __init__(self,material, density, heat_capacity, melting_temperature):
        self.material = material
        self.density = density
        self.heat_capacity = heat_capacity
        self.melting_temperature = melting_temperature

    def __repr__(self):
        return f"({self.material}) {self.density} {self.heat_capacity} {self.melting_temperature}"


# class ProcessParams(Base):
#     __tablename__ = 'process_params'
#
#     id = Column('id', Integer, primary_key=True, autoincrement=True)
#     cover_speed = Column('cover_speed', Float)
#     cover_temperature = Column('cover_temperature', Float)
#
#     def __init__(self, cover_speed, cover_temperature):
#         self.cover_speed = cover_speed
#         self.cover_temperature = cover_temperature
#
#     def __repr__(self):
#         return f"({self.cover_speed}) {self.cover_temperature}"


class MathModel(Base):
    __tablename__ = 'math_model'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    consistency_coefficient = Column('consistency_coefficient', Float)
    temp_viscosity_coefficient = Column('temp_viscosity_coefficient', Float)
    casting_temperature = Column('casting_temperature', Float)
    flow_index = Column('flow_index', Float)
    cover_heat_transfer_coefficient = Column('cover_heat_transfer_coefficient', Float)
    material_id = Column('material_id',Integer)

    def __init__(self, consistency_coefficient, temp_viscosity_coefficient, casting_temperature, flow_index,
                 cover_heat_transfer_coefficient,material_id):
        self.consistency_coefficient = consistency_coefficient
        self.temp_viscosity_coefficient = temp_viscosity_coefficient
        self.casting_temperature = casting_temperature
        self.flow_index = flow_index
        self.cover_heat_transfer_coefficient = cover_heat_transfer_coefficient
        self.material_id = material_id

    def __repr__(self):
        return (f"({self.consistency_coefficient}) {self.temp_viscosity_coefficient} {self.casting_temperature}"
                f"{self.flow_index} {self.cover_heat_transfer_coefficient} {self.material_id}")
