#!/usr/bin/env python3
import os
import subprocess
import argparse
import webbrowser
import urllib.parse
import re

# -------------------
# Tool functions
# -------------------


def show_cwd(args):
    print(f"📁 Current Directory: {os.getcwd()}")


def list_files(args):
    files = os.listdir(".")
    if files:
        for f in files:
            print(f)
    else:
        print("📂 Directory is empty")


def system_info(args):
    # Clean, readable system info
    os_name = subprocess.getoutput("uname -s")
    hostname = subprocess.getoutput("hostname")
    kernel = subprocess.getoutput("uname -r")
    arch = subprocess.getoutput("uname -m")

    print(f"🖥️  OS: {os_name}")
    print(f"🏷️  Hostname: {hostname}")
    print(f"🔧 Kernel: {kernel}")
    print(f"💻 Architecture: {arch}")


def ping_host(args):
    subprocess.run(["ping", "-c", "4", args.host])


def calc(args):
    try:
        result = eval(args.expression, {"__builtins__": {}})
        print(f"🧮 Result: {result}")
    except Exception as e:
        print(f"❌ Error: {e}")


def weather(args):
    if isinstance(args.city, list):
        city_name = " ".join(args.city)
    else:
        city_name = args.city
    city_name = city_name[:50]
    city_encoded = urllib.parse.quote(city_name)
    url = f"https://wttr.in/{city_encoded}?0"
    result = subprocess.run(["curl", "-s", url], capture_output=True, text=True)
    safe_text = re.sub(r"[\x00-\x08\x0b-\x1f\x7f]", "", result.stdout)
    print(safe_text)


def show_ip(args):
    print("🌐 Local IP:")
    subprocess.run(["ipconfig", "getifaddr", "en0"])
    print("\n🌍 Public IP:")
    subprocess.run(["curl", "-s", "https://ifconfig.me"])


def search(args):
    query = "+".join(args.query)
    webbrowser.open(f"https://www.google.com/search?q={query}")
    print(f"🔎 Searching Google for: {' '.join(args.query)}")


def take_file(args):
    open(args.filename, "a").close()
    print(f"✅ Created file: {args.filename}")


def del_file(args):
    try:
        os.remove(args.filename)
        print(f"🗑️ Deleted file: {args.filename}")
    except FileNotFoundError:
        print("❌ File not found!")


def list_processes(args):
    subprocess.run(["ps", "-ax"])


def disk_usage(args):
    subprocess.run(["df", "-h"])


def current_user(args):
    subprocess.run(["whoami"])


# -------------------
# CLI setup
# -------------------


def main():
    parser = argparse.ArgumentParser(
        prog="matchbox", description="Matchbox CLI Toolbox v2"
    )
    subparsers = parser.add_subparsers(title="commands")

    # Basic tools
    subparsers.add_parser("cwd", help="Show current directory").set_defaults(
        func=show_cwd
    )
    subparsers.add_parser("ls", help="List files").set_defaults(func=list_files)
    subparsers.add_parser("sysinfo", help="Show system info").set_defaults(
        func=system_info
    )
    ping_parser = subparsers.add_parser("ping", help="Ping a host")
    ping_parser.add_argument("host", help="Host to ping")
    ping_parser.set_defaults(func=ping_host)

    # Extra tools
    calc_parser = subparsers.add_parser("calc", help="Simple calculator")
    calc_parser.add_argument("expression", help="Expression to evaluate")
    calc_parser.set_defaults(func=calc)

    weather_parser = subparsers.add_parser("weather", help="Show weather for city")
    weather_parser.add_argument("city", nargs="+", help="City name (supports spaces)")
    weather_parser.set_defaults(func=weather)

    subparsers.add_parser("ip", help="Show local & public IP").set_defaults(
        func=show_ip
    )

    search_parser = subparsers.add_parser("search", help="Google search")
    search_parser.add_argument("query", nargs="+", help="Search query")
    search_parser.set_defaults(func=search)

    take_parser = subparsers.add_parser("take", help="Create a file")
    take_parser.add_argument("filename", help="Filename to create")
    take_parser.set_defaults(func=take_file)

    del_parser = subparsers.add_parser("del", help="Delete a file")
    del_parser.add_argument("filename", help="Filename to delete")
    del_parser.set_defaults(func=del_file)

    # System tools
    subparsers.add_parser("ps", help="List processes").set_defaults(func=list_processes)
    subparsers.add_parser("disk", help="Show disk usage").set_defaults(func=disk_usage)
    subparsers.add_parser("whoami", help="Show current user").set_defaults(
        func=current_user
    )

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
