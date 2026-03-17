---
name: browser-automation
description: Browser automation with Patchright (anti-bot detection, Playwright API) and Agent Browser (fast CLI, Rust-based). Use for web scraping, automated testing, screenshots, form filling, and bypassing bot detection. Choose Patchright for anti-bot protection and full API. Choose Agent Browser for quick CLI operations.
---

# Browser Automation - Patchright & Agent Browser

This skill provides access to two powerful browser automation systems, each optimized for different use cases.

## Quick Decision Guide

### Choose **Patchright** when:
- ✅ Bypassing bot detection is required
- ✅ Complex web scraping from protected sites
- ✅ Full Playwright API needed
- ✅ Multi-language support (Python, Node.js, Java, .NET)
- ✅ Video recording or tracing needed
- ✅ PDF generation from webpages
- ✅ Network interception and monitoring
- ✅ Testing across multiple browsers (Chromium, Firefox, WebKit)

### Choose **Agent Browser** when:
- ✅ Quick, simple automation tasks
- ✅ Command-line operations
- ✅ Fast startup for one-off tasks
- ✅ Simple navigation and interaction
- ✅ Minimal overhead needed
- ✅ AI agent scripting workflows

## Patchright - Anti-Bot Detection Expert

### Installation
Already installed. Verify:
```bash
patchright --version  # Should show v1.58.2
```

### Command Line Quick Start

```bash
# Screenshot
patchright screenshot https://example.com screenshot.png

# PDF
patchright pdf https://example.com document.pdf

# Code generation
patchright codegen https://example.com

# Interactive browser
patchright open https://example.com
```

### Python API

```python
from patchright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://example.com')
    page.screenshot(path='screenshot.png')
    browser.close()
```

### Anti-Bot Features

Patchright is specifically designed to bypass common detection:

```python
browser = p.chromium.launch(
    headless=True,
    args=[
        '--disable-blink-features=AutomationControlled',
        '--no-sandbox'
    ]
)

context = browser.new_context(
    viewport={'width': 1920, 'height': 1080},
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
)
```

### Key Capabilities

**Multi-Browser Support:**
```bash
patchright cr https://example.com  # Chromium
patchright ff https://example.com  # Firefox  
patchright wk https://example.com  # WebKit
```

**Video Recording:**
```python
context = browser.new_context(record_video_dir='videos')
# ... perform actions ...
browser.close()  # Video saved automatically
```

**Network Interception:**
```python
def handle_route(route, request):
    print(f"Request: {request.url}")
    route.continue_()

page.route('**/*', handle_route)
```

**PDF Generation:**
```python
page.pdf(
    path='output.pdf',
    format='A4',
    print_background=True,
    margin={'top': '1cm', 'right': '1cm', 'bottom': '1cm', 'left': '1cm'}
)
```

## Agent Browser - Fast CLI Automation

### Installation
Already installed. Verify:
```bash
agent-browser --version  # Should show v0.20.13
```

### Quick Start

```bash
# Open page
agent-browser open https://example.com

# Take screenshot
agent-browser screenshot out.png

# Get element references
agent-browser snapshot -i

# Click element
agent-browser click @e1

# Fill form
agent-browser fill @e2 "text"

# Navigate
agent-browser goto https://another-site.com
```

### Element References

Agent Browser uses `@e1`, `@e2`, etc. to reference elements:

```bash
# Get all interactive elements
agent-browser snapshot -i

# Click specific element
agent-browser click @e3

# Fill input field
agent-browser fill @e5 "search query"

# Wait for element
agent-browser wait-for @e2
```

### Key Capabilities

**Simple Navigation:**
```bash
agent-browser open https://example.com
agent-browser click @e1
agent-browser goto /about
```

**Form Filling:**
```bash
agent-browser fill @e5 "John Doe"
agent-browser fill @e6 "john@example.com"
agent-browser click @e7  # Submit button
```

**Element Extraction:**
```bash
# Get text from element
agent-browser text @e3

# Get all text
agent-browser text-all
```

**Screenshot Specific Area:**
```bash
# Full page screenshot
agent-browser screenshot full.png

# Element-specific screenshot
agent-browser screenshot element.png --selector "@e3"
```

## Advanced Patterns

### Web Scraping with Patchright

```python
from patchright.sync_api import sync_playwright

def scrape_protected_site(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 ...'
        )
        page = context.new_page()
        
        page.goto(url)
        page.wait_for_selector('.content')
        
        data = page.evaluate('''
            () => {
                const items = document.querySelectorAll('.item');
                return Array.from(items).map(item => ({
                    title: item.querySelector('.title').innerText,
                    price: item.querySelector('.price').innerText
                }));
            }
        ''')
        
        browser.close()
        return data
```

### Quick Task with Agent Browser

```bash
# Fast screenshot for debugging
agent-browser open https://example.com
agent-browser screenshot debug.png
```

### Pagination Scraping

**Patchright:**
```python
base_url = 'https://example.com/page/'

for page_num in range(1, 11):
    page.goto(f'{base_url}{page_num}')
    page.wait_for_selector('.item')
    # Extract data...
```

**Agent Browser:**
```bash
for i in {1..10}; do
    agent-browser goto "https://example.com/page/$i"
    agent-browser screenshot "page_$i.png"
done
```

### Form Automation

**Patchright:**
```python
page.goto('https://example.com/form')
page.fill('input[name="name"]', 'John Doe')
page.select_option('select[name="country"]', 'US')
page.check('input[name="terms"]')
page.click('button[type="submit"]')
page.wait_for_url('**/success')
```

**Agent Browser:**
```bash
agent-browser open https://example.com/form
agent-browser fill @e1 "John Doe"
agent-browser fill @e2 "john@example.com"
agent-browser click @e3
```

## Performance Comparison

| Task | Patchright | Agent Browser |
|------|-----------|---------------|
| Simple screenshot | ⚠️ Medium (2-3s) | ✅ Fast (1-2s) |
| Anti-bot detection | ✅ Excellent | ❌ None |
| Multi-language | ✅ Python, Node.js, etc. | ❌ CLI only |
| API flexibility | ✅ Full Playwright API | ⚠️ Structured commands |
| Startup time | ⚠️ Medium | ✅ Fast |
| Memory usage | ⚠️ Higher | ✅ Lower |
| Learning curve | ⚠️ Steeper | ✅ Simpler |

## Best Practices

### Resource Management

**Patchright:**
```python
# Always use context manager
with sync_playwright() as p:
    browser = p.chromium.launch()
    # ... do work ...
    # Browser closes automatically
```

**Agent Browser:**
```bash
# Browser handles cleanup automatically
agent-browser open https://example.com
# ... do work ...
# Browser closes on completion
```

### Error Handling

**Patchright:**
```python
try:
    page.goto(url, timeout=30000)
except TimeoutError:
    print("Page load timed out")
except Exception as e:
    print(f"Error: {e}")
finally:
    browser.close()
```

**Agent Browser:**
```bash
# CLI handles errors with clear messages
agent-browser open https://example.com || echo "Failed to load page"
```

### Anti-Detection Tips

**Randomize timing:**
```python
import random
import time

actions = [lambda: page.click('.button1'), lambda: page.click('.button2')]
for action in actions:
    action()
    time.sleep(random.uniform(1, 3))
```

**Use realistic viewports:**
```python
viewports = [
    {'width': 1920, 'height': 1080},
    {'width': 1366, 'height': 768},
    {'width': 1536, 'height': 864}
]
context = browser.new_context(viewport=random.choice(viewports))
```

## Integration Examples

### WhatsApp Integration

**Patchright:**
```python
page.goto('data:text/html,' + html_content)
page.screenshot(path='screenshot.png')
# Then send via WhatsApp
```

**Agent Browser:**
```bash
agent-browser open "data:text/html,$html_content"
agent-browser screenshot screenshot.png
# Then send via WhatsApp
```

### Data Export

**Patchright:**
```python
import json

data = {
    'title': page.title(),
    'url': page.url,
    'content': page.content()
}

with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)
```

## Troubleshooting

### Common Issues

**Issue:** Page loading timeout
```python
# Patchright
page.goto(url, timeout=60000)

# Agent Browser (CLI handles timeouts automatically)
```

**Issue:** Element not found
```python
# Patchright
page.wait_for_selector('.element', timeout=10000)

# Agent Browser
agent-browser wait-for @e1
```

**Issue:** Captcha or verification
```python
# Patchright - use non-headless for manual intervention
browser = p.chromium.launch(headless=False)
page.goto(url)
page.wait_for_timeout(30000)  # Wait for manual captcha
# Continue automation
```

### Debug Mode

**Patchright:**
```python
browser = p.chromium.launch(
    headless=False,
    slow_mo=1000  # Slow down by 1 second
)

def console_message(msg):
    print(f"Console: {msg.text}")

page.on('console', console_message)
```

**Agent Browser:**
```bash
# CLI provides clear error messages
agent-browser open https://example.com
# Any errors are displayed in output
```

## Additional Resources

- **Patchright GitHub:** https://github.com/Kaliiiiiiiiii-Vinyzu/patchright-nodejs
- **Playwright Docs:** https://playwright.dev/python/ (compatible API)
- **Agent Browser:** See `scripts/` for examples

## When to Use This Skill

Use this browser automation skill when you need to:
- Scrape data from websites
- Automate repetitive browser tasks
- Bypass bot detection systems
- Capture screenshots or PDFs
- Fill forms automatically
- Test web applications
- Monitor websites for changes

Choose the right tool based on complexity, anti-bot requirements, and performance needs.
