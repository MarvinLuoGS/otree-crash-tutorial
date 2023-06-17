import pandas as pd

data = pd.read_csv('all_apps_wide_2023-03-28.csv', sep=',')

def rename(st, app):
    return st.replace(app + '.', '').replace('subsession.', '').replace('group.', '').replace('player.', '')

app_name = ['trustgame','questionnaire']
for app in app_name:
    condition = [app in st for st in data.columns.values]
    df = data.loc[:, condition]
    df = df.rename(columns={st: rename(st, app) for st in df.columns.values})
    df.columns = pd.MultiIndex.from_tuples(
        [tuple(st.split('.', 1)) for st in df.columns], names=['round', 'varname'])
    df = df.stack('round').reset_index(1)
    df.to_csv('{}.csv'.format(app))
