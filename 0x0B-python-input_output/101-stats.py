#!/usr/bin/python3
"""COntains print mechanics functions"""


import sys


def print_metrics(metrics):
    """
    Print the computed metrics.

    Args:
        metrics (dict): A dictionary containing the metrics.

    The function prints the total file size
    and the number of lines for each status code.
    """
    total_size = metrics.get('total_size', 0)
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        count = metrics.get(code, 0)
        if count > 0:
            print(f"{code}: {count}")


def main():
    metrics = {}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            data = line.split()
            if len(data) > 6:
                code = int(data[-2])
                size = int(data[-1])
                metrics['total_size'] = metrics.get('total_size', 0) + size
                metrics[code] = metrics.get(code, 0) + 1

            if line_count % 10 == 0:
                print_metrics(metrics)

    except KeyboardInterrupt:
        pass

    print_metrics(metrics)


if __name__ == "__main":
    main()
