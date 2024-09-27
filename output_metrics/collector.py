import aiohttp
from datetime import datetime, timezone


class MetricsCollector:


    def __init__(self, victoria_url: str):
        self.victoria_url = victoria_url


    async def fetch_metrics(self, query: str) -> dict:
        
        now = datetime.now(timezone.utc)
        start_time = now.replace(minute=0, second=0, microsecond=0) # Округляю текущее время до начала часа
        end_time = now

        #   Преобразую в юникс 
        start_timestamp = int(start_time.timestamp()) 
        end_timestamp = int(end_time.timestamp())

        query_url = f"{self.victoria_url}/api/v1/query_range?query={query}&start={start_timestamp}&end={end_timestamp}&step=60"

        async with aiohttp.ClientSession() as session:
            async with session.get(query_url) as response:
                if response.status in (200, 204):
                    data = await response.json()
                    return data
                else:
                    print(f"Ошибка при запросе: {response.status}")
                    return {}