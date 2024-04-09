# Red-Black Tree REPL:

The REPL offers functionality for inserting, deleting, and searching within a 
red-black tree, along with the capability to generate an ASCII, or a graphical, 
representation of the tree structure in real-time.

## Building:

After cloning this repository, install all the requirements in `requirements.txt`:

```shell
pip install -r requirements.txt
```
And run:

```shell
python3 main.py
```

To run the tests:

```shell
python3 -m pytest tests/*.py
```

## Acknowledgements:

The tree implementation was taken from [Red-black tree implementation in
Python](https://github.com/emilydolson/python-red-black-trees?tab=License-1-ov-file)
, and the plotting code was taken from [Implementation and
Visualization of Red/Black Trees](https://github.com/cehrett/Left-leaning_red_black_trees).
