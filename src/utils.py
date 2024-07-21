def gen_batches(iterable, n: int = 1000):
    """
    Generate batches of sizer n from an iterable.

    Args:
        iterable (iterable): The iterable to be batched.
        n (int, optional): The batch size. Defaults to 1000.

    Yields:
        iterable: A batch of the input iterable, with each batch being of size `n` or less.
    """
    length = len(iterable)
    for ndx in range(0, length, n):
        yield iterable[ndx: min(ndx + n, length)]
