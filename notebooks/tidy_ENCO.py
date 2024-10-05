{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMS+OCcrE/x76zqh7FQZ8A5",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AngelBReal/Proyecto_IC_MCD_GINI/blob/agrega-raw/notebooks/tidy_ENCO.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# ***Proyecto 1. Descargando datos de la web***\n",
        "\n",
        "---\n",
        "\n",
        "Curso Ingeniería de Características\n"
      ],
      "metadata": {
        "id": "rRPFYvrXRL88"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Libreta con código para pasar a formaro tidy los datos de la Encuesta Nacional sobre Confianza del Consumidor (ENCO) en el año 2022, para su posterior comparación con los datos de la Encuesta Nacional de Ingresos y Gastos de los Hogares (ENIGH) en el mismo año."
      ],
      "metadata": {
        "id": "Mteinj_pRXZw"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xVvdA1a290bO",
        "outputId": "f53f7578-7fb9-4c98-cdbb-92125593e442"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Archivos extraídos de https://www.inegi.org.mx/contenidos/programas/enco/datosabiertos/2022/conjunto_de_datos_enco_2022_01_csv.zip\n",
            "Archivos extraídos de https://www.inegi.org.mx/contenidos/programas/enco/datosabiertos/2022/conjunto_de_datos_enco_2022_02_csv.zip\n",
            "Archivos extraídos de https://www.inegi.org.mx/contenidos/programas/enco/datosabiertos/2022/conjunto_de_datos_enco_2022_03_csv.zip\n",
            "Archivos extraídos de https://www.inegi.org.mx/contenidos/programas/enco/datosabiertos/2022/conjunto_de_datos_enco_2022_04_csv.zip\n",
            "Archivos extraídos de https://www.inegi.org.mx/contenidos/programas/enco/datosabiertos/2022/conjunto_de_datos_enco_2022_05_csv.zip\n",
            "Archivos extraídos de https://www.inegi.org.mx/contenidos/programas/enco/datosabiertos/2022/conjunto_de_datos_enco_2022_06_csv.zip\n",
            "Archivos extraídos de https://www.inegi.org.mx/contenidos/programas/enco/datosabiertos/2022/conjunto_de_datos_enco_2022_07_csv.zip\n",
            "Archivos extraídos de https://www.inegi.org.mx/contenidos/programas/enco/datosabiertos/2022/conjunto_de_datos_enco_2022_08_csv.zip\n",
            "Archivos extraídos de https://www.inegi.org.mx/contenidos/programas/enco/datosabiertos/2022/conjunto_de_datos_enco_2022_09_csv.zip\n",
            "Archivos extraídos de https://www.inegi.org.mx/contenidos/programas/enco/datosabiertos/2022/conjunto_de_datos_enco_2022_10_csv.zip\n",
            "Archivos extraídos de https://www.inegi.org.mx/contenidos/programas/enco/datosabiertos/2022/conjunto_de_datos_enco_2022_11_csv.zip\n",
            "Archivos extraídos de https://www.inegi.org.mx/contenidos/programas/enco/datosabiertos/2022/conjunto_de_datos_enco_2022_12_csv.zip\n"
          ]
        }
      ],
      "source": [
        "# Importar librerías necesarias\n",
        "import requests\n",
        "import zipfile\n",
        "import os\n",
        "import pandas as pd\n",
        "from io import BytesIO\n",
        "\n",
        "# URLs de los archivos a descargar (ajustar según sea necesario)\n",
        "base_url = \"https://www.inegi.org.mx/contenidos/programas/enco/datosabiertos/2022/\"\n",
        "urls = [f\"{base_url}conjunto_de_datos_enco_2022_{str(i).zfill(2)}_csv.zip\" for i in range(1, 13)]\n",
        "\n",
        "# Función para descargar y extraer archivos zip\n",
        "def descargar_y_extraer_zip(url, extract_path='/content/enco_2022'):\n",
        "    response = requests.get(url)\n",
        "    if response.status_code == 200:\n",
        "        with zipfile.ZipFile(BytesIO(response.content)) as z:\n",
        "            z.extractall(extract_path)\n",
        "            print(f\"Archivos extraídos de {url}\")\n",
        "    else:\n",
        "        print(f\"Error al descargar {url}\")\n",
        "\n",
        "# Descarga y extracción de los archivos en la carpeta enco_2022\n",
        "os.makedirs('/content/enco_2022', exist_ok=True)\n",
        "\n",
        "for url in urls:\n",
        "    descargar_y_extraer_zip(url)\n",
        "\n",
        "# Definir las columnas comunes y específicas para cada conjunto de datos\n",
        "columnas_comunes = ['fol', 'ent', 'con', 'v_sel', 'n_hog', 'h_mud']\n",
        "\n",
        "# Columnas específicas para cada archivo\n",
        "viv_especificas = ['ageb', 'fch_def']\n",
        "cs_especificas = ['i_per', 'ing']\n",
        "cb_especificas = [f'p{i}' for i in range(1, 16)]  # 'p1' a 'p15' para 'cb'\n",
        "\n",
        "# Definir las columnas que se usarán en cada conjunto de datos\n",
        "viv_cols = columnas_comunes + viv_especificas\n",
        "cs_cols = columnas_comunes + cs_especificas\n",
        "cb_cols = columnas_comunes + cb_especificas\n",
        "\n",
        "# Función para seleccionar las columnas relevantes\n",
        "def seleccionar_columnas(df, columnas_relevantes):\n",
        "    return df[columnas_relevantes]\n",
        "\n",
        "# Leer y filtrar los DataFrames de cada archivo\n",
        "base_path = '/content/enco_2022'\n",
        "\n",
        "# Función para leer y almacenar los DataFrames\n",
        "def cargar_datos(mes, tipo):\n",
        "    file_name = f'conjunto_de_datos_{tipo}_enco_2022_{str(mes).zfill(2)}.CSV'\n",
        "    folder_path = f'{base_path}/conjunto_de_datos_{tipo}_enco_2022_{str(mes).zfill(2)}/conjunto_de_datos'\n",
        "    file_path = os.path.join(folder_path, file_name)\n",
        "\n",
        "    if os.path.exists(file_path):\n",
        "        return pd.read_csv(file_path)\n",
        "    else:\n",
        "        print(f\"Archivo no encontrado: {file_name}\")\n",
        "        return pd.DataFrame()  # Devolver DataFrame vacío si no se encuentra el archivo\n",
        "\n",
        "# Almacenar los DataFrames filtrados para cada conjunto\n",
        "cs_enco_filtrado = [seleccionar_columnas(cargar_datos(i, 'cs'), cs_cols) for i in range(1, 13)]\n",
        "viv_enco_filtrado = [seleccionar_columnas(cargar_datos(i, 'viv'), viv_cols) for i in range(1, 13)]\n",
        "cb_enco_filtrado = [seleccionar_columnas(cargar_datos(i, 'cb'), cb_cols) for i in range(1, 13)]\n",
        "\n",
        "# Unir los DataFrames por las columnas comunes y concatenar los resultados\n",
        "df_final = pd.DataFrame()\n",
        "\n",
        "for cs_df, viv_df, cb_df in zip(cs_enco_filtrado, viv_enco_filtrado, cb_enco_filtrado):\n",
        "    # Solo hacer merge si los DataFrames no están vacíos\n",
        "    if not cs_df.empty and not viv_df.empty and not cb_df.empty:\n",
        "        temp = pd.merge(cs_df, viv_df, on=columnas_comunes, how='inner')\n",
        "        temp = pd.merge(temp, cb_df, on=columnas_comunes, how='inner')\n",
        "        df_final = pd.concat([df_final, temp], ignore_index=True)\n",
        "\n",
        "# Visualizar las primeras filas del DataFrame final\n",
        "df_final.head()\n",
        "\n",
        "# Guardar el DataFrame tidy procesado\n",
        "df_final.to_csv('/content/enco_2022/processed_enco_tidy.csv', index=False)\n"
      ]
    }
  ]
}