def ft_tqdm(lst: range) -> None:
    """
    Print a progress bar for an iterable range.
    """
    total = len(lst)
    bar_size = 95

    for i in lst:
        i += 1
        percent = (i / total) * 100
        filled_bar = int(i * bar_size // total)
        bar = '█' * filled_bar + '-' * (bar_size - filled_bar)
        print(f'\r{percent:.0f}%|{bar}| {i}/{total}', end='')
        yield i
