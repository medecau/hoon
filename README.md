# Install

    pip install hoon

# Use

    import hoon
    print hoon.hash(hoon.fread('README.md'))
    # Print the sha1 for this file

# Use notes:

Don't expect backwards compatibility in hoon, each version usually breaks everything with the previous. e.g.: function names

# Documentation

### hash(s, algorithm=sha1)
Like binhash() except the digest is returned as a string of double
length, containing only hexadecimal digits.

algorithm parameter defaults to sha1.
### opcodes(a, b)
Get a list of tuples describing how to turn a into b.
### prettify(thing, indent=2)
Some humans like it this way
### qmatch(a, b, ratio=1)
Fast test the similarity of two sequences by testing with
real_quick_ratio() first.
### qratio(a, b)
Return an upper bound on ratio() very quickly.
### ratio(a, b)
Return a measure of the sequences' similarity.
### request(url, data)
Makes a simple request. If no data it's a GET else it's a POST.
Returns a string.
### sequence_matcher(a=None, b=None, isjunk=None)
Short for the SequenceMatcher constructor.
isjunk is moved to the right so it's not required
when providing a and b parameters.
### translate(s, old, new)
Translate each character in old to the character
at the same positionin new
### int_bytes(n)
Convert integer numbers to binary data.

# Bugs & Co.

Found bugs or have a new feature that you want to add?

* [Fork and add changes](https://github.com/medecau/hoon/fork)
* [Fork and write tests that fail](https://github.com/medecau/hoon/fork)
* [Submit an issue in github](https://github.com/medecau/hoon/issues)
