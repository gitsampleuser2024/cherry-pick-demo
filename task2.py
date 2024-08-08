def write_file(filepath, content):
    with open(filepath, 'w') as file:
        file.write(content)
    return "Write successful"
