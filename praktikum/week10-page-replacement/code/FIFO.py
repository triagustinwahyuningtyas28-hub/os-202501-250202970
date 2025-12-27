# Simulasi Page Replacement - FIFO

reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frames = 3

def fifo_page_replacement(ref, frames):
    memory = []
    page_faults = 0

    print("FIFO Page Replacement")

    for page in ref:
        if page in memory:
            print(f"Page {page}: HIT   | Memory: {memory}")
        else:
            page_faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            print(f"Page {page}: FAULT | Memory: {memory}")

    print("Total Page Fault (FIFO):", page_faults)

fifo_page_replacement(reference_string, frames)
