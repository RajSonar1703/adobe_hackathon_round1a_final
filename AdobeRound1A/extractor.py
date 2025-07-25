
import fitz  # PyMuPDF
import os
import json

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    title = doc.metadata.get("title", "Untitled Document")
    outline = []

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" in b:
                for line in b["lines"]:
                    text = " ".join([span["text"] for span in line["spans"]]).strip()
                    font_size = line["spans"][0]["size"]
                    
                    # Heuristic: Define heading levels based on font size (relative)
                    if font_size > 20:
                        level = "H1"
                    elif font_size > 16:
                        level = "H2"
                    elif font_size > 13:
                        level = "H3"
                    else:
                        continue  # Skip small text
                    
                    outline.append({
                        "level": level,
                        "text": text,
                        "page": page_num
                    })

    return {
        "title": title,
        "outline": outline
    }

if __name__ == "__main__":
    import sys
    input_dir = "input"
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            full_path = os.path.join(input_dir, filename)
            output_json = extract_outline(full_path)
            out_file_path = os.path.join(output_dir, filename.replace(".pdf", ".json"))
            with open(out_file_path, "w") as f:
                json.dump(output_json, f, indent=2)
