#!/usr/bin/env python3

# Script goes here!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

# Connect to your SQLite DB
engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create all tables (if not created)
Base.metadata.create_all(engine)

# Create sample companies
company1 = Company(name="Tech Corp", founding_year=2000)
company2 = Company(name="Code LLC", founding_year=2010)

# Create sample devs
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")

# Create freebies
freebie1 = Freebie(item_name="T-shirt", value=20, dev=dev1, company=company1)
freebie2 = Freebie(item_name="Mug", value=10, dev=dev1, company=company2)
freebie3 = Freebie(item_name="Sticker", value=5, dev=dev2, company=company1)

# Add all to session
session.add_all([company1, company2, dev1, dev2, freebie1, freebie2, freebie3])

# Commit to DB
session.commit()
print("Seed data added successfully!")

session.close()
