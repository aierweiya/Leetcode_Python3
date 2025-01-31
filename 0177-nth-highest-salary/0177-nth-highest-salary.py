import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # 計算薪水的排名，使用 dense 排名方法，確保排名無間隙
    employee['rank'] = employee['salary'].rank(method='dense', ascending=False)

    # 篩選出 rank 等於 N 的薪水
    nth_highest_salary = employee.loc[employee['rank'] == N, 'salary'].drop_duplicates()

    # 如果找到對應的 N 高薪水，返回結果，否則返回 null
    if not nth_highest_salary.empty:
        return pd.DataFrame({'getNthHighestSalary(%d)' % N: nth_highest_salary})
    else:
        return pd.DataFrame({'getNthHighestSalary(%d)' % N: [None]})