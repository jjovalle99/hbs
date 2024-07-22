# HBS Take-home Assignment
#### Author: Juan Ovalle

## Overview
This repository contains the solution for the Harvard Business School take-home assignment about retrieval.

## Repository Structure
| Folder/File | Description |
| ----------- | ----------- |
| `data/` | Should contain the `label.csv`, `product.csv` and `query.csv` files to work. |
| `notebooks/` | Contains all the Jupyter Notebooks used for solving the assignment |
| `notebooks/HBS_retrieval_assignment.ipynb` | Base TF-IDF solution. |
| `notebooks/01_openai_solution.ipynb` | OpenAI embeddings solution. |
| `notebooks/02_open_source_embeddings.ipynb` | Open source embeddings solution. ❗ USES Metal Performance Shaders (MPS) |
| `notebooks/03_fine_tuneembeddings.ipynb` | Fine-tuning open source embeddings solution. ❗ USES GPU |
| `src/` | Contains all Python modules used for solving the assignment |
| `.env.copy` | Template for environment variables |
| `Makefile` | Contains shortcuts for various commands |

## Written answers
1. To improve the MAP@10 score of the search engine, several approaches can be considered. Utilizing pre-trained embedding models, both closed-source (like OpenAI's offerings `notebooks/01_openai_solution.ipynb`) and open-source options (`notebooks/02_open_source_embeddings.ipynb`), could enhance the semantic understanding of queries and documents. Fine-tuning these open-source models (`notebooks/03_fine_tuneembeddings.ipynb`) on domain-specific data might further improve performance. Additionally, implementing the BM25 algorithm, known for its effectiveness in information retrieval, could boost relevance scoring. A hybrid approach combining multiple techniques might yield the best results, leveraging the strengths of each method to create a more robust search system.

2. Regarding the evaluation of partial matches, implementing a function that assigns half a point for partial matches and a full point for exact matches could provide a more nuanced assessment of the search engine's performance. This approach acknowledges that partial matches still hold value, albeit less than exact matches, offering a fairer representation of the system's capabilities. Such a scoring method strikes a balance between rewarding precision and recognizing the relevance of close matches, potentially providing a more comprehensive view of the search engine's effectiveness. However, it's important to consider that this method might slightly inflate scores compared to stricter evaluation metrics, so using it alongside other established metrics could offer a more holistic performance assessment. This function was implemented in `src/evaluation`.

## Results

| Model | MAP@10 (Strict) | MAP@10 (Flexible)|
| ----- | --------------- | ----------------- |
| TF-IDF | 0.2931 | n/a |
| OpenAI Embeddings | 0.3867 | 0.5815 |
| Open Source Embeddings | 0.3212 | 0.5212 |
| Fine-tuned Embeddings ⭐ | 0.3939 | 0.6125 |

⭐ Fine tuning achieves score above 0.6, which is stated in the assignment as production level.

## Setup and Installation

### Prerequisites
- Python 3.11
- Poetry

### Steps
1. Install Python 3.11:
   ```
   pyenv install 3.11
   ```

2. Install Poetry:
   ```
   pip install poetry
   ```

3. Install project dependencies:
   ```
   poetry install
   ```

4. Copy `.env.copy` to `.env` and fill in the required environment variables.
