import contextlib
from io import StringIO
from pathlib import Path

import streamlit as st
from code_editor import code_editor

from utils import get_files

from .settings import PYTHON_EDITOR_SETTINGS

EXERCISE_DIR = Path(__file__).resolve().parent / "exercises"
PYTHON_FILE_EXT = ".py"


def execute_script(script: str):
    output_buffer = StringIO()

    with contextlib.redirect_stdout(output_buffer):
        try:
            exec(script)
        except Exception as e:
            st.error(f"Error: {e}")

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
