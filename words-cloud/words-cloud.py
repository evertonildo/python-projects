import pdfplumber

# Abra o arquivo PDF
pdf = pdfplumber.open("UsoInteligenciaArtificial.pdf")

# Selecione a primeira página (ou a página desejada)
pagina_pdf = pdf.pages[0]

# Extraia o texto da página
texto = pagina_pdf.extract_text()

# Feche o arquivo PDF
pdf.close()

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd

# Crie um DataFrame com as palavras e suas frequências
palavras_frequencia = pd.Series(texto.split()).value_counts()

# Crie a nuvem de palavras
wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(palavras_frequencia)

# Exiba a nuvem de palavras
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
