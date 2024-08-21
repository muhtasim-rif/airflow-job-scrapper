from scripts.db_manager import Base, get_session

def initialize_database():
    session = get_session()
    Base.metadata.create_all(session.bind)
    print("Database Initiated")

if __name__ == "__main__":
    initialize_database()