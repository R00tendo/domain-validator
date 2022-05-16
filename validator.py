import socket
import argparse
from termcolor import colored

def main(args):
  if args.output_file:
   open(args.output_file, 'w').write('')
  with open(args.input_file, encoding='latin-1') as lines:
    for domain in lines:
       domain = domain.strip()
       try: 
        socket.gethostbyname(domain)
        print(colored(f'[+] {domain}', 'green'))
        if args.output_file:
          with open(args.output_file, 'a') as add_host:
           add_host.write(f'{domain}\n')
       except socket.gaierror:
          print(colored(f'[-] {domain}', 'red'))
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', '--input-file', help='A file that contains all the subdomains', required=True)
  parser.add_argument('-o', '--output-file', help='If you want output all valid subdomains to a file please specify it with this flag', required=False, nargs='?')
  args = parser.parse_args()
  main(args)
