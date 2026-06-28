from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"#*tell where to connect,if blog.db didnt exist then it will be autometicaly created
                                               #*when we change to postgress this url is  the only thing we need to change

engine = create_engine(#*engine connects codebase with database
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},#* fast api can handle many thread request at same time and sql lite go one by one. so doingg it false solve this problem
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#* sessionmaker create a session with dadabase. each request has its own session.auto commitis false because we want to control when to update our db

class Base(DeclarativeBase):#*help in type checking
    pass


def get_db():
    with SessionLocal() as db:#* work as acontext manager(like opening a file), so this ensure clean up even when error occur
        yield db