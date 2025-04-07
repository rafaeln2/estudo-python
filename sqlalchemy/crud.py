from sqlalchemy.orm import Session

from models import User , engine

Session = sessionmaker(bind=engine)
session = Session()

user = User(name="rafael", age=30)
session.add(user)
session.commit()