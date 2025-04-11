import os
import subprocess

# Migration script for .NET Upgrade Assistant

class NetUpgradeAssistant:
    def __init__(self, gemini_integration):
        self.gemini_integration = gemini_integration

    def update_project_files(self, project_path):
        # Logic to update project files
        prompt_message = "Updating project files to .NET 8. Do you want to proceed?"
        if self.gemini_integration:
            gemini_response, user_confirmed = self.gemini_integration.prompt_user(prompt_message)
            if not user_confirmed:
                print("Project file update cancelled by user.")
                return
        else:
            print("Gemini integration not available. Proceeding with project file updates.")

        try:
            # 1. Backup the project file
            backup_path = os.path.join(project_path, "project.backup")
            project_file = [f for f in os.listdir(project_path) if f.endswith(".csproj")][0] #Find the .csproj file
            project_file_path = os.path.join(project_path, project_file)
            print(f"Backing up {project_file_path} to {backup_path}")
            os.rename(project_file_path, backup_path)

            # 2. Create a new .NET 8 project file
            new_project_file_content = f"""<Project Sdk="Microsoft.NET.Sdk">
    <PropertyGroup>
        <TargetFramework>net8.0</TargetFramework>
        <OutputType>Exe</OutputType>  <!-- Adjust as needed: Exe, Library, etc. -->
        <ImplicitUsings>enable</ImplicitUsings>
        <Nullable>enable</Nullable>
    </PropertyGroup>
</Project>"""

            with open(project_file_path, "w") as f:
                f.write(new_project_file_content)
            print(f"Created new .NET 8 project file at {project_file_path}")

            # 3.  (Simplified)  Add back source files.  A more robust solution would analyze the old project file.
            source_files = [f for f in os.listdir(project_path) if f.endswith(".cs")]
            print("Keeping source files:", source_files)

            print("Project files updated to .NET 8.")

            #4. Prompt Gemini to analyze the changes and suggest further steps
            if self.gemini_integration:
                analysis_prompt = f"I've updated the project file at {project_path} to .NET 8.  The original project file was backed up to {backup_path}. The following source files were kept: {source_files}.  What are the next steps I should take to ensure a successful migration, focusing on dependency updates and code compatibility?"
                gemini_response = self.gemini_integration.send_to_gemini(analysis_prompt)
                print(f"Gemini suggests: {gemini_response}")


        except Exception as e:
            print(f"Error updating project files: {e}")


    def detect_obsolete_apis(self, codebase):
        # Logic to detect obsolete APIs
        if self.gemini_integration:
            self.gemini_integration.prompt_user("Detecting obsolete APIs. Do you want to proceed?")
        else:
            print("Gemini integration not available. Proceeding with obsolete API detection.")
        # Perform detection
        # ...

    def replace_obsolete_apis(self, codebase):
        # Logic to replace obsolete APIs
        if self.gemini_integration:
            self.gemini_integration.prompt_user("Replacing obsolete APIs. Do you want to proceed?")
        else:
            print("Gemini integration not available. Proceeding with obsolete API replacement.")
        # Perform replacements
        # ...

    def analyze_compatibility(self, project_path):
        # Logic to analyze compatibility issues
        self.gemini_integration.prompt_user("Analyzing compatibility issues. Do you want to proceed?")
        # Perform analysis
        # ...

    def guide_manual_fixes(self):
        # Logic to guide users through manual fixes
        self.gemini_integration.prompt_user("Guiding through manual fixes. Do you want to proceed?")
        # Provide guidance
        # ...
   
   
    def run_migration(self):
        
        project_path="/Users/bakkialakshmishanmugam/Downloads/dotnet-4.8-sample-app-master/DescopeSampleApp"
        self.update_project_files(project_path)
        self.detect_obsolete_apis(project_path)
        self.replace_obsolete_apis(project_path)
        self.analyze_compatibility(project_path)
        self.guide_manual_fixes()