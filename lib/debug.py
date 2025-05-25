#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Test a Freebie and its relationships
    freebie = session.query(Freebie).first()
    print(f"Freebie: {freebie}")
    print(f"Belongs to Dev: {freebie.dev}")
    print(f"Belongs to Company: {freebie.company}")

    # Test Company relationships
    company = session.query(Company).first()
    print(f"\nCompany: {company}")
    print("Company freebies:")
    for f in company.freebies:
        print(f" - {f}")
    print("Company devs:")
    for d in company.devs:
        print(f" - {d}")

    # Test Dev relationships
    dev = session.query(Dev).first()
    print(f"\nDev: {dev}")
    print("Dev freebies:")
    for f in dev.freebies:
        print(f" - {f}")
    print("Dev companies:")
    for c in dev.companies:
        print(f" - {c}")

    session.close()