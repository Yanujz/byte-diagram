#! /usr/bin/env python3
import argparse
from argparse import RawTextHelpFormatter

__author__ = u"Yanujz"
__copyright__ = "Copyright 2024"
__credits__ = ["Yanujz"]
__version__ = "0.1.0"
__mantainers__ = ["Yanujz"]
__email__ = "yanujz@live.it"
__license__ = """
Copyright 2024 Yanujz

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""



s = "{:<20}{}\n{:<20}{}\n{:<20}{}\n{:<20}{}\n".format("Author:",
                                                      __author__,
                                                      "Maintainer(s):",
                                                      " ".join(__mantainers__),
                                                      "Email:",
                                                      __email__,
                                                      "Credits:",
                                                      " ".join(__credits__)
                                                      )

version = "{} {}\n{}\n{}\n{}".format('%(prog)s', __version__, __copyright__, s, __license__)



def generate_lines(hex_string, desc):
    size = len(hex_string)
    arrowLen = (4 * size) + (size - 1)
    
    arrowDecreseLen = 5
    if 2 != arrowLen % arrowDecreseLen:
        arrowLen -= arrowDecreseLen
        while 1:
            arrowLen += 1
            if 2 == arrowLen % arrowDecreseLen:
                break
    
    arrow_lines = []
    
    leftStr = "   "
    for i in range(size + 1):
        arrow_line = leftStr 
        if i != size:
            arrow_line +=  "-" * (arrowLen) +"> "
            if (desc is not None) and (i < len(desc)):
                arrow_line += desc[i]
        if 0 == i:
            leftStr = " "  + " /     "
        else:
            leftStr = " |   " + leftStr

        arrowLen -= arrowDecreseLen

        arrow_lines.append(arrow_line)
    
    # Print the arrow lines
    for line in arrow_lines:
        print(line)
        
    # Print the byte sequence line
    print(" |   " * size + "     ")
    
    for b in hex_string:
        print("0x{:02X} ".format(b), end="")
    print("")


def get_parser():
    parser = argparse.ArgumentParser(
        description="Create an ASCII art diagram to explain bytes.",
        formatter_class=RawTextHelpFormatter
    )
    
    parser.add_argument(
        "-s", "--str", type=str, required=True, help="Input string"
    )
    
    parser.add_argument(
        "-d", "--desc", metavar='N', type=str, nargs='+', help="Sequential description per field"
        )
    
    parser.add_argument(
        "--version", 
        action="version", 
        version=version,
        help="Show program's version number and exit"
    )
    
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()
    payload = bytearray.fromhex(args.str)
    
    desc = []
    for d in args.desc:
        desc.append(d.strip())
        
    generate_lines(payload, desc)

if __name__ == '__main__':
    main()
    