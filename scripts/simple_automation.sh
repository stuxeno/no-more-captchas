#!/bin/bash
#
# Simple browser automation with Agent Browser
# Demonstrates basic operations
#

URL="${1:-https://example.com}"

echo "🤖 Agent Browser Automation"
echo "📍 URL: $URL"
echo ""

# Open the page
echo "📄 Opening page..."
agent-browser open "$URL"

# Wait for page to load
sleep 2

# Take screenshot
echo "📸 Taking screenshot..."
agent-browser screenshot automation_screenshot.png

# Get page title (using text extraction)
echo "📝 Extracting page title..."
TITLE=$(agent-browser snapshot -i | grep -i title || echo "Not found")
echo "Title: $TITLE"

# Get all links (using text extraction)
echo "🔗 Extracting links..."
agent-browser text-all > page_text.txt
LINK_COUNT=$(grep -o "http" page_text.txt | wc -l)
echo "Found $LINK_COUNT links"

echo ""
echo "✅ Automation complete!"
echo "📁 Files generated:"
echo "   - automation_screenshot.png"
echo "   - page_text.txt"

# Cleanup
rm -f page_text.txt
