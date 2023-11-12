"""Módulo principal do projeto."""

import os

from ETL.extract import extract_from_excel
from utils.absenteeism_generator import generate_absenteeism_data


def generate_excel_files(files: int = 10):
    """Gera n arquivos excel com dados de absenteísmo.

    Args:
        files (int, opcional): Número n de arquivos desejado. Valor padrão é 10.
    """
    for i in range(files):
        df = generate_absenteeism_data()
        print(df.head())
        output_path = os.path.join("data/input", f"absenteeism_data_{i}.xlsx")
        df.to_excel(output_path, index=False)


if __name__ == "__main__":
    # Rodar apenas uma vez a função para gerar os arquivos de teste
    # generate_excel_files(50)
    df_list = extract_from_excel("data/input")
    print(df_list)
