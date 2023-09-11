from app import app, db

if __name__ == "__main__":
    with app.app_context():
        import ipdb

        from models import Bakery, BakedGood

        ipdb.set_trace()