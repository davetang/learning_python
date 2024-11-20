#!/usr/bin/env python3

import os
import sys
import psutil
import time

def check_available_memory():
    """Check and display the total and available memory."""
    mem = psutil.virtual_memory()
    print(f"Total Memory: {mem.total / (1024**3):.2f} GB")
    print(f"Available Memory: {mem.available / (1024**3):.2f} GB")

def allocate_memory(size_in_mb):
    """Try to allocate memory and hold it."""
    try:
        print(f"Attempting to allocate {size_in_mb} MB of memory...")
        # Allocate a list that roughly corresponds to the requested memory size
        size_in_bytes = size_in_mb * 1024 * 1024
        large_list = bytearray(size_in_bytes)  # Allocate memory
        print(f"Successfully allocated {size_in_mb} MB of memory. Holding it for 10 seconds...")
        time.sleep(10)  # Hold the memory for 10 seconds
        del large_list
        print("Memory released successfully.")
    except MemoryError:
        print("Memory allocation failed: MemoryError!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    script_name = os.path.basename(__file__)
    if len(sys.argv) != 2:
        print(f"Usage: python3 {script_name} <size_in_mb>")
        sys.exit(1)

    size_in_mb = int(sys.argv[1])
    check_available_memory()
    allocate_memory(size_in_mb)
