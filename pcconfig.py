import pynecone as pc


config = pc.Config(
    app_name="web_pynecon",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
