import pandas as pd


URL = 'https://tiny.cc/Datacovidjakarta'
SHEET = 'Data Indonesia dan Jakarta'


def fetch(url, sheet):
    df = pd.read_excel(url, sheet_name=sheet)
    return df


if __name__ == '__main__':
    df = fetch(URL, SHEET)
