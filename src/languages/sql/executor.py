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


@st.cache_resource
def get_engine() -> sa.Engine:
    engine_url = st.secrets["DATABASE_URL"]
    return sa.create_engine(engine_url)


engine = get_engine()


def execute_query(query: str):
    # refresh public schema each time before executing a query
    query = f"{DROP_SCHEMA_PUBLIC}\n\n{query}"

    try:
        with engine.begin() as conn:
            result = conn.execute(sa.text(query))

            if result.returns_rows:
                df = pd.DataFrame(result.fetchall(), columns=list(result.keys()))
                st.dataframe(df, hide_index=True, use_container_width=True)
            else:
                st.success("Query executed successfully!")

    except Exception as e:
        st.error(f"Error: {e}")


def list_table_names() -> list[str]:
    query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"

    try:
        with engine.begin() as conn:
            result = conn.execute(sa.text(query))
            return [row[0] for row in result.fetchall()]
    except Exception as e:
        st.error(f"Error fetching tables: {e}")
        return []


def show_tables(table_names: list[str]):
    if not table_names:
        return

    tables_tabs = st.tabs(table_names)

    for table_tab, table_name in zip(tables_tabs, table_names):
        with table_tab:
            query = f"SELECT * FROM {table_name};"
            try:
                with engine.begin() as conn:
                    df = pd.read_sql_query(query, con=conn)
                st.dataframe(df, use_container_width=True, hide_index=True, height=213)
            except Exception as e:
                st.error(f"Error fetching table {table_name}: {e}")


def run():
    with st.sidebar:
        ex_files = get_files(EXERCISE_DIR, SQL_FILE_EXT)
        selected_exercise = st.selectbox(
            label="Load an exercise",
            options=ex_files,
            format_func=lambda x: x.replace(SQL_FILE_EXT, "").title(),
            key="sql_exercise",
        )
        show_all_tables = st.toggle("Show all tables in the database", False)

    tables_panel = st.container()

    ex_text = (EXERCISE_DIR / selected_exercise).read_text()
    response_dict = code_editor(code=ex_text, key="sql_editor", **SQL_EDITOR_SETTINGS)

    query_sql = response_dict["text"].strip()

    if query_sql:
        st.write("Results")
        execute_query(query_sql)

    if show_all_tables:
        with tables_panel:
            all_tables = list_table_names()
            show_tables(all_tables)
            if all_tables:
                st.caption("All tables in the database")
