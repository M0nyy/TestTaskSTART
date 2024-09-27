#TODO в перспективе это все закидывается в .env и добавляется в гитигнор

victoria_url = "http://127.0.0.1:8428"
victoria_url_to_send = "http://127.0.0.1:8428/api/v1/import/prometheus"

queries = {
        "cpu_usage_percent": "cpu_usage_percent",
        "memory_usage_percent": "memory_usage_percent",
        "disk_usage_percent": "disk_usage_percent"
    } # production

filename = "metrics.csv"