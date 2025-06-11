"""Utility functions for file handling."""

from pathlib import Path

import pandas as pd


def get_devices_details_path(file_name: str) -> Path:
    """
    Get the path to the devices details file.

    Args:
        file_name (str): The name of the file.
    Returns:
        Path: The path to the devices details file.
    """
    cwd = Path.cwd()
    return cwd / "details" / file_name


def get_devices_xlsx_path(dir_name: str) -> Path:
    """
    Get the path to the devices XLSX file.

    Args:
        dir_name (str): The name of the directory.

    Returns:
        Path: The path to the devices XLSX file.
    """
    cwd = Path.cwd()
    return cwd / dir_name


def read_excel_file(file_path: Path, sheet_name: str) -> pd.DataFrame:
    """
    Read an excel file and return a pandas dataframe

    Args:
        file_path (Path): Path to the excel file
        sheet_name (str): Name of the sheet to read from

    Returns:
        pd.DataFrame: Dataframe of the excel sheet
    """

    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df
