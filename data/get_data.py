import pandas as pd

"""
List of data sources by province: https://docs.google.com/spreadsheets/d/1ma1T9hWbec1pXlwZ89WakRk-OfVUQZsOCFl4FwZxzVw/edit#gid=1814790353

"""



URL = 'https://tiny.cc/Datacovidjakarta'
SHEET = 'Data Indonesia dan Jakarta'


def fetch(url, sheet):
    df = pd.read_excel(url, sheet_name=sheet)
    return df


if __name__ == '__main__':
    df = fetch(URL, SHEET)
