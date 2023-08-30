def log_runtime(logger):
    """Log the runtime of the decorated function to the logger"""

    def decorator_log(func: Callable):
        @wraps(func)
        async def wrapper_timer(*args, **kwargs):
            start_time = time.perf_counter()
            resp = await func(*args, **kwargs)
            end_time = time.perf_counter()
            run_time = end_time - start_time

            logger.info(f"[TIME][Performance] {func.__name__!r} in {run_time:.4f} secs")
            return resp

        return wrapper_timer

    return decorator_log
