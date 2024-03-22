import scanner
from sys import argv, exit

def print_help():
    commands = {
        'help': ('', 'displays this message'),
        'scan': ('<target(s)>', 'scans the provided addre'),
        'scan-threaded': ('<thread count> <target(s)>', 'runs a multithreaded scan, utilizing a set number of threads to the scan')
    }
    print(f'Available Commands:\n\t{"Command:".ljust(15)}{"Arguments:".ljust(40)}Description:\n')
    for i in commands:
        print(f'\t{i.ljust(15)}{commands[i][0].ljust(40)}{commands[i][1]}')

# validate user arguments
if len(argv) < 2:
    print('Please provide a command')
    print_help()

# run the user's provided command
command = argv[1]
match command:
    case 'help':
        print_help()
    
    case 'scan':
        if len(argv) < 3:
            print('This command takes at least one argument')
            print_help()
            exit(1)
        try:
            scanner.start_scan(argv[2:])
        except ValueError as e:
            print(e)
    
    case 'scan-threaded':
        if len(argv) < 4:
            print('This command takes at least two arguments')
            print_help()
            exit(1)
        try:
            threads = argv[2]
            if not threads.isdigit():
                raise ValueError('Please provide a valid integer for the thread count')
            scanner.start_scan(argv[3:], int(threads))
        except ValueError as e:
            print(e)



    
