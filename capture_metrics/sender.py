import aiohttp


class MetricsSender:

    
    def __init__(self, victoria_url: str):
        self.victoria_url = victoria_url

    
    async def send_metrics(self, metrics: dict[str, int]) -> None:
        async with aiohttp.ClientSession() as session:
            metrics = [f"{key} {value}" for key, value in metrics.items()]
            metrics = '\n'.join(metrics)

            async with session.post(self.victoria_url, data=metrics) as response:
                if response.status in (200, 204):
                    print("Метрики успешно были отправлены")
                else:
                    print(f"Ошибка отправки метрик {response.status}")
    

