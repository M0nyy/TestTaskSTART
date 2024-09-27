import asyncio
from capture_metrics.collector import MetricsCapture
from capture_metrics.sender import MetricsSender


async def main():
    victoria_url = "http://127.0.0.1:8428/api/v1/import/prometheus"
    metrics_sender = MetricsSender(victoria_url)
    metrics_capture = MetricsCapture()
    
    
    while True:
        metrics = metrics_capture.capture_metrics()
        
        await metrics_sender.send_metrics(metrics)
        
        await asyncio.sleep(5)


if __name__ == '__main__':
    asyncio.run(main())
