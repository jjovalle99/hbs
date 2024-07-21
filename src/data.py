from pathlib import Path

import pandas as pd


def load_data(datapath: Path) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Loads Wayfair ANnotation Dataset

    Args:
        datapath (Path): Folder where .csv files are located.

    Returns:
        tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]: .csv files loaded as pandas dataframes.
    """
    query_df = pd.read_csv(datapath / "query.csv", sep="\t", encoding="utf-8")
    product_df = pd.read_csv(datapath / "product.csv", sep="\t", encoding="utf-8")
    label_df = pd.read_csv(datapath / "label.csv", sep="\t", encoding="utf-8")

    print(f"QueryDF: Rows [{query_df.shape[0]:,}], Columns: [{query_df.shape[1]}]")
    print(f"ProductDF: Rows [{product_df.shape[0]:,}], Columns: [{product_df.shape[1]}]")
    print(f"LabelDF: Rows [{label_df.shape[0]:,}], Columns: [{label_df.shape[1]}]")

    return query_df, product_df, label_df
