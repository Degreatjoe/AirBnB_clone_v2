#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete, delete-orphan')

    @property
    def cities(self):
        from models import storage_type, storage
        from models.city import City
        """Getter for cities when using FileStorage"""
        if storage_type == 'db':
            return self.cities
        else:
            return [city for city in storage.all(City).values() if city.state_id == self.id]
