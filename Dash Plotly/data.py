import pandas as pd
from sqlalchemy import create_engine


engine = create_engine(
"mysql+mysqlconnector://root:iamgroot@localhost/ujiantitanic?host=localhost?port=3306"
)


q1 = "select * from Titanic"
q2 = "select * from titanicoutcalc"
dfTitanic= pd.read_sql(q1,engine)
dfTitanicOutlier = pd.read_sql(q2, engine)