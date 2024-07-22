import pandas as pd


def naive_map_at_k(true_ids, predicted_ids, k=10):
    """
    Calculate the Mean Average Precision at K (MAP@K).

    Parameters:
    true_ids (list): List of relevant product IDs.
    predicted_ids (list): List of predicted product IDs.
    k (int): Number of top elements to consider.
             NOTE: IF you wish to change top k, please provide a justification for choosing the new value

    Returns:
    float: MAP@K score.
    """
    # if either list is empty, return 0
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
    query_id: int, true_ids: list, predicted_ids: list, label_df: pd.DataFrame, k: int = 10, partial_weight: float = 0.5
):
    if not len(true_ids) or not len(predicted_ids):
        return 0.0

    score = 0.0
    weighted_hits = 0.0

    for i, product_id in enumerate(predicted_ids[:k]):
        if product_id in true_ids:
            label = label_df.loc[(label_df["query_id"] == query_id) & (label_df["product_id"] == product_id), "label"].values[0]
            if label == "Exact":
                weight = 1.0
            elif label == "Partial":
                weight = partial_weight
            else:
                weight = 0.0

            if product_id not in predicted_ids[:i]:
                weighted_hits += weight
                score += weighted_hits / (i + 1.0)

    return score / min(len(true_ids), k)
