import csv
import os
from collections import defaultdict

def read_dataset(filename):
    processes = []
    allocation = {}
    request = {}

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            p = row['Process']
            processes.append(p)
            allocation[p] = row['Allocation']
            request[p] = row['Request']

    return processes, allocation, request

def build_wait_for_graph(processes, allocation, request):
    wfg = defaultdict(list)

    for p1 in processes:
        for p2 in processes:
            if p1 != p2:
                if request[p1] == allocation[p2]:
                    wfg[p1].append(p2)

    return wfg

def detect_cycle(wfg, processes):
    visited = set()
    stack = set()
    deadlock_processes = set()

    def dfs(p):
        if p in stack:
            deadlock_processes.update(stack)
            return True
        if p in visited:
            return False

        visited.add(p)
        stack.add(p)

        for neighbor in wfg[p]:
            if dfs(neighbor):
                return True

        stack.remove(p)
        return False

    for p in processes:
        if dfs(p):
            break

    return deadlock_processes

def main():
    # 🔥 INI BAGIAN PALING PENTING
    base_dir = os.path.dirname(__file__)
    filename = os.path.join(base_dir, "dataset_deadlock.csv")

    processes, allocation, request = read_dataset(filename)

    wfg = build_wait_for_graph(processes, allocation, request)
    deadlock = detect_cycle(wfg, processes)

    print("Wait-For Graph:")
    for p in wfg:
        print(f"{p} -> {wfg[p]}")

    if deadlock:
        print("\nDEADLOCK TERDETEKSI!")
        print("Proses yang terlibat deadlock:")
        for p in deadlock:
            print(p)
    else:
        print("\nTidak terjadi deadlock.")

if __name__ == "__main__":
    main()
