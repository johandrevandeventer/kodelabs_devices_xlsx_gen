"""Module for handling data operations related to devices"""

from typing import List, Tuple

import pandas as pd

from config import device_settings


def fix_building_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fix the building names in the dataframe

    Args:
        df (pd.DataFrame): Dataframe with building names

    Returns:
        pd.DataFrame: Dataframe with fixed building names
    """

    df["building_name"] = df["building_name"].str.lower()
    df["building_name"] = df["building_name"].str.replace(" | ", "_")
    df["building_name"] = df["building_name"].str.replace(" ", "_")
    return df


def build_dataframes(df: pd.DataFrame) -> List[Tuple[str, pd.DataFrame]]:
    """
    Build the dataframes for the devices

    Args:
        df (pd.DataFrame): Dataframe with device details

    Returns:
        Tuple[str, pd.DataFrame]: Tuple with the sheet name and the dataframe
    """

    dataframes = []

    for _, row in df.iterrows():
        building_name = row["building_name"]
        device_name = row["device_name"]
        modem_serial = row["modem_serial"]

        if device_name == "Unnamed Brand":
            device_name = "Generator"

        if pd.notna(modem_serial):
            building_meter_id_list = []
            building_meter_name_list = []
            building_data_point_list = []
            building_point_name_list = []
            building_units_list = []
            building_kind_list = []
            building_gain_list = []

            for _ in range(len(device_settings.DATA_POINTS)):
                building_meter_id_list.append(modem_serial)
                building_meter_name_list.append(device_name)

            building_data_point_list.extend(device_settings.DATA_POINTS)
            building_point_name_list.extend(device_settings.POINT_NAMES)
            building_units_list.extend(device_settings.UNITS)
            building_kind_list.extend(device_settings.KINDS)
            building_gain_list.extend(device_settings.GAINS)

            building_data = {
                "MeterId": building_meter_id_list,
                "MeterName": building_meter_name_list,
                "DataPoint": building_data_point_list,
                "PointName": building_point_name_list,
                "Units": building_units_list,
                "Kind": building_kind_list,
                "Gain": building_gain_list,
            }

            building_df = pd.DataFrame(building_data)

            dataframes.append((building_name, building_df))

    return dataframes
