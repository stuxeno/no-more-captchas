#!/usr/bin/env python3
"""
Helper script to choose between Patchright and Agent Browser
Based on your specific use case
"""

def ask_question(question):
    """Ask a yes/no question"""
    while True:
        answer = input(f"{question} (y/n): ").lower().strip()
        if answer in ['y', 'yes']:
            return True
        elif answer in ['n', 'no']:
            return False
        print("Please answer 'y' or 'n'")

def recommend_tool():
    """Recommend the appropriate tool based on answers"""
    
    print("🤖 Browser Automation Tool Selector")
    print("=" * 50)
    print("Answer a few questions to find the right tool\n")
    
    # Question 1: Anti-bot detection
    anti_bot = ask_question("❓ Do you need to bypass bot detection or scrape protected sites?")
    
    # Question 2: Complexity
    complex = ask_question("❓ Is this a complex automation task (multiple steps, conditionals)?")
    
    # Question 3: Speed
    speed = ask_question("❓ Is speed/fast startup a priority?")
    
    # Question 4: Language preference
    python = ask_question("❓ Do you prefer to write automation code in Python?")
    
    # Question 5: Video/PDF
    media = ask_question("❓ Do you need video recording or PDF generation?")
    
    # Question 6: Simple task
    simple = ask_question("❓ Is this a simple one-off task (screenshot, quick navigation)?")
    
    print("\n" + "=" * 50)
    print("📊 Recommendation")
    print("=" * 50)
    
    # Decision logic
    patchright_score = 0
    agent_browser_score = 0
    
    if anti_bot:
        patchright_score += 3
    
    if complex:
        patchright_score += 2
    
    if speed:
        agent_browser_score += 2
    
    if python:
        patchright_score += 1
    
    if media:
        patchright_score += 2
    
    if simple:
        agent_browser_score += 1
    
    print(f"\nPatchright Score: {patchright_score}")
    print(f"Agent Browser Score: {agent_browser_score}\n")
    
    if patchright_score > agent_browser_score:
        print("✅ Recommended: **Patchright**")
        print("\nWhy:")
        if anti_bot:
            print("  • Anti-bot detection is required")
        if complex:
            print("  • Complex automation needs full API")
        if media:
            print("  • Video/PDF generation needed")
        if python:
            print("  • Python API preferred")
        
        print("\nExample command:")
        print("  python3 quick_screenshot_patchright.py https://example.com")
        
    elif agent_browser_score > patchright_score:
        print("✅ Recommended: **Agent Browser**")
        print("\nWhy:")
        if speed:
            print("  • Fast startup is needed")
        if simple:
            print("  • Simple task better suited for CLI")
        
        print("\nExample command:")
        print("  ./quick_screenshot_agent.sh https://example.com")
        
    else:
        print("⚖️  Either tool would work well!")
        print("\nBoth Patchright and Agent Browser can handle this task.")
        print("Choose based on your preference:")
        print("  • Use Patchright for: Anti-bot, Python API, advanced features")
        print("  • Use Agent Browser for: Speed, simplicity, CLI usage")
    
    print("\n" + "=" * 50)

def quick_reference():
    """Show quick reference for both tools"""
    print("\n📚 Quick Reference")
    print("=" * 50)
    print("\n🔧 Patchright:")
    print("  • Best for: Anti-bot, complex tasks, Python API")
    print("  • CLI: patchright screenshot <url> <output>")
    print("  • Python: from patchright.sync_api import sync_playwright")
    
    print("\n⚡ Agent Browser:")
    print("  • Best for: Speed, simplicity, CLI automation")
    print("  • CLI: agent-browser open <url>")
    print("  • CLI: agent-browser screenshot <output>")
    print("=" * 50)

def main():
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--quick':
        quick_reference()
    else:
        recommend_tool()
        quick_reference()

if __name__ == '__main__':
    main()
