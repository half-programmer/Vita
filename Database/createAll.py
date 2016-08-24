
from models import Base

import tables
from models import engine
import Database.tables

Base.metadata.create_all(engine)
print "创建表"