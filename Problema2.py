import pandas as pd
import numpy as np

# Crear el DataFrame con los datos
data = pd.DataFrame({'x1': [1, 2, 3, 4, 5, 6],
                     'x2': [1, 2, 3, 1, 2, 7],
                     'x3': [32, 30, np.nan, np.nan, 27, 44],
                     'x4': [102, 121, 343, np.nan, 121, 125]})

# Imputar los datos faltantes con la media de cada columna
data_imputed = data.fillna(data.mean())

# Mostrar el DataFrame resultante
print(data_imputed)