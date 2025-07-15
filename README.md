#Alurastores

Análisis comparativo de desempeño entre cuatro tiendas para recomendar la venta de la menos eficiente como estrategia de reinversión.

Este ejercicio consistió en realizar un análisis comparativo del desempeño de cuatro tiendas de la cadena Alura Store, con el objetivo de identificar cuál de ellas debería ser vendida para liberar capital y reforzar las operaciones más rentables. Para lograrlo, se utilizó Python como herramienta principal de análisis de datos, aprovechando su ecosistema de bibliotecas especializadas. El proceso comenzó con la carga y exploración del conjunto de datos, empleando bibliotecas como pandas para la manipulación de datos tabulares y numpy para cálculos numéricos. Se llevó a cabo una limpieza de datos inicial, donde se identificaron y corrigieron inconsistencias en la escala de los precios, que presentaban dos ceros adicionales. Estos valores fueron ajustados dividiendo entre 100 para reflejar los ingresos reales. Posteriormente, se calcularon métricas clave por tienda, incluyendo:

Facturación total (suma de ingresos por ventas), Gastos en envíos, Utilidad neta (ingresos menos costos logísticos), Número total de envíos, y Calificación promedio de clientes.

Con estos datos, se construyó un Índice Compuesto de Desempeño (IDC), que integra tres dimensiones estratégicas: rentabilidad (utilidad neta), satisfacción del cliente (calificación promedio) y eficiencia operativa (utilidad neta por envío). Cada una de estas métricas fue normalizada a una escala entre 0 y 1 utilizando una fórmula estándar de normalización min-max, lo que permitió una comparación justa entre las tiendas.

Finalmente, se visualizaron los resultados mediante gráficos generados con matplotlib y seaborn, facilitando la interpretación de los datos y destacando las diferencias de rendimiento entre tiendas. A partir de este análisis, se concluyó que la Tienda 4 presentaba el desempeño más débil en las tres dimensiones evaluadas, y por lo tanto se recomendó su venta como una medida estratégica para optimizar recursos y fortalecer el crecimiento de las tiendas más rentables.
