# Koderpad
An online Python and SQL database playground for testing codes

## Requirements
1. [uv](https://github.com/astral-sh/uv)
2. make
3. Docker
4. Python3.11

## Local Development
1. Setup environment variables.
    ```sh
    cp -i .streamlit/secrets.toml.example .streamlit/secrets.toml
    ```
- Note that instead of `.env`, we are using `secrets.toml` located in the `.streamlit` directory to store secrets for this project.
- Uncomment and set a value for `APP_PWD` in `.streamlit/secrets.toml` to test for password checking, otherwise leave
- The default value for `DATABASE_URL` in `.streamlit/secrets.toml` should match the `make db` in `Makefile`. Update if required to point to other database url.

2. Run database and app
    ```sh
    $ make db  # run a Postgres db container in the background based on DATABASE_URL in .env
    $ make run # run the Streamlit app
    ```

## Warning
Do not host app this online without password protection as the system environment variables are easily exposed via Python os module.
