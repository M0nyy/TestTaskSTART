import asyncio
from capture_metrics.collector import MetricsCapture
from capture_metrics.sender import MetricsSender
from settings import victoria_url_to_send


async def main():
    
    victoria_url = victoria_url_to_send

    metrics_sender = MetricsSender(victoria_url)
    metrics_capture = MetricsCapture()
    
    
    while True:
        metrics = metrics_capture.capture_metrics()
        
        await metrics_sender.send_metrics(metrics)
        
        await asyncio.sleep(60)


if __name__ == '__main__':
    asyncio.run(main())
