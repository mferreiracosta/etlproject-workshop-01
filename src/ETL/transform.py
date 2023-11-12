"""Módulo responsável por consolidar os dados de entradas."""

import pandas as pd
from typing import List


def concat_data_frames(df_list: List[pd.DataFrame]) -> pd.DataFrame:
    """Função que consolida uma lista de dataframes em um único dataframe.

    Args:
        df_list (List[pd.DataFrame]): Lista de dataframes.

    Returns:
        pd.DataFrame: DataFrame consolidado
    """
    if not df_list:
        raise ValueError("No data to transform.")
    consolidated_df = pd.concat(df_list, axis=0, ignore_index=True)

    return consolidated_df
