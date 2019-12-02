from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_declarative import Address, Base, Person

engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


c1 = Customer(first_name = 'Toby',
              last_name = 'Miller',
              username = 'tmiller',
              email = 'tmiller@example.com',
              address = '1662 Kinney Street',
              town = 'Wolfden'
             )

c2 = Customer(first_name = 'Scott',
              last_name = 'Harvey',
              username = 'scottharvey',
              email = 'scottharvey@example.com',
              address = '424 Patterson Street',
              town = 'Beckinsdale'
             )
c3 = Customer(
    first_name="John",
    last_name="Lara",
    username="johnlara",
    email="johnlara@mail.com",
    address="3073 Derek Drive",
    town="Norfolk"
)

c4 = Customer(
    first_name="Sarah",
    last_name="Tomlin",
    username="sarahtomlin",
    email="sarahtomlin@mail.com",
    address="3572 Poplar Avenue",
    town="Norfolk"
)

c5 = Customer(first_name='Toby',
              last_name='Miller',
              username='tmiller',
              email='tmiller@example.com',
              address='1662 Kinney Street',
              town='Wolfden'
              )

c6 = Customer(first_name='Scott',
              last_name='Harvey',
              username='scottharvey',
              email='scottharvey@example.com',
              address='424 Patterson Street',
              town='Beckinsdale'
              )
session.add_all([c1, c2, c3, c4, c5, c6])
session.commit()



