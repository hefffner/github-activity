def parse_env(filepath=".env"):
    env_vars = {}

    with open (filepath, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            
            if not line or line.startswith('#'):
                continue

            if '=' not in line:
                continue

            key, value = line.split('=', 1)

            key = key.strip()
            value = value.strip()

            if (value.startswith('"') and value.endswith('"') or \
                (value.startswith("'")) or value.endswith("'")): value = value[1:-1]
            
            env_vars[key] = value

    return env_vars