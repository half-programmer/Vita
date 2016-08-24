<<<<<<< HEAD
# -*- coding: utf-8 -*-

from Database.models import Base
=======

from models import Base

import tables
>>>>>>> 64b56da94f548ac82f63674689dccc7f2df5d0af
from models import engine
import Database.tables

Base.metadata.create_all(engine)
print "创建表"