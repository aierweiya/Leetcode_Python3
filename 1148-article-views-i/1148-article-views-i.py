import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views = views[views['author_id'] == views['viewer_id']]
    views = views[['author_id']].rename(columns={'author_id': 'id'}).drop_duplicates().sort_values(by='id')
    return views