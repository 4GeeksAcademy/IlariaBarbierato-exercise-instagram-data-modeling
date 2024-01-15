import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key = True)
    username = Column(String(250), nullable = False, unique = True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(150), unique = True)

class Follower(Base):
    __tablename__ = "follower"
    id = Column(Integer, primary_key = True)
    user_from_id = Column(Integer, ForeignKey("user.id"))
    user_from_id_relationship = relationship(User)
    user_to_id = Column(Integer, ForeignKey("user.id"))
    user_to_id_relationship = relationship(User)

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user_id_relationship = relationship(User)

class MediaPost(Base):
    __tablename__ = "media_post"
    id = Column(Integer, primary_key = True)
    url = Column(String(250))
    post_id  = Column(Integer, ForeignKey("post.id"))
    post_id_relationship = relationship(Post)

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key = True)
    comment = Column(String(500))
    author_id = Column(Integer, ForeignKey("user.id"))
    author_id_relationship = relationship(User)
    post_id  = Column(Integer, ForeignKey("post.id"))
    post_id_relationship = relationship(Post)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
