"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import os
import pandas as pd
import re

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    archivo_entrada = 'files/input/solicitudes_de_credito.csv'
    archivo_salida = 'files/output/solicitudes_de_credito.csv'

    df = pd.read_csv(archivo_entrada, sep=';', index_col=0)

    df['sexo'] = df['sexo'].str.lower()
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower().str.strip()
    df['barrio'] = df['barrio'].str.lower().str.replace('_', ' ', regex=False).str.replace('-', ' ', regex=False)
    df['idea_negocio'] = df['idea_negocio'].str.lower().str.replace('_', ' ', regex=False).str.replace('-', ' ', regex=False).str.strip()
    df['monto_del_credito'] = df['monto_del_credito'].str.strip().str.replace('$', '', regex=False).str.replace(',', '', regex=False).str.replace('.00', '', regex=False)
    df['monto_del_credito'] = pd.to_numeric(df['monto_del_credito'], errors='coerce')
    df['línea_credito'] = df['línea_credito'].str.lower().str.replace('_', ' ').str.replace('-', ' ').str.strip()
    df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce").combine_first(pd.to_datetime(df["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce"))
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)

    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    output_directory = os.path.dirname(archivo_salida)
    os.makedirs(output_directory, exist_ok=True)
    df.to_csv(archivo_salida, sep=';', index=False, encoding="utf-8")


pregunta_01() 
