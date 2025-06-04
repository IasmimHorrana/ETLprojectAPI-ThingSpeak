## 🌡️ IoT ETL Pipeline com ThingSpeak + OpenWeatherMap 

Este projeto implementa uma pipeline de dados end-to-end para ingestão, transformação e visualização de dados ambientais em tempo real, usando sensores públicos do ThingSpeak e dados climáticos do OpenWeatherMap.

### 🎯 Objetivo

- Coletar dados de sensores reais de temperatura, umidade e pressão via ThingSpeak
- Enriquecer os dados com previsão do tempo do OpenWeatherMap
- Limpar e transformar os dados com Pandas
- Armazenar os dados em PostgreSQL com Docker
- Visualizar os dados com dashboards interativos
- Emitir alertas automáticos com base em regras.

### 🧱 Tecnologias Utilizadas

- Python (pandas, requests, SQLAlchemy, dotenv)
- PostgreSQL + Docker + PGAdmin
- Streamlit (dashboards)
- ThingSpeak API
- OpenWeatherMap API