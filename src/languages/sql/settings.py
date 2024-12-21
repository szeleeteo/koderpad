"""
References
- https://code-editor-documentation.streamlit.app/Reference
- https://code-editor-documentation.streamlit.app/Advanced_usage#custom-buttons
- https://github.com/securingsincity/react-ace/blob/master/docs/Ace.md#available-props
- https://github.com/ajaxorg/ace/wiki/Configuring-Ace
"""

# Import local modules
from utils import RUN_BUTTON

SQL_EDITOR_SETTINGS = {
    "lang": "sql",
    "height": [12, 12],
    "theme": "default",
    "focus": True,
    "buttons": [RUN_BUTTON],
    "props": {
        "enableBasicAutocompletion": True,
        "enableLiveAutocompletion": False,
        "enableSnippets": False,
    },
    "options": {"showLineNumbers": True, "wrap": True},
    "info": {"info": [{"name": "SQL Editor"}]},
    "allow_reset": True,
}
