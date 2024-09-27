import csv
from datetime import datetime, timezone


class MetricsWriter:


    def __init__(self, filename: str):
        self.filename = filename


    def write_to_csv(self, metrics: dict, metric_name: str) -> None:
        with open(self.filename, mode='a') as file:
            writer = csv.writer(file)
            writer.writerow(["DateTime", metric_name])

            for result in metrics.get("data", {}).get("result", []):
                for value in result.get("values", []):
                    timestamp, metric_value = value
                    
                    datetime_obj = datetime.fromtimestamp(timestamp, timezone.utc)
                    date_time = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')

                    writer.writerow([date_time, metric_value])

        print(f"Метрики успешно записаны в {self.filename}")