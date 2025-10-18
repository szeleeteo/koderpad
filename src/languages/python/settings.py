"""
References
- https://code-editor-documentation.streamlit.app/Reference
- https://code-editor-documentation.streamlit.app/Advanced_usage#custom-buttons
- https://github.com/securingsincity/react-ace/blob/master/docs/Ace.md#available-props
- https://github.com/ajaxorg/ace/wiki/Configuring-Ace
"""

from utils import RUN_BUTTON

PYTHON_EDITOR_SETTINGS = {
    "height": [16, 24],
    "theme": "default",
    "focus": True,
    "buttons": [RUN_BUTTON],
    "props": {
        "enableBasicAutocompletion": True,
        "enableLiveAutocompletion": False,
        "enableSnippets": False,
    },
    "options": {"showLineNumbers": True, "wrap": True},
    "info": {"info": [{"name": "Python Editor"}]},
}
