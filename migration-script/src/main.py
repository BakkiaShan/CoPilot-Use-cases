# migration-script/migration-script/src/main.py

import sys
from gemini_integration import GeminiIntegration
from net_upgrade_assistant import NetUpgradeAssistant

def main():
    print("Starting .NET Framework to .NET 8 Migration Assistant...")
    
    # Initialize Gemini LLM integration
    gemini = GeminiIntegration()
    
    # Initialize .NET Upgrade Assistant
    upgrade_assistant = NetUpgradeAssistant(gemini)
    
    # Start the migration process
    try:
        upgrade_assistant.run_migration()
    except Exception as e:
        print(f"An error occurred during migration: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()