from werkzeug.security import generate_password_hash
from datetime import date, datetime, timedelta
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
from Models import *
import os

load_dotenv()
DB_URL = "mysql+pymysql://{}:{}@localhost/{}".format(os.getenv("DB_USERNAME"),os.getenv("DB_PASSWORD"),os.getenv("DB_DATABASE"))
engine = create_engine(DB_URL)
local_session = sessionmaker(autoflush=False, autocommit=False, bind=engine)
db = local_session()
nows = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
wala = None



seeds =[

    ##Users
    Admin(email='zhie@caz.com', username='admin', password=generate_password_hash('password', method='md5'), access='developer', active=1),
    Admin(email='jigem18@gmail.com', username='jigem', password=generate_password_hash('Apple1243', method='md5'), access='developer', active=1),
    Admin(email='agunodkrista@gmail.com', username='rissi', password=generate_password_hash('mizkahayah', method='md5'), access='developer', active=1),
    Admin(email='joy@gmail.com', username='joy', password=generate_password_hash('joy', method='md5'), access='developer', active=1),

   
]
  
db.bulk_save_objects(seeds)

db.commit()
db.close()
print("Successfully added a new post")