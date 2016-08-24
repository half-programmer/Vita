<<<<<<< HEAD
# -*- coding: utf-8 -*-

from Database.models import Base
=======

from models import Base

import tables
>>>>>>> 7d6d33e5b640c3be8399381c6f8522dea0489958
from models import engine
import Database.tables

Base.metadata.create_all(engine)
print "创建表"