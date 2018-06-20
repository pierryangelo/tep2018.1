import json
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Text

profile = 'pierry'
passwd = ''

engine = create_engine(f'postgresql://{profile}:{passwd}@localhost/blog')

Base = declarative_base()

class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    name = Column(String)
    email = Column(String)


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    profile_id = Column(Integer, ForeignKey('profiles.id'))
    street = Column(String)
    suite = Column(String)
    city = Column(String)
    zipcode = Column(String)

    #profile = relationship('Profile', back_ref="addresses")

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    profile_id = Column(Integer, ForeignKey('profiles.id'))
    title = Column(String)
    body = Column(Text)

    #profile = relationship('Profile', back_populates="posts")

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
profiles = data['profiles']

for profile in profiles:
    u = Profile(id=profile['id'], user_id=profile['id'], name=profile['name'], email=profile['email'])
    session.add(u)
    session.commit()


# POPULATING ADDRESSES TABLE
profiles = data['profiles']

for profile in profiles:
    u_adress = profile['address']
    a = Address(id=profile['id'], profile_id=profile['id'], street=u_adress['street'],
                suite=u_adress['suite'], city=u_adress['city'],
                zipcode=u_adress['zipcode'])
    session.add(a)
    session.commit()


# POPULATING POSTS TABLE
posts = data['posts']

for post in posts:
    p = Post(id=post['id'], profile_id=post['profileId'],
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