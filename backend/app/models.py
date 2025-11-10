from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

mood_recipe_association = Table(
    'mood_recipe', Base.metadata,
    Column('mood_id', Integer, ForeignKey('moods.id')),
    Column('recipe_id', Integer, ForeignKey('recipes.id'))
)

class Mood(Base):
    __tablename__ = 'moods'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    recipes = relationship('Recipe', secondary=mood_recipe_association, back_populates='moods')

class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    ingredients = Column(String, nullable=False)  # Could be JSON encoded string
    instructions = Column(String, nullable=False)
    moods = relationship('Mood', secondary=mood_recipe_association, back_populates='recipes')
