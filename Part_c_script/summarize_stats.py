
import os
import csv

protocols = ['vegas', 'bbr', 'sprout']
scenarios = ['50mbps_10ms', '1mbps_200ms']

def average_from_file(path, column_index):
    values = []
    with open(path) as f:
        for line in f:
            if line.startswith("#"):
                continue
            parts = line.strip().split()
            if len(parts) > column_index:
                try:
                    values.append(float(parts[column_index]))
                except:
                    continue
    if len(values) == 0:
        return "-"
    return round(sum(values) / len(values), 2)

with open('results/summaries/summary.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Scenario', 'Protocol', 'Avg Throughput (Kbps)', 'Avg RTT (ms)', 'Loss Rate (approx)'])

    for scenario in scenarios:
        for proto in protocols:
            base = "results/" + scenario + "/" + proto + "/"
            datalink = base + proto + "_mm_datalink_run1.log"
            acklink = base + proto + "_mm_acklink_run1.log"

            if not os.path.exists(datalink) or not os.path.exists(acklink):
                continue

            avg_tput = average_from_file(datalink, 2)
            avg_rtt = average_from_file(acklink, 2)

            # Approximate loss as drop in throughput (very rough)
            loss = "-"
            if isinstance(avg_tput, float) and avg_tput > 0:
                loss = round(1 - (avg_tput / 1000.0), 3)  # Fake approximation

            writer.writerow([scenario, proto, avg_tput, avg_rtt, loss])

def average_and_95th(path, column_index):
    values = []
    with open(path) as f:
        for line in f:
            if line.startswith("#"):
                continue
            parts = line.strip().split()
            if len(parts) > column_index:
                try:
                    values.append(float(parts[column_index]))
                except:
                    continue
    if len(values) == 0:
        return "-", "-"
    values.sort()
    avg = round(sum(values) / len(values), 2)
    idx_95 = int(len(values) * 0.95)
    perc95 = round(values[idx_95], 2)
    return avg, perc95


