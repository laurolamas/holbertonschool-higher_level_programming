#!/usr/bin/python3
""" Task 7 """


if __name__ == "__main__":

    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    import sys

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2],
                sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State)

    found = False

    for state in states:
        if sys.argv[4] == state.name:
            print(state.id)
            found = True
    if not found:
        print("Not Found")
        print("[Anything]", file=sys.stderr)
