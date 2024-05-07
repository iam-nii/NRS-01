from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import reflection
from customtkinter import CTkLabel
from polosin.public.databases import User,Chanel,Material,MathModel,ProcessParams,Base


class Database:
    def __init__(self,window='main'):
        # Creating the database file
        self.engine = create_engine("sqlite:///chemresearch.db", echo=True)


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

    def get_chanel_params(self,id=None):
        if id is not None:
            chanels = self.session.query(Chanel).filter(Chanel.id == id).first()

        else:
            chanels = self.session.query(Chanel).all()
        return [chanels,3]

    def get_materials(self):
        materials = self.session.query(Material).all()
        return [materials,4]

    def get_math_module(self,id=None):
        if id is not None:
            math_modules = self.session.query(MathModel).filter(MathModel.id == id).first()
        else:
            math_modules = self.session.query(MathModel).all()
        return [math_modules,5]

    def get_process_params(self,id=None):
        if id is not None:
            process_params = self.session.query(ProcessParams).filter(ProcessParams.id == id).first()
        else:
                process_params = self.session.query(ProcessParams).all()
        return [process_params,2]

    def get_tables(self):
        insp = reflection.Inspector.from_engine(self.engine)
        # Return the table names
        return insp.get_table_names()
