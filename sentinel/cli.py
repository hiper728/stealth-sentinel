#!/usr/bin/env python3
import argparse
import json
from sentinel.core import PageSnapshot

def main():
    p = argparse.ArgumentParser(description="Sentinel Web Change Inspector")
    p.add_argument("--html-file", help="Path to local HTML file to inspect")
    args = p.parse_args()
    if args.html_file:
        with open(args.html_file, "r", encoding="utf-8") as f:
            res = PageSnapshot.inspect_html(f.read(), url=args.html_file)
        print(json.dumps(res, indent=2))
    else:
        sample = "<html><body><h1>Production Status</h1><p>All services healthy.</p><a href='/docs'>Docs</a></body></html>"
        print(json.dumps(PageSnapshot.inspect_html(sample), indent=2))

if __name__ == "__main__":
    main()
