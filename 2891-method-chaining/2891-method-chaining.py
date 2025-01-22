import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals['weight'] > 100].sort_values(by='weight', ascending=False)[['name']]

#[['name']] 与 ['name'] 的区别：
#['name'] 返回的是一个 Series。
#[['name']] 返回的是一个包含 name 列的 DataFrame。