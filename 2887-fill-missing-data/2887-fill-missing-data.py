import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products = products.fillna(0)
    return products