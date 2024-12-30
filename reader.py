import pandas as pd
import os

def read_dataset(file_path):
    """
    Reads a dataset from a given file path and returns a DataFrame.

    Parameters:
    file_path (str): Path to the dataset file.

    Returns:
    pd.DataFrame: DataFrame containing the dataset.

    Raises:
    ValueError: If the file type is unsupported.
    FileNotFoundError: If the file does not exist.
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Get the file extension
    file_extension = os.path.splitext(file_path)[1].lower()

    try:
        # Read dataset based on file extension
        if file_extension == '.csv':
            data = pd.read_csv(file_path)
        elif file_extension in ['.xls', '.xlsx']:  # Excel files
            data = pd.ExcelFile(file_path)
            if len(data.sheet_names) > 1:
                print(f"Multiple sheets found: {data.sheet_names}")
                sheet_name = input("Enter the sheet name to load: ")
                data = pd.read_excel(file_path, sheet_name=sheet_name)
            else:
                data = pd.read_excel(file_path)
        elif file_extension == '.json':
            data = pd.read_json(file_path)
        elif file_extension == '.parquet':
            data = pd.read_parquet(file_path)
        elif file_extension == '.txt':
            data = pd.read_csv(file_path, delimiter='\t')
        else:
            raise ValueError(f"Unsupported file type: {file_extension}")

        print("Dataset loaded successfully!")
        return data

    except Exception as e:
        raise ValueError(f"Error reading the file: {str(e)}")
