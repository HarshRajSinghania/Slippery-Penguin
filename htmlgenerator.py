from yattag import Doc
from rich.console import Console
import json


def generate_PDF(b_exp):
    try:
        with open("art.txt", "r") as f:
            ascii_art = f.read()
    except FileNotFoundError:
        ascii_art = ""
    doc, tag, text = Doc().tagtext()
    with tag("html", lang="en"):
        with tag("head"):
            with tag("meta", charset="utf-8"):
                pass
            with tag("title"):
                text("Slippery Penguin PDF Report")

            with tag("style"):
                doc.asis("""
                @page {
                    margin: 0.5cm;              
                    size: Letter;                 
                    @top-right {
                        content: "Page " counter(page) " of " counter(pages);}}
""")

            with tag("style"):
                doc.asis(f"""
                    body::before {{
                        position: fixed;
                        bottom: 5px;
                        top: 50%;
                        left: 50%;
                        transform: translate(-50%, 0);
                        font-family: monospace;
                        font-size: 10px;
                        line-height: 8px;
                        color: rgba(0, 100, 0, 0.05);  
                        white-space: pre;
                        z-index: 0;
                        pointer-events: none;
                        width: 100%;      
                        text-align: center; 
                    }}

                    body {{
                        margin: 10;
                        padding: 20px;
                        background: #1a1a1a;
                        color: #00ff00;
                    }}

                    .header {{
                        text-align: center;
                        border: 2px solid green;
                        border-radius: 10px;
                        padding: 20px;
                        margin-bottom: 20px;
                        background: black;
                        page-break-after: avoid;
                    }}
                    .section {{
                        margin: 0;

... (rest of the file truncated for this example, but in real it would be full) ...

                        const displayText = formatContent(type, data[type]);
                        if (displayText !== null) {
                            const pre = document.createElement('pre');
                            pre.textContent = displayText;
                            section.appendChild(pre);
                        } else {
                            const msg = document.createElement('p');
                            // Specific message for GTFOBins as requested
                            msg.textContent = (type === 'gtfo') ? 'No matches found' : 'No results';
                            section.appendChild(msg);
                        }

                        resultsDiv.appendChild(section);
                    });
                }

                select.addEventListener('change', function() {
                    render(this.value);
                });

                render(select.value);
            })();
            </script>
            """
            doc.asis(js_code)

    return doc.getvalue()
