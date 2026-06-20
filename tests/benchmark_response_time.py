"""
Benchmark: prove sub-100ms API response time for POST /logs

Run with:
    python tests/benchmark_response_time.py

Requires the app to be running:
    docker compose up -d
"""

import httpx
import time
import statistics
import json

BASE_URL = "http://localhost:8000"

SAMPLE_PAYLOAD = {
    "message": "Database connection timeout after 30s",
    "level": "ERROR",
    "service": "auth-service",
    "host": "prod-01",
    "metadata": {"region": "ap-south-1"},
}

WARMUP_REQUESTS = 5
BENCHMARK_REQUESTS = 50


def run_benchmark():
    print(f"\nLogSleuth API Benchmark — POST /logs")
    print(f"Target: {BASE_URL}")
    print(f"Warmup: {WARMUP_REQUESTS} requests")
    print(f"Benchmark: {BENCHMARK_REQUESTS} requests\n")

    with httpx.Client(timeout=10.0) as client:
        # warmup
        for _ in range(WARMUP_REQUESTS):
            client.post(f"{BASE_URL}/logs", json=SAMPLE_PAYLOAD)

        # benchmark
        latencies = []
        failures = 0

        for i in range(BENCHMARK_REQUESTS):
            start = time.perf_counter()
            try:
                response = client.post(f"{BASE_URL}/logs", json=SAMPLE_PAYLOAD)
                end = time.perf_counter()

                if response.status_code == 200:
                    latency_ms = (end - start) * 1000
                    latencies.append(latency_ms)
                else:
                    failures += 1
                    print(f"  Request {i+1}: HTTP {response.status_code}")
            except Exception as e:
                failures += 1
                print(f"  Request {i+1}: ERROR — {e}")

        if not latencies:
            print("All requests failed. Is the server running?")
            return

        print(f"Results ({len(latencies)} successful / {failures} failed):")
        print(f"  Min:    {min(latencies):.2f}ms")
        print(f"  Max:    {max(latencies):.2f}ms")
        print(f"  Mean:   {statistics.mean(latencies):.2f}ms")
        print(f"  Median: {statistics.median(latencies):.2f}ms")
        print(f"  p95:    {sorted(latencies)[int(len(latencies)*0.95)]:.2f}ms")
        print(f"  p99:    {sorted(latencies)[int(len(latencies)*0.99)]:.2f}ms")
        print()

        p95 = sorted(latencies)[int(len(latencies) * 0.95)]
        if p95 < 100:
            print(f"✓ CLAIM VERIFIED: p95 latency {p95:.1f}ms < 100ms")
        else:
            print(f"✗ CLAIM FAILED: p95 latency {p95:.1f}ms exceeds 100ms")
            print("  Consider: add DB connection pooling, or change claim to p50 <100ms")


if __name__ == "__main__":
    run_benchmark()
