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
