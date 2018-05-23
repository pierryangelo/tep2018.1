import json
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Text

user = 'pierry'
passwd = 'wd45$sds'

engine = create_engine(f'postgresql://{user}:{passwd}@localhost/blog')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    street = Column(String)
    suite = Column(String)
    city = Column(String)
    zipcode = Column(String)

    #user = relationship('User', back_ref="addresses")

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String)
    body = Column(Text)

    #user = relationship('User', back_populates="posts")

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    name = Column(String)
    email = Column(String)
    body = Column(Text)

    #post = relationship('Post', back_populates='comments')

# creates the schema for all entities
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# loads json data
f = open('data.json')
data = json.load(f)

# POPULATING USERS TABLE
users = data['users']

for user in users:
    u = User(id=user['id'], name=user['name'], email=user['email'])
    session.add(u)
    session.commit()


# POPULATING ADDRESSES TABLE
users = data['users']

for user in users:
    u_adress = user['address']
    a = Address(id=user['id'], user_id=user['id'], street=u_adress['street'],
                suite=u_adress['suite'], city=u_adress['city'],
                zipcode=u_adress['zipcode'])
    session.add(a)
    session.commit()


# POPULATING POSTS TABLE
posts = data['posts']

for post in posts:
    p = Post(id=post['id'], user_id=post['userId'],
             title=post['title'], body=post['body'])

    session.add(p)
    session.commit()

# POPULATING COMMENTS TABLE
comments = data['comments']

for comment in comments:
    c = Comment(id=comment['id'], post_id=comment['postId'],
                name=comment['name'], email=comment['email'],
                body=comment['body'])

    session.add(c)
    session.commit()