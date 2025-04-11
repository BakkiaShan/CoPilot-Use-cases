# compatibility_analysis_server.py

class CompatibilityAnalysisServer:
    def __init__(self):
        self.compatibility_issues = []

    def analyze_compatibility(self, project):
        # Analyze the project for compatibility issues with .NET 8
        # This is a placeholder for actual analysis logic
        self.compatibility_issues = self.detect_issues(project)
        return self.compatibility_issues

    def detect_issues(self, project):
        # Placeholder for detecting compatibility issues
        issues = []
        # Logic to analyze project files and dependencies
        return issues

    def guide_manual_fixes(self, issues):
        # Provide guidance for manual fixes based on detected issues
        for issue in issues:
            print(f"Manual fix needed for: {issue}")
            # Logic to provide specific guidance

    def prompt_user_for_confirmation(self, message):
        response = input(f"{message} (yes/no): ")
        return response.lower() == 'yes'

    def run_analysis(self, project):
        issues = self.analyze_compatibility(project)
        if issues:
            if self.prompt_user_for_confirmation("Compatibility issues detected. Would you like guidance on manual fixes?"):
                self.guide_manual_fixes(issues)
        else:
            print("No compatibility issues found.")