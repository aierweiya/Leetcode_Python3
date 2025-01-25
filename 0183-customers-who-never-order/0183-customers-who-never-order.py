import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    new_table = customers.merge(orders, left_on='id', right_on='customerId', how='left')
    new_table = new_table[pd.isnull(new_table['customerId'])][['name']]
    new_table = new_table.rename(columns={'name' : 'Customers'})
    return new_table
    