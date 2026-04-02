#!/usr/bin/env python3
"""
Build script for Jar of Joy static site generator
Generates HTML files from Jinja2 templates with multilingual support
"""

import os
import shutil
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from src.config import LANGUAGES, DEFAULT_LANGUAGE, DAILY_QUOTES
import random

# Directories
BASE_DIR = Path(__file__).parent
TEMPLATES_DIR = BASE_DIR / 'src' / 'templates'
STATIC_DIR = BASE_DIR / 'src' / 'static'
OUTPUT_DIR = BASE_DIR / 'docs'

def clean_output_dir():
    """Clean the output directory"""
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def copy_static_files():
    """Copy static files to output directory"""
    if STATIC_DIR.exists():
        shutil.copytree(STATIC_DIR, OUTPUT_DIR / 'static', dirs_exist_ok=True)

def get_random_quote(lang_code):
    """Get a random daily quote for the specified language"""
    quote_data = random.choice(DAILY_QUOTES)
    return quote_data.get(lang_code, quote_data['en'])

def build_site():
    """Build the static site for all languages"""
    print("🏗️  Building Jar of Joy...")
    
    # Clean and prepare output directory
    clean_output_dir()
    
    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    
    # Build for each language
    for lang_code, lang_data in LANGUAGES.items():
        print(f"📝 Building {lang_data['name']} ({lang_code})...")
        
        translations = lang_data['translations']
        daily_quote = get_random_quote(lang_code)
        
        # Common context for all pages
        context = {
            'lang': lang_code,
            'lang_name': lang_data['name'],
            'lang_dir': lang_data['dir'],
            't': translations,
            'daily_quote': daily_quote,
            'languages': LANGUAGES,
            'current_lang': lang_code,
            'default_lang': DEFAULT_LANGUAGE,
        }
        
        # Build pages with language suffix
        pages = ['index', 'add', 'reveal', 'collection']
        
        for page in pages:
            template = env.get_template(f'{page}.html')
            # All files go to top-level docs folder with language suffix
            output_file = OUTPUT_DIR / f'{page}_{lang_code}.html'
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(template.render(**context))
            
            print(f"  ✅ {page}_{lang_code}.html")
    
    # Create index.html redirect to primary language
    print(f"📄 Creating index.html redirect to primary language ({DEFAULT_LANGUAGE})...")
    redirect_html = f"""<!DOCTYPE html>
<html lang="{DEFAULT_LANGUAGE}">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url=index_{DEFAULT_LANGUAGE}.html">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Redirecting...</title>
    <script>
        window.location.href = 'index_{DEFAULT_LANGUAGE}.html';
    </script>
</head>
<body>
    <p>Redirecting to <a href="index_{DEFAULT_LANGUAGE}.html">Jar of Joy</a>...</p>
</body>
</html>"""
    
    with open(OUTPUT_DIR / 'index.html', 'w', encoding='utf-8') as f:
        f.write(redirect_html)
    
    print("  ✅ index.html (redirect)")
    
    # Copy static files
    print("📦 Copying static files...")
    copy_static_files()
    
    # Create .nojekyll file for GitHub Pages
    (OUTPUT_DIR / '.nojekyll').touch()
    
    print("✨ Build complete! Site generated in 'docs' folder.")
    print(f"🌍 Languages: {', '.join([lang['name'] for lang in LANGUAGES.values()])}")

if __name__ == '__main__':
    build_site()

# Made with Bob
