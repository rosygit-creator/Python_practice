def compare_ver(version):
    with open('version.txt', 'r') as f:
        expected_version=f.read()
        if version > float(expected_version):
            return True
        else:
            return False



ans=compare_ver(15)
assert ans, True