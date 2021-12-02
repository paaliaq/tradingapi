"""Wraps synchronous I/O blocking calls."""

import asyncio
from functools import partial, wraps
from typing import Any, Callable


def async_wrap(func: Callable) -> Callable:
    """Wrap a synchronous function such that it can be called async.

    Args:
        func (Callable): The function to wrap.

    Returns:
        Callable: The async wrapper function.
    """

    @wraps(func)
    async def run(*args: Any, **kwargs: Any) -> Any:
        """The wrapped function."""
        loop = asyncio.get_event_loop()
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(None, pfunc)

    return run
