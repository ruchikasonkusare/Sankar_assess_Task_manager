from app import create_app, db, socketIO

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    socketIO.run(app, debug=True)