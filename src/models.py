import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)

    favoritos = relationship("Favorito", back_populates="usuario")

class Planeta(Base):
    __tablename__ = 'planeta'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    clima = Column(String)
    terreno = Column(String)
    
    favoritos = relationship("Favorito", back_populates="planeta")

class Personaje(Base):
    __tablename__ = 'personaje'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    especie = Column(String)
    genero = Column(String)
    
    favoritos = relationship("Favorito", back_populates="personaje")

class Vehiculo(Base):
    __tablename__ = 'vehiculo'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    modelo = Column(String)
    longitud = Column(String)
    velocidad_maxima = Column(String)
    capacidad_carga = Column(String)
    
    favoritos = relationship("Favorito", back_populates="vehiculo")

class Favorito(Base):
    __tablename__ = 'favorito'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable=True)
    personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=True)
    vehiculo_id = Column(Integer, ForeignKey('vehiculo.id'), nullable=True)
    
    usuario = relationship("Usuario", back_populates="favoritos")
    planeta = relationship("Planeta", back_populates="favoritos")
    personaje = relationship("Personaje", back_populates="favoritos")
    vehiculo = relationship("Vehiculo", back_populates="favoritos")


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
