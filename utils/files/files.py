"""Utility functions for file handling."""

from pathlib import Path
from typing import List, Tuple

import pandas as pd
import openpyxl


def get_devices_details_path(file_name: str) -> Path:
    """
    Get the path to the devices details file.

    Args:
        file_name (str): The name of the file.
    Returns:
        Path: The path to the devices details file.
    """
    cwd = Path.cwd()
    return cwd / "resources" / "details" / file_name


def get_devices_xlsx_path(dir_name: str) -> Path:
    """
    Get the path to the devices XLSX file.

    Args:
        dir_name (str): The name of the directory.

    Returns:
        Path: The path to the devices XLSX file.
    """
    cwd = Path.cwd()
    return cwd / "resources" / dir_name


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


def create_excel_files_from_dataframes(
    dataframes: List[Tuple[str, pd.DataFrame]], file_path: Path
) -> None:
    """
    Create excel files from the given dataframes.

    Args:
        dataframes (List[Tuple[str, pd.DataFrame]]): List of tuples containing sheet names and dataframes
        file_path (Path): Path to save the excel file
    """

    if not file_path.exists():
        file_path.mkdir(parents=True, exist_ok=True)

    file_list = [file.name for file in file_path.glob("*.xlsx") if file.is_file()]

    new_file_list = []
    replaced_file_list = []
    missing_file_list = []

    for file_name, df in dataframes:
        if not df.empty:
            new_file_name = f"{file_name}_kodelabs_devices.xlsx"
            new_file_list.append(new_file_name)

            new_file_path = file_path / new_file_name

            if new_file_name in file_list:
                new_file_path.unlink()
                replaced_file_list.append(new_file_name)

            df.to_excel(new_file_path, index=False, engine="openpyxl")

            wb = openpyxl.load_workbook(new_file_path)
            ws = wb.active

            header_row = ws[1]

            for cell in header_row:
                cell.font = openpyxl.styles.Font(bold=False)
                cell.border = openpyxl.styles.Border()
                cell.alignment = openpyxl.styles.Alignment(
                    horizontal="left", vertical="center"
                )

            wb.save(new_file_path)

    for file in file_list:
        if file not in new_file_list:
            missing_file_list.append(file)

    print(f"New files created: {new_file_list}")
    print(f"Files replaced: {replaced_file_list}")
    print(f"Files missing: {missing_file_list}")
