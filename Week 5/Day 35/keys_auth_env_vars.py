import os

env_vars = list(os.environ.keys())
print(env_vars)

hidden_key = os.environ.get("JAVA_HOME")
print(hidden_key)