# Import standard library modules
import hmac
from pathlib import Path

# Import third-party library modules
import streamlit as st


def _password_entered():
    if hmac.compare_digest(st.session_state["app_password"], st.secrets["APP_PWD"]):
        st.session_state["password_correct"] = True
        del st.session_state["app_password"]
    else:
        st.session_state["password_correct"] = False


def check_password():
    """
    Based on https://docs.streamlit.io/knowledge-base/deploy/authentication-without-sso
    """
    if st.secrets.get("APP_PWD") is None or st.session_state.get(
        "password_correct", False
    ):
        return True

    st.text_input(
        "Password",
        type="password",
        on_change=_password_entered,
        key="app_password",
    )

    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")

    return False


def get_files(dir_path: Path, file_ext: str) -> list[str]:
    if not dir_path.is_dir():
        raise ValueError(f"The provided path '{dir_path}' is not a valid directory.")

    file_names = sorted(
        file.name for file in dir_path.glob(f"*{file_ext}") if file.is_file()
    )
    return file_names


# https://code-editor-documentation.streamlit.app/Advanced_usage#custom-buttons
RUN_BUTTON = {
    "name": "Run",
    "feather": "Play",
    "primary": True,
    "hasText": True,
    "showWithIcon": True,
    "commands": ["submit"],
    "alwaysOn": True,
    "style": {"bottom": "0.44rem", "right": "0.4rem"},
}
