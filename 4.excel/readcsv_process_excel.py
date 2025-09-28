import pandas as pd
import ssl

# SSL 검증 비활성화 (임시 해결)
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://raw.githubusercontent.com/tsdata/pandas-data-analysis/refs/heads/main/part7/data/wolesale_customers.csv'
df = pd.read_csv(url)
print(df.head())
print(f"데이터 크기: {df.shape}")  # 추가 정보