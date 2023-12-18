dynamic_code_execution_example = """
user_snippet = input('Please enter in some Python code: ')

secret_key = 'asfasdfasfas'

my_code_snippets = [
    'print("Hello dynamic code execution!")',
    'x = 5',
    'y = 10',
    'print(x + y)',
    user_snippet,
]

for snippet in my_code_snippets:
    exec(snippet)
"""

print(eval('type("Hello")'))