import asyncio
from output_metrics.collector import MetricsCollector
from output_metrics.writer import MetricsWriter

from settings import victoria_url, queries, filename


async def main():
  
    metrics_collector = MetricsCollector(victoria_url=victoria_url)
    metrics_writer = MetricsWriter(filename=filename)
    
    for metric_name, query in queries.items():
        metrics = await metrics_collector.fetch_metrics(query) # Получаем метрики
        metrics_writer.write_to_csv(metrics, metric_name)  # Записываем метрики в CSV

if __name__ == '__main__':
    asyncio.run(main())
