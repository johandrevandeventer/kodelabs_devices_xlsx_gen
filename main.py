"""Main script"""

from utils.files import files
from config import config


def main():
    devices_details_path = files.get_devices_details_path(
        config.DEVICES_DETAILS_FILE_NAME
    )

    df = files.read_excel_file(devices_details_path, "Details")

    print(df.head())


if __name__ == "__main__":
    main()
