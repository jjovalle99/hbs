from typing import List

import pandas as pd


def naive_map_at_k(true_ids: List[str], predicted_ids: List[str], k: int = 10) -> float:
    """
    Calculate the Mean Average Precision at K (MAP@K) for exact matches.

    Args:
        true_ids: List of relevant product IDs.
        predicted_ids: List of predicted product IDs.
        k: Number of top elements to consider.

    Returns:
        MAP@K score.
    """
    if not len(true_ids) or not len(predicted_ids):
        return 0.0

    score = 0.0
    num_hits = 0.0

    for i, p_id in enumerate(predicted_ids[:k]):
        if p_id in true_ids and p_id not in predicted_ids[:i]:
            num_hits += 1.0
            score += num_hits / (i + 1.0)

    return score / min(len(true_ids), k)


def weighted_map_at_k(
    query_id: int, true_ids: List[str], predicted_ids: List[str], label_df: pd.DataFrame, k: int = 10, partial_weight: float = 0.5
) -> float:
    """
    Calculate the Weighted Mean Average Precision at K (WMAP@K).

    Args:
        query_id: ID of the query.
        true_ids: List of relevant product IDs.
        predicted_ids: List of predicted product IDs.
        label_df: DataFrame containing label information.
        k: Number of top elements to consider.
        partial_weight: Weight for partial matches.

    Returns:
        WMAP@K score.
    """
    if not len(true_ids) or not len(predicted_ids):
        return 0.0

    score = 0.0
    weighted_hits = 0.0

    for i, product_id in enumerate(predicted_ids[:k]):
        if product_id in true_ids and product_id not in predicted_ids[:i]:
            label = label_df.loc[(label_df["query_id"] == query_id) & (label_df["product_id"] == product_id), "label"].values[0]

            weighted_hits += 1.0 if label == "Exact" else partial_weight
            score += weighted_hits / (i + 1.0)

    return score / min(len(true_ids), k)


def apply_weighted_map(row: pd.Series, label_df: pd.DataFrame, k: int = 10, partial_weight: float = 0.5) -> float:
    """
    Apply weighted MAP calculation to a row of data.

    Args:
        row: Series containing query_id, actuals, and preds.
        label_df: DataFrame containing label information.
        k: Number of top elements to consider.
        partial_weight: Weight for partial matches.

    Returns:
        WMAP@K score for the given row.
    """
    return weighted_map_at_k(
        query_id=row["query_id"],
        true_ids=row["actuals"],
        predicted_ids=row["preds"],
        label_df=label_df,
        k=k,
        partial_weight=partial_weight,
    )
