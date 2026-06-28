from __future__ import annotations

from datetime import UTC, datetime #* improting date,time and utc time zone

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class User(Base): #* class to create table for user data
    __tablename__ = "users" #* table name

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True) #* creating column of table
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    image_file: Mapped[str | None] = mapped_column( #* either str or null
        String(200),
        nullable=True,
        default=None,
    )

    posts: Mapped[list[Post]] = relationship(back_populates="author")#* list of all post created by user
                  #*     ^-- this post here is a referenace to the class created below. this type of referencing is called forword referencing.
    @property
    def image_path(self) -> str:
        if self.image_file: #* if user have a uploaded image
            return f"/media/profile_pics/{self.image_file}"
        return "/static/profile_pics/default.jpg"#* if user dont have a uploaded image


class Post(Base): #* class to create table for user data
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[User] = relationship(back_populates="posts") #* mapping relationship with user
                            #* ^--many to one type thing

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),# it link post to userid
        nullable=False,
        index=True,#it is similar to index in book,primary kkey get indexes autometically but forignkey dont.
    )
    date_posted: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )
        
#* model act as a template/ i define our data