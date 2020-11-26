from heqtor.core import Session
from heqtor.models import User, Company


def create_company(name: str, siren: str, email: str, phone: str, made_by_id: int):
    session = Session()
    try:
        creator = session.query(User).get(made_by_id)
        if creator is None:
            raise Exception("Company creator not found")
        company = Company(name=name, siren=siren, email=email, phone=phone)
        session.add(company)
        session.query(Company).filter(
            CompanyRestaurateur.siren == siren,
        ).one()  # update company instance with id from database
        creator.company_id = company.id
        session.commit()
        return company.get_small_data()
    except:
        session.rollback()
        return False
    finally:
        session.close()


# TODO
# get company by id, delete company

def get_company_byId(company_id: int):
    session = Session()
    company = session.query(Company).get(company_id)
    if company is not None:
        company = company.get_small_data()
    session.close()
    return company

def update_company_data(company_id: int, phone: str = None):
    session = Session()
    try:
        company = session.query(Company).get(company_id)
        if phone is not None:
            company.phone = phone
        session.commit()
        return company.get_small_data()
    except:
        session.rollback()
        return False
    finally:
        session.close()

def delete_company(company_id: int):
    session = Session()
    try:
        company = session.query(Company).get(company_id)
        session.delete(company)
        session.commit()
        return True
    except:
        session.rollback()
        return False
    finally:
        session.close()