from collections import defaultdict
from typing import Dict, List, Tuple

import pandas as pd


def create_query_dict(query_df: pd.DataFrame) -> Dict[str, str]:
    return dict(zip(query_df["query_id"], query_df["query"]))


def create_product_dict(product_df: pd.DataFrame) -> Dict[str, str]:
    return dict(zip(product_df["product_id"], product_df["product_name"]))


def create_relevance_dict(label_df: pd.DataFrame) -> Dict[str, List[str]]:
    relevance_dict = defaultdict(list)
    for _, row in label_df[label_df["label"].isin(["Exact"])].iterrows():
        relevance_dict[row["query_id"]].append(row["product_id"])
    return dict(relevance_dict)


def prepare_data(
    query_df: pd.DataFrame, product_df: pd.DataFrame, label_df: pd.DataFrame
) -> Tuple[Dict[str, str], Dict[str, str], Dict[str, List[str]]]:
    queries = create_query_dict(query_df)
    corpus = create_product_dict(product_df)
    relevant_docs = create_relevance_dict(label_df)

    return queries, corpus, relevant_docs
