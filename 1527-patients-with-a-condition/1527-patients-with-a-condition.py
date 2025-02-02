import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].str.match(r'^DIAB1.*|.* DIAB1.*')]