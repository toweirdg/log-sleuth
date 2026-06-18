from prometheus_client import Counter

logs_created_total = Counter(
    "logs_created_total",
    "Total logs ingested"
)

processing_failures_total = Counter(
    "processing_failures_total",
    "Total processing failures"
)
