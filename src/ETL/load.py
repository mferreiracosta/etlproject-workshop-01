"""Módulo responsável pela carga dos dados no formato Excel."""

import os

import pandas as pd


def load_excel(df: pd.DataFrame, output_path: str, filename: str) -> str:
    """Receber um dataframe consolidado e salvar como excel.

    Args:
        df (pd.DataFrame): DataFrame consolidado a ser salvo como excel.
        output_path (str): Caminho da pata de destino onde o arquivo será salvo.
        filename (str): Nome do arquivo consolidado a ser salvo.

    Return: "Arquivo salvo com sucesso!"
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    df.to_excel(f"{output_path}/{filename}.xlsx", index=False)

    return "Arquivo salvo com sucesso!"


if __name__ == "__main__":
    df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    print(load_excel(df, "data/output", "teste"))
