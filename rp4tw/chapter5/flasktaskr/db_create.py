from app import db
from app.models import FTasks
from datetime import date

# Create the database and the db table
db.create_all()

# Insert data
db.session.add(FTasks("Finish this tutorial", date(2013, 3, 14), 10,
                      date(2013, 3, 13), 1, 1))
db.session.add(FTasks("Finish my book", date(2013, 3, 13), 10,
                      date(2013, 3, 13), 1, 1))

# Commit changes
db.session.commit()
