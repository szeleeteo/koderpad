# Import standard library modules
from pathlib import Path

# Import third-party library modules
import pandas as pd
import sqlalchemy as sa
import streamlit as st
from code_editor import code_editor

# Import local modules
from utils import get_files

from .settings import SQL_EDITOR_SETTINGS

EXERCISE_DIR = Path(__file__).resolve().parent / "exercises"
SQL_FILE_EXT = ".sql"
DROP_SCHEMA_PUBLIC = "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"

conn = st.connection(name="sql", type="sql", autocommit=True, ttl=3600)
should_hide_tables = False


def hide_tables():
    global should_hide_tables
    should_hide_tables = True


def execute_query(query: str):
    # refresh public schema each time before executing a query
    query = f"{DROP_SCHEMA_PUBLIC}\n\n{query}"

    try:
        with conn.session as session:
            result = session.execute(sa.text(query))
            rows = result.fetchall()
            st.subheader("Output")
            st.dataframe(rows, hide_index=True, use_container_width=True)
    except sa.exc.ResourceClosedError:
        # Handle the case where no rows are returned (e.g., for DDL statements)
        pass
    except Exception as e:
        st.error(f"Error: {type(e)}")


def list_table_names() -> list[str]:
    query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"

    table_names = []
    try:
        with conn.session as session:
            result = session.execute(sa.text(query))
            rows = result.fetchall()
            table_names = [row[0] for row in rows]
    except Exception as e:
        st.error(f"Error fetching tables: {e}")

    return table_names


def show_tables(table_names: list[str]):
    if not table_names:
        return

    tables_tabs = st.tabs(table_names)

    for table_tab, table_name in zip(tables_tabs, table_names):
        with table_tab:
            query = f"SELECT * FROM {table_name};"
            try:
                with conn.session as session:
                    result = session.execute(sa.text(query))
                    rows = result.fetchall()
                    st.dataframe(
                        rows, use_container_width=True, hide_index=True, height=387
                    )
            except Exception as e:
                st.error(f"Error fetching table {table_name}: {e}")


def run():
    with st.sidebar:
        ex_files = get_files(EXERCISE_DIR, SQL_FILE_EXT)
        selected_exercise = st.selectbox(
            label="Load an exercise",
            options=ex_files,
            format_func=lambda x: x.replace(SQL_FILE_EXT, "").title(),
            on_change=hide_tables,
            key="sql_exercise",
        )
        st.caption(
            "Click Run button once after loading a different exercise to populate the table(s)"
            "\n\nCollapse the sidebar for more space for the code editor and the tables"
        )

    query_col, tables_col = st.columns(2)

    with query_col:
        ex_text = (EXERCISE_DIR / selected_exercise).read_text()
        response_dict = code_editor(
            code=ex_text,
            key="sql_editor",
            response_mode="debounce",  # https://discuss.streamlit.io/t/new-component-streamlit-code-editor-a-react-ace-code-editor-customized-to-fit-with-streamlit-with-some-extra-goodies-added-on-top/42868/16
            **SQL_EDITOR_SETTINGS,
        )
        # query_sql is only set after the user clicks the Run button
        query_sql = response_dict["text"].strip()

    global should_hide_tables
    if should_hide_tables:
        should_hide_tables = False
    else:
        execute_query(query_sql)

        with tables_col:
            tables_panel = st.container()
            with tables_panel:
                all_tables = list_table_names()
                show_tables(all_tables)
