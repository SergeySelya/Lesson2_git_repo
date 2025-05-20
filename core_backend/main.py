def hello(name="world"):
    if not isinstance(name, str):
        raise TypeError("Имя должно быть строкой")
    name = name.strip().title()
    return f"Hello, {name}!"