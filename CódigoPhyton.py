import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda = pd.read_csv(url)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

tienda.head()

facturacion_total_tienda = tienda['Precio'].sum() / 100
print(f"Facturación total (Tienda 1): ${facturacion_total_tienda:,.2f}\n")

facturacion_total_tienda2 = tienda2['Precio'].sum() / 100
print(f"Facturación total (Tienda 2): ${facturacion_total_tienda2:,.2f}\n")

facturacion_total_tienda3 = tienda3['Precio'].sum() / 100
print(f"Facturación total (Tienda 3): ${facturacion_total_tienda3:,.2f}\n")

facturacion_total_tienda4 = tienda4['Precio'].sum() / 100
print(f"Facturación total (Tienda 4): ${facturacion_total_tienda4:,.2f}\n")

#@title 2. Ventas por categoría
tiendas = {
    "Tienda 1": tienda,
    "Tienda 2": tienda2,
    "Tienda 3": tienda3,
    "Tienda 4": tienda4
}

for nombre, df in tiendas.items():
    print(f"--- Resultados para {nombre} ---")


    ventas_por_categoria = (
        df.groupby("Categoría del Producto")
        .size()
        .reset_index(name="Total Ventas")
        .sort_values(by="Total Ventas", ascending=False)
        .reset_index(drop=True)
    )

    categoria_mas_vendida = ventas_por_categoria.iloc[0]["Categoría del Producto"]

    styled_table = (
        ventas_por_categoria.style
        .hide(axis="index")
        .set_caption(f"Ventas por categoría en {nombre} | Categoría más vendida: {categoria_mas_vendida}")
        .format({"Total Ventas": "{:,.0f}"})
    )

    display(styled_table)
    print("\n" + "="*40 + "\n")

#@title 3. Calificación promedio de la tienda
tiendas = {
    "Tienda 1": tienda,
    "Tienda 2": tienda2,
    "Tienda 3": tienda3,
    "Tienda 4": tienda4
}
medias = []

for nombre, df in tiendas.items():
    media = df['Calificación'].mean()
    medias.append({
        "Tienda": nombre,
        "Media de Calificación": media
    })

df_medias = pd.DataFrame(medias).round(2)
styled_table = (
    df_medias.style
    .hide(axis="index")
    .set_caption("MEDIA DE CALIFICACIONES POR TIENDA")
    .background_gradient(cmap='Blues', subset=["Media de Calificación"])
    .format({
        "Media de Calificación": "{:.2f} ★"
    })
)

display(styled_table)

# @title 4. Productos más y menos vendidos
tiendas = {
    "Tienda 1": tienda,
    "Tienda 2": tienda2,
    "Tienda 3": tienda3,
    "Tienda 4": tienda4
}

resultados = []

for nombre, df in tiendas.items():
    ventas_producto = df['Producto'].value_counts()


    producto_mas_vendido = ventas_producto.index[0]
    total_mas_vendido = ventas_producto.iloc[0]


    producto_menos_vendido = ventas_producto.index[-1]
    total_menos_vendido = ventas_producto.iloc[-1]

    resultados.append({
        "Tienda": nombre,
        "Producto Más Vendido": producto_mas_vendido,
        "Ventas (Más Vendido)": total_mas_vendido,
        "Producto Menos Vendido": producto_menos_vendido,
        "Ventas (Menos Vendido)": total_menos_vendido
    })

df_resultados = pd.DataFrame(resultados)
styled_table = (
    df_resultados.style
    .hide(axis="index")
    .set_caption("PRODUCTOS MÁS Y MENOS VENDIDOS POR TIENDA")
    .background_gradient(cmap='Greens', subset=["Ventas (Más Vendido)"])
    .background_gradient(cmap='Reds', subset=["Ventas (Menos Vendido)"])
    .format({
        "Ventas (Más Vendido)": "{:,.0f}",
        "Ventas (Menos Vendido)": "{:,.0f}"
    })
)

display(styled_table)

# @title 5. Envío promedio por tienda

tiendas = {
    "Tienda 1": tienda,
    "Tienda 2": tienda2,
    "Tienda 3": tienda3,
    "Tienda 4": tienda4
}

resultados = []

for nombre, df in tiendas.items():
    promedio_envio = df['Costo de envío'].mean()
    total_envios = df['Costo de envío'].count()
    total_gastado = df['Costo de envío'].sum()

    resultados.append({
        "Tienda": nombre,
        "Promedio Costo de Envío": promedio_envio,
        "Total Envíos": total_envios,
        "Total Gastado en Envíos": total_gastado
    })

df_promedios = pd.DataFrame(resultados).round(2)
styled_table = (
    df_promedios.style
    .hide(axis="index")
    .set_caption("PROMEDIO DE COSTO DE ENVÍO POR TIENDA")
    .background_gradient(cmap='YlOrRd', subset=["Promedio Costo de Envío"])
    .format({
        "Promedio Costo de Envío": "${:,.2f}",
        "Total Gastado en Envíos": "${:,.2f}"
    })
)

display(styled_table)

# @title Facturación Bruta por Punto de Venta

import matplotlib.pyplot as plt

facturaciones = [
    facturacion_total_tienda,
    facturacion_total_tienda2,
    facturacion_total_tienda3,
    facturacion_total_tienda4
]
nombres_tiendas = list(tiendas.keys())
colores = ['#4CAF50', '#2196F3', '#FF9800', '#9C27B0']

plt.figure(figsize=(10, 6))
barras = plt.bar(nombres_tiendas, facturaciones, color=colores)

# Título más ejecutivo
plt.title('Comparativo de Ingresos Brutos por Punto de Venta', fontsize=16, fontweight='bold')
plt.ylabel('Facturación (USD)', fontsize=12)
plt.xlabel('Tiendas', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Línea del promedio
promedio_facturacion = sum(facturaciones) / len(facturaciones)
plt.axhline(promedio_facturacion, color='red', linestyle='--', linewidth=1.5, label=f'Promedio: ${promedio_facturacion:,.2f}')
plt.legend()

# Etiquetas de cada barra
for barra in barras:
    altura = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2, altura + 100, f"${altura:,.2f}",
             ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()

# @title Análisis de las Categorías Más Relevantes por Volumen de Venta

import matplotlib.pyplot as plt

ventas_combinadas = pd.concat([tienda, tienda2, tienda3, tienda4])

ventas_por_categoria = (
    ventas_combinadas.groupby("Categoría del Producto")
    .size()
    .reset_index(name="Total Ventas")
    .sort_values(by="Total Ventas", ascending=False)
)

top5_categorias = ventas_por_categoria.head(5)

plt.figure(figsize=(10, 6))
colors = ['#2E7D32', '#1976D2', '#FFA000', '#8E24AA', '#D81B60']
barras = plt.barh(
    top5_categorias["Categoría del Producto"],
    top5_categorias["Total Ventas"],
    color=colors
)

plt.title("Top 5 Categorías con Mayor Demanda Consolidada", fontsize=16, fontweight='bold')
plt.xlabel("Cantidad Total de Ventas", fontsize=12)
plt.ylabel("Categoría", fontsize=12)
plt.gca().invert_yaxis()  # Para mostrar la más vendida arriba
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Etiquetas con formato profesional
for barra in barras:
    ancho = barra.get_width()
    plt.text(
        ancho + 40,
        barra.get_y() + barra.get_height() / 2,
        f"{int(ancho):,}",
        va='center',
        fontsize=10,
        fontweight='bold'
    )

plt.tight_layout()
plt.show()

#@title Costo promedio de envio por tienda

tiendas = {
    "Tienda 1": tienda,
    "Tienda 2": tienda2,
    "Tienda 3": tienda3,
    "Tienda 4": tienda4
}

promedios_envio = {}
for nombre, df in tiendas.items():
    promedio = df['Costo de envío'].mean()
    promedios_envio[nombre] = promedio

df_promedios = pd.DataFrame.from_dict(promedios_envio, orient='index', columns=["Promedio Costo de Envío"])

plt.figure(figsize=(10, 7))
colores = ['#4CAF50', '#2196F3', '#FF9800', '#9C27B0']

explode = [0, 0, 0, 0]


plt.pie(
    df_promedios["Promedio Costo de Envío"],
    labels=df_promedios.index,
    colors=colores,
    explode=explode,
    autopct=lambda p: f'{p:.1f}%\n(${p * sum(promedios_envio.values())/100:,.2f})',  # Muestra porcentaje y valor absoluto
    startangle=90,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)

plt.title("Promedio de Costo de Envío por Tienda", fontsize=16, fontweight='bold')
plt.legend(
    title="Tiendas",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
    labels=[f"{label}: ${value:,.2f}" for label, value in zip(df_promedios.index, df_promedios["Promedio Costo de Envío"])]
)

plt.tight_layout()
plt.show()
