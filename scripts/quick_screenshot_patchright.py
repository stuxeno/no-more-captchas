#!/usr/bin/env python3
"""
Quick screenshot capture using Patchright
Usage: python3 quick_screenshot_patchright.py <url> [output_file]
"""

import sys
import argparse
from pathlib import Path
from patchright.sync_api import sync_playwright

def main():
    parser = argparse.ArgumentParser(description='Capture screenshot with Patchright')
    parser.add_argument('url', help='URL to capture')
    parser.add_argument('output', nargs='?', default='screenshot.png', help='Output filename')
    parser.add_argument('--full-page', action='store_true', help='Capture full page')
    parser.add_argument('--width', type=int, default=1920, help='Viewport width')
    parser.add_argument('--height', type=int, default=1080, help='Viewport height')
    
    args = parser.parse_args()
    
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(viewport={'width': args.width, 'height': args.height})
            page = context.new_page()
            
            print(f"📸 Patchright: Capturing {args.url}...")
            page.goto(args.url)
            
            page.screenshot(path=args.output, full_page=args.full_page)
            browser.close()
            
            print(f"✅ Saved to {args.output}")
            return 0
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1

if __name__ == '__main__':
    sys.exit(main())
