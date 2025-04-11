# Migration Script for .NET Framework to .NET 8

This project provides a migration script designed to assist in the migration of .NET Framework applications to .NET 8 and containerization on the OpenShift platform. The script integrates with the Gemini LLM to guide users through the migration process, ensuring that each step is confirmed and that the user is informed of any necessary actions.

## Project Structure

- `src/main.py`: Entry point of the migration script. Initializes the migration process and manages user interactions.
- `src/gemini_integration.py`: Handles communication with the Gemini LLM for user prompts and responses.
- `src/net_upgrade_assistant.py`: Implements core functionalities for automating project file updates, detecting obsolete APIs, and analyzing compatibility issues.
- `src/mcp_servers/`: Contains MCP servers for specific functionalities:
  - `project_update_server.py`: Automates project file updates.
  - `api_replacement_server.py`: Detects and replaces obsolete APIs.
  - `compatibility_analysis_server.py`: Analyzes compatibility issues and guides manual fixes.
- `src/utils/helpers.py`: Utility functions for logging, user input handling, and data validation.
- `requirements.txt`: Lists dependencies required for the project.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd migration-script
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage Guidelines

To start the migration process, run the following command:
```
python src/main.py
```

Follow the prompts provided by the Gemini LLM to guide you through each stage of the migration. The script will ensure that you confirm actions before proceeding and will provide insights into any compatibility issues or necessary manual fixes.

## Overview of Migration Process

1. **Initialization**: The script initializes the migration process and integrates with the Gemini LLM.
2. **Project File Updates**: The project update server automates updates to project files based on migration requirements.
3. **API Replacement**: The API replacement server detects obsolete APIs and suggests replacements.
4. **Compatibility Analysis**: The compatibility analysis server guides users through manual fixes where automation is not possible.
5. **Finalization**: The migration process concludes with a summary of changes and any remaining actions required.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.