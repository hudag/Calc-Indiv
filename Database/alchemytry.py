from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pprint import pprint


engine = create_engine('sqlite:////web/Sqlite-Data/example.db')
session = sessionmaker(bind=engine)

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250))
    last_name = Column(String(250))
    username = Column(String(250))
    email = Column(String(250))
    address = Column(String(250))
    town = Column(String(250))

class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(Integer)
    cost_price = Column(Float)
    selling_price = Column(Float)
    quantity = Column(Float)


Base.metadata.create_all(engine)

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

#PART 1------------------------------------------------------------
c1 = Customer(first_name='Toby',
              last_name='Miller',
              username='tmiller',
              email='tmiller@example.com',
              address='1662 Kinney Street',
              town='Wolfden'
              )

c2 = Customer(first_name='Scott',
              last_name='Harvey',
              username='scottharvey',
              email='scottharvey@example.com',
              address='424 Patterson Street',
              town='Beckinsdale'
              )


session.add(c1)
session.add(c2)

session.commit()

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

session.add_all([c3, c4, c5, c6])
session.commit()

i1 = Item(name='Chair', cost_price=9.21, selling_price=10.81, quantity=5)
i2 = Item(name='Pen', cost_price=3.45, selling_price=4.51, quantity=3)
i3 = Item(name='Headphone', cost_price=15.52, selling_price=16.81, quantity=50)
i4 = Item(name='Travel Bag', cost_price=20.1, selling_price=24.21, quantity=50)
i5 = Item(name='Keyboard', cost_price=20.1, selling_price=22.11, quantity=50)
i6 = Item(name='Monitor', cost_price=200.14, selling_price=212.89, quantity=50)
i7 = Item(name='Watch', cost_price=100.58, selling_price=104.41, quantity=50)
i8 = Item(name='Water Bottle', cost_price=20.89, selling_price=25, quantity=50)

session.add_all([i1, i2, i3, i4, i5, i6, i7, i8])
session.commit()

o1 = Order(customer=c1)
o2 = Order(customer=c1)

line_item1 = OrderLine(order=o1, item=i1, quantity=3)
line_item2 = OrderLine(order=o1, item=i2, quantity=2)
line_item3 = OrderLine(order=o2, item=i1, quantity=1)
line_item3 = OrderLine(order=o2, item=i2, quantity=4)

session.add_all([o1, o2])

session.new
session.commit()

o3 = Order(customer=c1)
orderline1 = OrderLine(item=i1, quantity=5)
orderline2 = OrderLine(item=i2, quantity=10)

o3.order_lines.append(orderline1)
o3.order_lines.append(orderline2)

session.add_all([o3])

session.commit()

conn = sqlite3.connect('example.db')

c = conn.cursor()

session.query(Customer).all()
print(session.query(Customer))

q = session.query(Customer)

for c in q:
    print(c.id, c.first_name)

session.query(Customer.id, Customer.first_name).all()

session.query(Customer).count()
session.query(Item).count()
session.query(Order).count()

session.query(Customer).first()
session.query(Item).first()
session.query(Order).first()

session.query(Customer).get(1)
session.query(Item).get(1)
session.query(Order).get(100)

print(session.query(Customer).filter(Customer.first_name == 'John'))

session.query(Customer).filter(Customer.id <= 5, Customer.town == "Norfolk").all()

# find all customers who either live in Peterbrugh or Norfolk

session.query(Customer).filter(or_(
    Customer.town == 'Peterbrugh',
    Customer.town == 'Norfolk'
)).all()

# find all customers whose first name is John and live in Norfolk

session.query(Customer).filter(and_(
    Customer.first_name == 'John',
    Customer.town == 'Norfolk'
)).all()

# find all johns who don't live in Peterbrugh

session.query(Customer).filter(and_(
    Customer.first_name == 'John',
    not_(
        Customer.town == 'Peterbrugh',
    )
)).all()

session.query(func.count(Customer.id)).join(Order).filter(
    Customer.first_name == 'John',
    Customer.last_name == 'Green',
).group_by(Customer.id).scalar()

session.query(
    func.count("*").label('town_count'),
    Customer.town
).group_by(Customer.town).having(func.count("*") > 2).all()

session.query(
    cast(func.pi(), Integer),
    cast(func.pi(), Numeric(10,2)),
    cast("2010-12-01", DateTime),
    cast("2010-12-01", Date),
).all()

s1 = session.query(Item.id, Item.name).filter(Item.name.like("Wa%"))
s2 = session.query(Item.id, Item.name).filter(Item.name.like("%e%"))
s1.union(s2).all()
s1.union_all(s2).all()

c.execute('SELECT * FROM person')
print
c.fetchall()
c.execute('SELECT * FROM address')
print
c.fetchall()
conn.close()

all_customer = session.query(Customer).all()
for customer in all_customer:
    pprint(customer.__dict__)

all_item = session.query(Item).all()
for item in all_item:
    pprint(item.__dict__)

print("\nPrint Count of both tables")
all_customers = session.query(Customer).count()
pprint(all_customers)
all_items = session.query(Item).count()
pprint(all_items)

print("\nPrint first rows")
all_customer = session.query(Customer).first()
all_items = session.query(Item).first()
pprint(all_customer.__dict__)
pprint(all_items.__dict__)

print("\nPrint using sql and or not in notin between like limit offset orderby")
all_customer = session.query(Customer).filter(or_(
    Customer.town == 'Peterbrugh',
    Customer.town == 'Norfolk'
)).all()
for customer in all_customer:
    pprint(customer.__dict__)

all_customer = session.query(Customer).filter(and_(
    Customer.first_name == 'John',
    Customer.town == 'Norfolk'
)).all()
for customer in all_customer:
    pprint(customer.__dict__)

all_customer = session.query(Customer).filter(and_(
    Customer.first_name == 'John',
    not_(
        Customer.town == 'Peterbrugh',
    )
)).all()
for customer in all_customer:
    pprint(customer.__dict__)

all_customer = session.query(Customer).filter(Customer.first_name.in_(['Toby', 'Sarah'])).all()
for customer in all_customer:
    pprint(customer.__dict__)

all_customer = session.query(Customer).filter(Customer.first_name.notin_(['Toby', 'Sarah'])).all()
for customer in all_customer:
    pprint(customer.__dict__)

all_item = session.query(Item).filter(Item.cost_price.between(10, 50)).all()
for item in all_item:
    pprint(item.__dict__)

all_item = session.query(Item).filter(Item.name.like("%r")).all()
for item in all_item:
    pprint(item.__dict__)

all_customer = session.query(Customer).limit(2).all()
for customer in all_customer:
    pprint(customer.__dict__)

all_customer = session.query(Customer).limit(2).offset(2).all()
for customer in all_customer:
    pprint(customer.__dict__)

all_item = session.query(Item).filter(Item.name.ilike("wa%")).order_by(desc(Item.cost_price)).all()
for item in all_item:
    pprint(item.__dict__)

all_customer = session.query(
    func.count("*").label('town_count'),
    Customer.town
).group_by(Customer.town).having(func.count("*") > 2).all()
for customer in all_customer:
    pprint(customer)

all_customer = session.query(Customer.town).filter(Customer.id  < 10).distinct().all()
for customer in all_customer:
    pprint(customer)
all_customer = session.query(
    func.count(distinct(Customer.town)),
    func.count(Customer.town)
).all()
for customer in all_customer:
    pprint(customer)

all_customer = session.query(
    cast(math.pi, Integer),
    cast(math.pi, Numeric(10,2)),
).all()
for customer in all_customer:
    pprint(customer)