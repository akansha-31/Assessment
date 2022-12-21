import pandas as pd


def get_top_contributors(request):
    df = pd.read_csv('all_commits.csv')
    top_contributors = df['committer'].value_counts().nlargest(10).reset_index()
    top_contributors.columns = ['author', 'commit_count']
    top_contributors.to_csv('contributors.csv', index=False)