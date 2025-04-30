import matplotlib.pyplot as plt
import os

protocols = ['vegas', 'bbr', 'sprout']
scenarios = ['50mbps_10ms', '1mbps_200ms']

for scenario in scenarios:
    for proto in protocols:
        path = "results/" + scenario + "/" + proto + "/" + proto + "_mm_acklink_run1.log"
        if not os.path.exists(path):
            continue
        with open(path) as f:
            lines = f.readlines()
        times = []
        rtts = []
        for line in lines:
            if line.startswith("#"):
                continue
            parts = line.strip().split()
            if len(parts) >= 3:
                times.append(float(parts[0]))
                rtts.append(float(parts[2]))
        plt.plot(times, rtts, label=proto)
    plt.xlabel("Time (s)")
    plt.ylabel("RTT (ms)")
    plt.title("RTT over Time - " + scenario)
    plt.legend()
    plt.grid(True)
    plt.savefig("results/plots/rtt_" + scenario + ".png")
    plt.clf()

