import yfinance as yf

# Dowload historial data for NVIDIA Corp (NVDA) from 2023-03-08 to 2024-03-08
nvda = yf.download('NVDA', start='2023-03-08', end='2024-03-08')

# Display the first few rows of data
print(nvda.head())
