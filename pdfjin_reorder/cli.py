import sys, argparse
try:
    from .core import reorder_pdf
    from . import __version__
except (ImportError, ValueError):
    from pdfjin_reorder.core import reorder_pdf
    from pdfjin_reorder import __version__


def main():
    p = argparse.ArgumentParser(prog="pdfjin-reorder", description="Rearrange pages in a PDF.")
    p.add_argument("input", help="Input PDF file")
    p.add_argument("-p", "--pages", required=True, help="0-based page indices (e.g. '2,0,1')")
    p.add_argument("-o", "--output", required=True, help="Output PDF file")
    p.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    args = p.parse_args()
    try:
        order = [int(x.strip()) for x in args.pages.split(",") if x.strip().isdigit()]
        reorder_pdf(args.input, order=order, output=args.output)
        print(f"Reordered PDF saved -> {args.output}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr); sys.exit(1)


if __name__ == "__main__":
    main()
