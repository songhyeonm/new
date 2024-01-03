from sqlalchemy import Column, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

#Base를 상속받는 Post 클래스 정의
class Post(Base):
    __tablename__ = "post"

    post_id = Column(Integer, primary_key = True, autoincrement= True)
    title = Column(Text, nullable = False)
    contents = Column(Text, nullable = True)
    writer = Column(Text, nullable = False)

class Comment(Base):
    __tablename__ = "comment"

    comment_id = Column(Integer, primary_key= True, autoincrement= True)
    post_id = Column(Integer, ForeignKey("post.post_id"))
    post = relationship("Post", back_populates = "comment")
    writer = Column(Text, nullable= False)
    content = Column(Text, nullable = True)

    