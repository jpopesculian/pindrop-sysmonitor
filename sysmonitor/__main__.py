import argparse
from .monitor import start_monitor
from .server import app

def main():
    parser = argparse.ArgumentParser(description="Monitor your system")

    parser.add_argument('--server', dest='server', action='store_true', help="start RESTful server (default)")
    parser.add_argument('--no-server', dest='server', action='store_false', help="don't start RESTful server")
    parser.set_defaults(server=True)

    parser.add_argument('--interval', '-i', dest='interval', type=int, default=5, help="how often to take stats in seconds (default 5)")

    args = parser.parse_args()

    if args.interval > 0:
       start_monitor(args.interval)

    if args.server:
        app.run()
    else:
        while True:
            pass

if __name__ == '__main__':
    main()