import psutil


class MetricsCapture:


    def capture_metrics(self) -> dict:

        statistics: dict[str, int] = {}

        cpu_used: int = psutil.cpu_percent(interval=1.0) # Загрузка CPU 
        statistics['cpu_usage_percent'] = cpu_used

        mem_used: int = psutil.virtual_memory().percent # Загрузка MEM 
        statistics['memory_usage_percent'] = mem_used

        disk_used: int = psutil.disk_usage(path='/').percent # Загрузка Disk 
        statistics['disk_usage_percent'] = disk_used

        return statistics
    
    
    def __str__(self) -> str:
        metrics = self.capture_metrics()

        return f"Загрузка CPU {metrics['cpu_usage_percent']} ||| Загрузка MEM {metrics['memory_usage_percent']} ||| Загрузка Disk {metrics['disk_usage_percent']}"
    

    def __repr__(self) -> str:
        metrics = self.capture_metrics()

        return (f"MetricsCapture(cpu_used={metrics['cpu_usage_percent']}%, "
                f"mem_used={metrics['memory_usage_percent']}%, "
                f"disk_used={metrics['disk_usage_percent']}%)")




    