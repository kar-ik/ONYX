import typer
from typing import Optional
from rich.console import Console
from rich.table import Table
from .adapters import get_adapters
from .services import normalize_results, resolve_entities
from .storage import save_results, get_db_session, init_db as storage_init_db
from .utils import export_to_csv, print_timeline
from .config import load_config

app = typer.Typer()
console = Console()

def print_disclaimer():
    console.print("[bold red]ONYX OSINT Tool - Ethical Use Disclaimer[/]")
    console.print("This tool is for educational purposes and ethical OSINT only.")
    console.print("Only use with public data and comply with laws (e.g., GDPR, CCPA).")
    console.print("Respect robots.txt and terms of service of all sources.")
    console.print("Press Enter to agree and continue, or Ctrl+C to exit.")
    try:
        input()
    except KeyboardInterrupt:
        raise typer.Exit()

@app.command()
def search(query: str, sources: Optional[str] = None, export: Optional[str] = None):
    """
    Run OSINT search.
    --sources: Comma-separated (e.g., google,hibp); default all.
    --export: File path for CSV export.
    """
    print_disclaimer()
    config = load_config()
    adapter_list = get_adapters(sources.split(',') if sources else None, config)
    results = []
    for adapter in adapter_list:
        console.print(f"Searching {adapter.name}...")
        try:
            for result in adapter.search(query, {}):
                results.append(result)
        except Exception as e:
            console.print(f"[red]Error in {adapter.name}: {e}[/]")

    if not results:
        console.print("[yellow]No results found.[/]")
        return

    normalized = normalize_results(results)
    entities = resolve_entities(normalized)

    table = Table(title="Search Results")
    table.add_column("Source", style="cyan")
    table.add_column("Title")
    table.add_column("Snippet")
    for res in normalized:
        table.add_row(res['metadata']['source'], res['title'], res['snippet'])
    console.print(table)

    print_timeline(normalized)

    with get_db_session() as session:
        save_results(session, query, normalized)

    if export:
        export_to_csv(normalized, export)
        console.print(f"[green]Exported to {export}[/]")

@app.command()
def init_db():
    """
    Initialize the database.
    """
    storage_init_db()
    console.print("[green]Database initialized.[/]")
