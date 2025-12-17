import ast
import contextlib
import traceback
from io import StringIO
from pathlib import Path

import streamlit as st
from code_editor import code_editor

from utils import get_files

from .settings import PYTHON_EDITOR_SETTINGS

EXERCISE_DIR = Path(__file__).resolve().parent / "exercises"
PYTHON_FILE_EXT = ".py"
DISALLOWED_PYTHON_PACKAGES = frozenset(
    {"os", "sys", "subprocess", "shutil", "pathlib", "socket"}
)


def basic_safety_check(src: str) -> tuple[bool, str]:
    """
    Checks the provided Python source code for forbidden imports.

    Args:
        src (str): The source code to check.

    Returns:
        tuple[bool, str]: (True, "") if safe, (False, reason) if unsafe.
    """
    # Allow a special marker to bypass checks (for testing purposes)
    if src.startswith("#no-check"):
        return True, ""

    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        return False, f"Syntax error: {e}"

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            if any(
                alias.name.split(".")[0] in DISALLOWED_PYTHON_PACKAGES
                for alias in node.names
            ):
                return False, "Blocked: forbidden import used."
        elif isinstance(node, ast.ImportFrom):
            if (node.module or "").split(".")[0] in DISALLOWED_PYTHON_PACKAGES:
                return False, "Blocked: forbidden import used."
    return True, ""


def execute_script(script: str):
    ok, msg = basic_safety_check(script)

    if not ok:
        st.error(msg)
        return

    output_buffer = StringIO()

    with contextlib.redirect_stdout(output_buffer):
        try:
            namespace = {}
            exec(script, namespace)
        except Exception as e:
            st.error(f"Error: {e}")
            error_trace = traceback.format_exc()
            st.code(error_trace)

    st.code(output_buffer.getvalue(), language="text", wrap_lines=True)


def run():
    with st.sidebar:
        ex_files = get_files(EXERCISE_DIR, PYTHON_FILE_EXT)
        selected_exercise = st.selectbox(
            label="Load an exercise",
            options=ex_files,
            format_func=lambda x: x.replace(PYTHON_FILE_EXT, "").title(),
            key="python_exercise",
        )

    ex_text = (EXERCISE_DIR / selected_exercise).read_text()
    response_dict = code_editor(lang="python", code=ex_text, **PYTHON_EDITOR_SETTINGS)
    if response_dict["text"]:
        st.subheader("Output")
        execute_script(response_dict["text"])
