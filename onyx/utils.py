from rich import print as rprint
import csv
import logging

logging.basicConfig(filename='onyx.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def print_timeline(results):
    sorted_res = sorted(results, key=lambda r: r.get('timestamp', ''), reverse=True)
    rprint("[bold]Timeline:[/]")
    for res in sorted_res:
        ts = res.get('timestamp', 'N/A')
        rprint(f"- {ts}: {res['title']} ({res['metadata']['source']})")
        logging.info(f"Timeline: {ts} - {res['title']}")

def export_to_csv(results, path):
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['url', 'title', 'snippet', 'timestamp', 'metadata'])
        writer.writeheader()
        writer.writerows(results)
    logging.info(f"Exported results to {path}")
