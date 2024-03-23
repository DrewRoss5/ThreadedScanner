# ThreadedScanner
A multithreaded port scanner written in Python

# Usage
To run the script, simply clone this repo and run `python src/main.py`

## Commands
<dl>
  <dt>help</dt>
  <dd>Prints a list of available commands and their usage</dd>
  <dt>scan [address(es)] </dt>
  <dd>Checks if the ports on the provided addresses are open, and displays the results. IP addresses are provided in a standard format, the address and port seperated by a colon (ex. 127.0.0.1:8080)<br>Example:<br> &nbsp;&nbsp;&nbsp;&nbsp;<code>python src/main.py scan 8.8.8.8:443, 8.8.8.8:80, 127.0.0.1:22, 127.0.0.1:123</code></dd>
  <dt>scan-threaded [thread count] [addresses]</dt>
  <dd>Scans port same as above, but is faster as it utilizes [thread count] threads to scan. The program delegates address to scan evenly among the threads.<br>Example:<br> &nbsp;&nbsp;&nbsp;&nbsp;<code>python src/main.py scan-threaded 2 8.8.8.8:443, 8.8.8.8:80, 127.0.0.1:22, 127.0.0.1:123</code></dd>
</dl>
