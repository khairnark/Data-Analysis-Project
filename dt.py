import pandas as pd
from pandas_profiling import ProfileReport



df=pd.read_csv(r'C:\Users\kkhairnar\data_analysis\Target_Table_Snapshot.csv')
profile = ProfileReport(df, title="Document Report")



profile.to_file("your_report.html")