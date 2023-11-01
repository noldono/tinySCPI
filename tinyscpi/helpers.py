def find_key_by_value(dictionary, target_value):
    for key, value in dictionary.items():
        if value == target_value:
            return key
    return None


def replace_src_dst(command, args):
    new_cmd = command
    new_cmd = new_cmd.replace("[src]", str(args[0]))
    if "[dst]" in new_cmd:
        new_cmd = new_cmd.replace("[dst]", str(args[1]))

    return new_cmd


def shorten_frequency(freq):
    if 1000 <= freq < 1000000:
        updated = round(freq / 1000, 3)
        return f"{updated}k"
    if 1000000 <= freq < 1000000000:
        updated = round(freq / 1000000, 3)
        return f"{updated}M"
    return str(freq)
