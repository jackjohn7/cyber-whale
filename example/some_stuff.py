def camel_to_snake_case(msg: str) -> str:
    '''
    Converts camelCase to snake_case. Also supports PascalCase technically
    '''
    out: str = ""
    for (i, c) in enumerate(msg):
        add_dash = c.isupper() and i != 0
        out += ("_" if add_dash else "") + c.lower()
    return out

