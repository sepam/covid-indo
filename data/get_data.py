""" Utility functions to capture data.

List of data sources by province:
https://docs.google.com/spreadsheets/d/1ma1T9hWbec1pXlwZ89WakRk-OfVUQZsOCFl4FwZxzVw/edit#gid=1814790353

"""
import pandas as pd


URL = 'https://tiny.cc/Datacovidjakarta'
SHEET = 'Data Indonesia dan Jakarta'


def fetch(url, sheet):
    """Fetches latest data sheet."""
    data_sheet = pd.read_excel(url, sheet_name=sheet)
    return data_sheet


if __name__ == '__main__':
    df = fetch(URL, SHEET)
