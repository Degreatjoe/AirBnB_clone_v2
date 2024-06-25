#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', 
                             String(60), 
                             ForeignKey('places.id'), 
                             primary_key=True, nullable=False),
                      Column('amenity_id', 
                             String(60), 
                             ForeignKey('amenities.id'), 
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable= False)
    name = Column(String(128), nullable= False)
    description = Column(String(1024), nullable= False)
    number_rooms = Column(Integer, default= 0, nullable= False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []
    reviews = relationship('Review', backref='user', cascade='all, delete, delete-orphan')
    amenities = relationship('Amenity', secondary=place_amenity, back_populates='place_amenities', viewonly=False)

    @property
    def reviews(self):
        """Getter attribute for FileStorage relationship between Place and Review"""
        from models import storage
        from models.review import Review
        return [review for review in storage.all(Review).values() if review.place_id == self.id]
    
    @property
    def amenities(self):
        """Getter attribute for FileStorage relationship between Place and Amenity"""
        from models import storage
        from models.amenity import Amenity
        amenity_list = []
        for amenity in storage.all(Amenity).values():
            if amenity.id in self.amenity_ids:
                amenity_list.append(amenity)
        return amenity_list
    
    @amenities.setter
    def amenities(self, obj):
        """Setter attribute for FileStorage relationship between Place and Amenity"""
        if isinstance(obj, Amenity):
            self.amenity_ids.append(obj.id)
