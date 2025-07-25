from jinja2 import Template

def generate_html_report(results, output_path):
    print("[+] Generating HTML report...")
    template_str = """
    <html><head><title>OSINT Report</title></head><body>
    <h1>OSINT Report</h1><pre>{{ results }}</pre>
    </body></html>
    """
    html = Template(template_str).render(results=results)
    with open(output_path, "w") as f:
        f.write(html)
