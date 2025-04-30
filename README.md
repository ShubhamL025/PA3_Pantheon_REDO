# PA3_Pantheon_REDO


This evaluates and compares three congestion control (CC) protocols — **Vegas**, **BBR** and **Sprout**
by using Stanford’s [Pantheon](https://pantheon.stanford.edu/) framework with Mahimahi network emulation.

## Project Overview

Tested each protocol under two distinct network scenarios:

1. **High-bandwidth, low-latency**: 50 Mbps, 10 ms RTT  
2. **Constrained-bandwidth, high-latency**: 1 Mbps, 200 ms RTT

The experiments collect and analyze:
- Time-series throughput
-  Time-series RTT
-  Average & 95th-percentile RTT
-  Observed tradeoffs in aggressiveness, queue buildup, and delay-friendliness


## How to Reproduce

###  Prerequisites

- Ubuntu or Ubuntu VM (recommended inside VirtualBox)
- Python 2.7
- `matplotlib` for Python 2
- Pantheon dependencies:sudo apt-get install python-matplotlib mahimahi cmake g++ python-pip libboost-all-dev libsqlite3-dev iproute


### Step 1: Clone Pantheon

git clone https://github.com/StanfordSNR/pantheon.git
cd pantheon
git submodule update --init --recursive

### Step 2: Set Up & Run Experiments

python2 src/experiments/setup.py --all

# Example for BBR (50Mbps scenario)
python2 src/experiments/test.py local \
  --schemes "bbr" \
  --uplink-trace traces/50mbps_10ms.trace \
  --downlink-trace traces/50mbps_10ms.trace \
  --data-dir results/50mbps_10ms/bbr

Repeat for other protocols and scenarios from Lcommands.txt

## How to Generate Graphs & Summary

### Generate Throughput Graphs from: python Part_c_script/plot_throughput.py

### Generate RTT Graphs from :python Part_c_script/plot_rtt.py

### Generate Summary CSV from:  python Part_c_script/summarize_stats.py

All graphs are saved in `results/plots/` and the summary table appears in `results/summaries/summary.csv`.

