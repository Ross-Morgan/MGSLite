import re


patterns = {
    "variable": re.compile(r"(\w+)(?= =)"),
    "inline_variables": re.compile(r"(?<=[^\\]\$)\w+"),
    "function": re.compile(r"\w+(?= ::)"),
    "function_args": re.compile(r"(?<= :: \[)(.+)(?=\])")
}
