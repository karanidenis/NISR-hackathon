import pandas as pd


file_path = './data/labour_force_data.xlsx'  # read excel file

# list of sheets used in the excel file
TABLE_B1 = 'Table B.1'
TABLE_B2 = 'Table B.2'


def read_table(file_path, sheet_name, table_start_col, table_end_col,
               table_start_row, table_end_row):
    """Reads a table from an Excel file and returns it as a DataFrame.

    Args:
        file_path (str): file path to the Excel file
        sheet_name (str): name of the sheet to read from
        table_start_col (str): starting column of the table
        table_end_col (str): ending column of the table
        table_start_row (int): starting row of the table
        table_end_row (int): ending row of the table

    Returns:
        DataFrame: the table as a DataFrame
    """

    df = pd.read_excel(
        file_path,
        sheet_name=sheet_name,
        usecols=f"{table_start_col}:{table_end_col}",
        skiprows=range(table_start_row - 1),  # skiprows expects 0-indexed
        nrows=table_end_row - table_start_row + 1
    )
    return df


# general_employement_df = read_table(file_path, TABLE_B1, 'A', 'D', 3, 7)

# Display the DataFrame to see if it has been loaded correctly
# print(general_employement_df)

if __name__ == "__main__":
    print(general_employement_df)
