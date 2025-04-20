# Import third-party library modules
import streamlit as st

# run this before importing local modules
st.set_page_config(
    page_title="Koderpad",
    page_icon=":memo:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Import local modules
import utils
from languages.python import executor as python_executor
from languages.sql import executor as sql_executor

if "app_password" not in st.session_state:
    st.session_state["app_password"] = ""

executor_mapping = {
    "Python": python_executor,
    "SQL": sql_executor,
}


def main():
    with st.sidebar:
        st.title("Koderpad")

        if not utils.check_password():
            st.stop()

        language = st.selectbox("Select language", ["SQL", "Python"])

    executor_mapping[language].run()


if __name__ == "__main__":
    main()
