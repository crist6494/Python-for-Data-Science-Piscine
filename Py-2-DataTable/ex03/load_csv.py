import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Takes as parameter a path to a csv file
    prints its dimensions and returns the dataset
    """
    try:
        assert path.lower().endswith('.csv'), "The file must be a csv file"
        data_set = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data_set.shape}")
        return data_set
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return None
