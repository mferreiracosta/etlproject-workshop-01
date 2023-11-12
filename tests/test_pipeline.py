import pandas as pd

from src.ETL.transform import concat_dataframes

df_1 = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
df_2 = pd.DataFrame({"col1": [5, 6], "col2": [7, 8]})


def testar_a_concatenacao_da_lista_de_dataframes():
    """Usando arrange, act e assert para testar a função concact_data_frames"""
    # arrange
    df_list = [df_1, df_2]

    # act
    df = concat_dataframes(df_list)

    assert df.shape == (4, 2)
    assert df.equals(pd.concat(df_list, axis=0, ignore_index=True))
