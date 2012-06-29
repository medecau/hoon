# Install

    pip install worm

# Use

    import worm
    print worm.hash(worm.fread('README.md'))
    # Print the sha1 for this file

# Use notes:

Don't expect backwards compatibility in worm, each version usually breaks everything with the previous. e.g.: function names

worm is for quick development not to be used in other modules.
Be specific with dependency requirements.

# Bugs & Co.

Found bugs or have a new feature that you want to add?

     * [Fork and add changes](https://github.com/medecau/worm/fork)
     * [Fork and write tests that fail](https://github.com/medecau/worm/fork)
     * [Submit an issue in github](https://github.com/medecau/worm/issues)
