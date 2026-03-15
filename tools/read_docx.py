#!/usr/bin/env python3
"""Read docx files without python-docx dependency"""
import zipfile
import xml.etree.ElementTree as ET
import sys

def read_docx(filepath):
    """Extract text from docx file"""
    try:
        docx = zipfile.ZipFile(filepath)
        content = docx.read('word/document.xml').decode('utf-8')
        
        root = ET.fromstring(content)
        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        
        texts = []
        for p in root.findall('.//w:p', ns):
            p_text = ''.join([t.text or '' for t in p.findall('.//w:t', ns)])
            if p_text.strip():
                texts.append(p_text.strip())
        
        return texts
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return []

if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else 'docs/Star_Courier_Characters.docx'
    texts = read_docx(filepath)
    
    print(f"=== {filepath} ===")
    print(f"Total paragraphs: {len(texts)}\n")
    
    for i, t in enumerate(texts):
        print(f"{i}: {t[:150]}")
        if i >= 40:
            print("... (truncated)")
            break
