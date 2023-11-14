"""Módulo responsável pela extração dos dados."""

import glob
import os
from typing import List

import pandas as pd


def extract_from_excel(path: str) -> List[pd.DataFrame]:
    """Função para ler os arquivos um "path" e retornar uma lista de dataframes.

    Args:
        input_path (str): Caminho da pasta de entrada com os arquivos.

    Return:
        List[pd.DataFrame]: Lista de dataframes lidos do caminho de entrada.
    """
    all_files = glob.glob(os.path.join(path, "*.xlsx"))

    df_list = []
    for file in all_files:
        df_list.append(pd.read_excel(file))

    return df_list


if __name__ == "__main__":
    df_list = extract_from_excel(path="data/input")
    print(len(df_list))
