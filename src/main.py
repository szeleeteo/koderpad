import streamlit as st

st.set_page_config(
    page_title="Koderpad",
    page_icon=":memo:",
    layout="wide",
    initial_sidebar_state="expanded",
)

if "app_password" not in st.session_state:
    st.session_state["app_password"] = ""


def main():
    import utils
    from languages.docker import executor as dockerfile_executor
    from languages.python import executor as python_executor
    from languages.sql import executor as sql_executor

    executor_mapping = {
        "Python": python_executor,
        "SQL": sql_executor,
        "Dockerfile": dockerfile_executor,
    }

    with st.sidebar:
        st.title("Koderpad")

        if not utils.check_password():
            st.stop()

        language = st.selectbox("Select language", executor_mapping.keys())

    executor_mapping[language].run()


if __name__ == "__main__":
    main()
