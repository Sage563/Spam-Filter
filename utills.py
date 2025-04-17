def remove_by_value(d, target_value):
    return {k: v for k, v in d.items() if v != target_value}

