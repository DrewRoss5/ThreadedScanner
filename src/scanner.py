import threading
import socket

# returns if a provided port is open on a provided address
def scan_addr(addr: str, port: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((addr, port))
        s.close()
        return True
    except (ConnectionRefusedError, TimeoutError):
        return False

# TODO: Make this output scan results to a file, if desired
# runs scans of a provided list of addresses and ports
def scan_list(targets: list[(str, int)]):
    for i in targets:
        result = scan_addr(*i)
        print(f'{i[0]} on port {i[1]}: {"OPEN" if result else "CLOSED"}')

# calls the scan_all function on a provided number of threads
def start_scan(targets: list[str], thread_count: int = 1):
    # split each target into it's component address and port
    pairs = []
    for i in targets:
        try:
            addr, port = i.split(':')
            port = int(port)
        except ValueError:
            raise ValueError(f'Invalid address: {i}')
        if not 0 < port < 65535:
            raise ValueError(f'Invalid Port Number: {port}')
        pairs.append((addr, port))
    # assign targets to each thread
    thread_targets = [[] for i in range(thread_count)]
    # TODO: make this more efficient
    while pairs:
        for i in range(len(thread_targets)):
            if pairs:
                thread_targets[i].append(pairs.pop())
    # start the scan
    print("Starting scan...")
    for i in thread_targets:
        thread = threading.Thread(target = lambda: scan_list(i))
        thread.start()

    
    
    
