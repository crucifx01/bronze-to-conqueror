#! bin/bash

nmap --script dns-brute --script-args dns-brute.domain=cisco.com,dns-brute.threads=6

