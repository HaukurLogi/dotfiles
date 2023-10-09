#!/usr/bin/env python3
import subprocess
from subprocess import PIPE, DEVNULL
import re

class radeontop:
    def __init__(self):
        Komi = subprocess.Popen(["radeontop", "-l", "1", "-d", "-"], stdout=PIPE, stderr=DEVNULL)
        output = Komi.communicate()[0].decode('utf-8')  # Komi can communicate?
        output = output.split("\n")[1]
        self.output = output.split(",")

    def join_tuple_string(self, strings_tuple) -> str:
        return ' '.join(strings_tuple).strip()

    def get_usage(self, field):
        for x in self.output:
            if field in x:
                results = re.findall(r'(\d+.\d+)(mb|ghz)?', x)
                return list(map(self.join_tuple_string, results))

    def get_multiple_usages(self, fields: []):
        result = {}
        for x in fields:
            result[x] = self.get_usage(x)

        return result


if __name__ == "__main__":
    rtop = radeontop()
    radeontop_fields = ["gpu"]
    result = rtop.get_multiple_usages(radeontop_fields)
    format_string = f"{int(round(float(result['gpu'][0]), 0))}%"
    print(format_string)

