# Newsletter Generator

![Crewai-Newsletter-Image](https://github.com/othmansamih/Agents-Powered-Newsletter/blob/main/assets/crewai-newsletter.png)

This project provides a streamlined solution for generating personalized newsletters by automating research, editing, and formatting tasks. The system is powered by a modular architecture, including tools for gathering content, editing, and assembling newsletters into a polished HTML format. A user-friendly GUI built with Streamlit allows users to interact seamlessly with the system.

## Features
- **Research Automation**: Fetch the latest news based on a specified topic.
- **Editing Support**: Edit and reorder articles to improve readability and engagement.
- **HTML Newsletter Compilation**: Generate visually appealing newsletters using a predefined HTML template.
- **Custom Tools**: Leverage APIs for searching content and finding related articles.
- **Streamlit GUI**: Simplify interaction with an intuitive sidebar interface.

## Project Structure
```
.env
.gitignore
README.md
requirements.txt
pyproject.toml
src/
    gui/
        __init__.py
        app.py
    newsletter_gen/
        __init__.py
        config/
            agents.yaml
            newsletter_template.html
            tasks.yaml
        crew.py
        main.py
        tools/
            __init__.py
            custom_tool.py
```

### Key Files
- **`app.py`**: Defines the GUI for generating newsletters.
- **`agents.yaml`**: Configures the roles and goals of the researcher, editor, and designer agents.
- **`tasks.yaml`**: Details the tasks for researching, editing, and compiling the newsletter.
- **`custom_tool.py`**: Implements tools for searching and retrieving content using APIs.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd newsletter-generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add your `EXA_API_KEY` for using the custom tools.
   - Add your `OPENAI_API_KEY` for using the agents.

## Usage

1. **Run the GUI**:
   ```bash
   streamlit run src/gui/app.py
   ```

2. **Generate Newsletter**:
   - Enter the topic and a personal message in the sidebar.
   - Click "Generate the newsletter" to start the process.
   - Download the generated HTML file.

## Configuration
- **HTML Template**:
  Update `src/newsletter_gen/config/newsletter_template.html` to change the design of the newsletter.
- **Agent Behavior**:
  Modify `src/newsletter_gen/config/agents.yaml` to customize the roles and behavior of the system agents.
- **Task Instructions**:
  Update `src/newsletter_gen/config/tasks.yaml` for new or refined workflows.
