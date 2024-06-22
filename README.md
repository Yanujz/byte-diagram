# byte-diagram
`byte-diagram` is a command-line tool designed to create visual representations of byte sequences. It generates ASCII art diagrams that illustrate byte positions and their hexadecimal values in a sequential manner.

## Usage
```
usage: byte-diagram.py [-h] -s STR [-d N [N ...]] [--version]

Create an ASCII art diagram to explain bytes.

options:
  -h, --help            show this help message and exit
  -s STR, --str STR     Input string
  -d N [N ...], --desc N [N ...]
                        Sequential description per field
  --version             Show program's version number and exit
```


## Features
- **Visual Representation**: Draws lines ASCII characters from each byte in order to explain the meaning of it.
- **Flexible Input length**: Accepts hexadecimal strings as input, allowing users to visualize various byte sequences.
- **Description**: Supports optional sequential descriptions for each byte field.


## Examples
```sh
./byte-diagram.py -s "00 01 02"
   ------------> 
  /     -------> 
 |     /     --> 
 |    |     /     
 |    |    |        
0x00 0x01 0x02 
```

```sh
./byte-diagram.py -s "00 01 02" -d "Field 0" "Field 1" "Field 2"
   ------------> Field 0
  /     -------> Field 1
 |     /     --> Field 2
 |    |     /     
 |    |    |        
0x00 0x01 0x02 
```