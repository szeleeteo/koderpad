from pathlib import Path

import streamlit as st
from code_editor import code_editor

from utils import get_files

from .settings import DOCKERFILE_EDITOR_SETTINGS

EXERCISE_DIR = Path(__file__).resolve().parent / "exercises"
DOCKERFILE_EXT = ".Dockerfile"


def run():
    with st.sidebar:
        ex_files = get_files(EXERCISE_DIR, DOCKERFILE_EXT)
        selected_exercise = st.selectbox(
            label="Load an exercise",
            options=ex_files,
            format_func=lambda x: x.replace(DOCKERFILE_EXT, "").title(),
            key="dockerfile_exercise",
        )

    ex_text = (EXERCISE_DIR / selected_exercise).read_text()
    code_editor(lang="dockerfile", code=ex_text, **DOCKERFILE_EDITOR_SETTINGS)
