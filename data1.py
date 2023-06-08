import pandas as pd 
from pandas_profiling import ProfileReport  
df = pd.read_csv('Target_Table_Snapshot.csv')
profile = ProfileReport(df, title="Pandas Profiling Report")
profile.to_file('EDA_snapshot_Analysis.html')