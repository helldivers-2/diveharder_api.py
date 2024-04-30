from prometheus_fastapi_instrumentator import Instrumentator, metrics

# from prometheus_fastapi_instrumentator.metrics import Info
# from prometheus_client import Counter

instrumentator = Instrumentator(
    should_group_status_codes=True,
    should_ignore_untemplated=False,
    should_group_untemplated=False,
    should_round_latency_decimals=True,
    should_instrument_requests_inprogress=True,
    excluded_handlers=[".*admin.*", "/metrics.py"],
    inprogress_name="inprogress",
    inprogress_labels=True,
)

instrumentator.add(
    metrics.request_size(
        should_include_method=True,
        should_include_status=True,
        should_include_handler=True,
        metric_namespace="request",
        metric_subsystem="size",
    )
).add(
    metrics.response_size(
        should_include_handler=True,
        should_include_status=True,
        should_include_method=False,
        metric_namespace="response",
        metric_subsystem="size",
    )
).add(
    metrics.latency(
        should_include_handler=True,
        should_include_status=True,
        should_include_method=False,
        metric_namespace="latency",
    )
)
