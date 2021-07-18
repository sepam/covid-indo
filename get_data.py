import pandas as pd


URL = 'https://tiny.cc/Datacovidjakarta'
SHEET = 'Data Indonesia dan Jakarta'


def get_data(url, sheet):
    df = pd.read_excel(url, sheet_name=sheet)
    return df


if __name__ == '__main__':
    df = get_data(URL, SHEET)
