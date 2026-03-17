#!/bin/bash
#
# Quick screenshot capture using Agent Browser
# Usage: ./quick_screenshot_agent.sh <url> [output_file]
#

URL="${1:-https://example.com}"
OUTPUT="${2:-screenshot.png}"

echo "📸 Agent Browser: Capturing $URL..."

# Use agent-browser to take screenshot
agent-browser open "$URL"
agent-browser screenshot "$OUTPUT"

if [ -f "$OUTPUT" ]; then
    SIZE=$(stat -f%z "$OUTPUT" 2>/dev/null || stat -c%s "$OUTPUT" 2>/dev/null)
    echo "✅ Saved to $OUTPUT (${SIZE} bytes)"
    exit 0
else
    echo "❌ Failed to capture screenshot"
    exit 1
fi
