import subprocess, shlex, re, io, inflection

def get_cpu_stats():
    result = _parse_stats('lscpu')
    available = _get_cpu_load()
    result['available'] = available
    result['unavailable'] = 100 - available
    return result

def get_mem_stats():
    return _parse_stats('cat /proc/meminfo')

def get_disk_stats():
    df = subprocess.Popen(shlex.split('df -k'), stdout=subprocess.PIPE)
    skip = True
    filesystems = []
    total_size = 0
    total_used = 0
    for line in io.TextIOWrapper(df.stdout, encoding="utf-8"):
        if skip:
            skip = False
            continue

        parts = re.split(r'\s+', line)
        filesystem = {
            'name': parts[0],
            'size': int(parts[1]),
            'used': int(parts[2]),
            'available': int(parts[3]),
            'use_percent': float(parts[4][:-1]),
            'mount': parts[5]
        }
        filesystems.append(filesystem)

        total_size += filesystem['size']
        total_used += filesystem['used']

    result = {
        'size': total_size,
        'used': total_used,
        'available': total_size - total_used,
        'use_percent': (100.0*total_used/total_size),
        'filesystems': filesystems
    }

    return result

def _get_cpu_load():
    top = subprocess.Popen(shlex.split('top -bn2'), stdout=subprocess.PIPE)
    accuracy = 0
    for line in io.TextIOWrapper(top.stdout, encoding="utf-8"):
        if "Cpu(s)" in line:
            accuracy += 1
            if accuracy > 1:
                match = re.findall(r'\d+\.\d+ id', line)[0][:-3]
                return float(match)

    return 0

def _parse_stats(command):
   ps = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
   result = dict()
   for line in io.TextIOWrapper(ps.stdout, encoding="utf-8"):
       parts = [part.strip() for part in line.split(':')]
       parts[1] = re.sub(r'(kB)', '', parts[1])
       try:
           value = float(parts[1])
       except ValueError:
           value = parts[1]
       parts[0] = re.sub(r'\s+', '_', parts[0])
       key = inflection.underscore(parts[0])
       result[key] = value

   return result

