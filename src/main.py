"""Módulo principal do projeto."""

import os

from .ETL.extract import extract_from_excel
from .ETL.load import load_excel
from .ETL.transform import concat_dataframes
from .utils.absenteeism_generator import generate_absenteeism_data


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


def full_pipeline(input_path: str, output_path: str, output_filename: str):
    """Organiza todo ETL do projeto.

    Args:
        input_path (str): Caminho da pasta de entrada com os arquivos.
        output_path (str): Caminho da pata de destino onde o arquivo será salvo.
        output_filename (str): Nome do arquivo consolidado a ser salvo.
    """
    df_list = extract_from_excel(input_path)
    consolidated_df = concat_dataframes(df_list)
    print(load_excel(consolidated_df, output_path, output_filename))


if __name__ == "__main__":
    # Rodar apenas uma vez a função para gerar os arquivos de teste
    # generate_excel_files(50)

    input_path = "data/input"
    output_path = "data/output"
    output_filename = "consolidated_absenteeism_data"
    full_pipeline(input_path, output_path, output_filename)
    print("Finished ETL successfuly!")
