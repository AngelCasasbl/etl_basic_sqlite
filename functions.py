import pandas as pd

def glimpse(df: pd.DataFrame) -> pd.DataFrame:
    """
    Similar to R's glimpse()

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
    """
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    sample_size = min(df.shape[0], 5)

    return (
        df.sample(sample_size)
        .T.assign(dtypes=df.dtypes)
        .loc[
            :, lambda x: sorted(x.columns, key=lambda col: 0 if col == "dtypes" else 1)
        ]
    )