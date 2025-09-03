#!/usr/bin/env python3
import os
import subprocess
import argparse
import webbrowser

def show_cwd(args):
    print(f"Current Directory: {os.getcwd()}")

def list_files(args):
    for f in os.listdir('.'):
        print(f)

def system_info(args):
    subprocess.run(["uname", "-a"])

def ping_host(args):
    subprocess.run(["ping", "-c", "4", args.host])

def calc(args):
    try:
        result = eval(args.expression, {"__builtins__": {}})
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

def weather(args):
    url = f"https://wttr.in/{args.city}"
    subprocess.run(["curl", "-s", url])

def show_ip(args):
    print("Local IP:")
    subprocess.run(["ipconfig", "getifaddr", "en0"])
    print("\nPublic IP:")
    subprocess.run(["curl", "-s", "https://ifconfig.me"])

def search(args):
    query = "+".join(args.query)
    webbrowser.open(f"https://www.google.com/search?q={query}")
    print(f"Searching Google for: {' '.join(args.query)}")

def take_file(args):
    open(args.filename, 'a').close()
    print(f"Created file: {args.filename}")

def del_file(args):
    try:
        os.remove(args.filename)
        print(f"Deleted file: {args.filename}")
    except FileNotFoundError:
        print("File not found!")

def main():
    parser = argparse.ArgumentParser(prog="matchbox", description="Matchbox CLI Toolbox")
    subparsers = parser.add_subparsers(title="commands")

    # Basic tools
    parser_cwd = subparsers.add_parser("cwd", help="Show current directory")
    parser_cwd.set_defaults(func=show_cwd)

    parser_ls = subparsers.add_parser("ls", help="List files")
    parser_ls.set_defaults(func=list_files)

    parser_sys = subparsers.add_parser("sysinfo", help="Show system info")
    parser_sys.set_defaults(func=system_info)

    parser_ping = subparsers.add_parser("ping", help="Ping a host")
    parser_ping.add_argument("host", help="Host to ping")
    parser_ping.set_defaults(func=ping_host)

    # Extra tools
    parser_calc = subparsers.add_parser("calc", help="Simple calculator")
    parser_calc.add_argument("expression", help="Expression to evaluate")
    parser_calc.set_defaults(func=calc)

    parser_weather = subparsers.add_parser("weather", help="Show weather")
    parser_weather.add_argument("city", help="City name")
    parser_weather.set_defaults(func=weather)

    parser_ip = subparsers.add_parser("ip", help="Show local & public IP")
    parser_ip.set_defaults(func=show_ip)

    parser_search = subparsers.add_parser("search", help="Google search")
    parser_search.add_argument("query", nargs="+", help="Search query")
    parser_search.set_defaults(func=search)

    parser_take = subparsers.add_parser("take", help="Create a file")
    parser_take.add_argument("filename", help="Filename to create")
    parser_take.set_defaults(func=take_file)

    parser_del = subparsers.add_parser("del", help="Delete a file")
    parser_del.add_argument("filename", help="Filename to delete")
    parser_del.set_defaults(func=del_file)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
