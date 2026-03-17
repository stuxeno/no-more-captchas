#!/usr/bin/env python3
"""
Web scraping template with anti-bot protection
Customize for your specific scraping needs
"""

import json
import sys
import random
import time
from patchright.sync_api import sync_playwright

def scrape_with_anti_bot(url):
    """
    Scrape data with anti-bot detection bypass
    """
    viewports = [
        {'width': 1920, 'height': 1080},
        {'width': 1366, 'height': 768},
        {'width': 1536, 'height': 864}
    ]
    
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    ]
    
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                '--disable-blink-features=AutomationControlled',
                '--no-sandbox',
                '--disable-dev-shm-usage'
            ]
        )
        
        context = browser.new_context(
            viewport=random.choice(viewports),
            user_agent=random.choice(user_agents)
        )
        
        page = context.new_page()
        
        print(f"🔍 Scraping {url}...")
        page.goto(url)
        
        # Random delay to appear more human
        time.sleep(random.uniform(1, 3))
        
        # Wait for content
        page.wait_for_selector('body')
        
        # Extract page data
        data = {
            'title': page.title(),
            'url': page.url,
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Example: Extract all links
        links = page.evaluate('''
            () => {
                const anchors = document.querySelectorAll('a[href]');
                return Array.from(anchors).map(a => ({
                    text: a.innerText.trim(),
                    href: a.href
                })).filter(l => l.text && l.href).slice(0, 20);
            }
        ''')
        data['links'] = links
        
        # Example: Extract specific elements
        # items = page.query_selector_all('.item-class')
        # for item in items:
        #     # Extract item data...
        
        browser.close()
        return data

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scrape_protected.py <url>")
        return 1
    
    url = sys.argv[1]
    
    try:
        data = scrape_with_anti_bot(url)
        
        # Save to JSON
        output_file = 'scraped_data.json'
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"✅ Data saved to {output_file}")
        print(f"📊 Found {len(data['links'])} links")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1

if __name__ == '__main__':
    sys.exit(main())
