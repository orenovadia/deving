# Deving

Some development tools

# Install

``` pip install --user -e git+https://github.com/orenovadia/deving.git@master#egg=deving ```

# Tools

## Python Tracebacks

Aggregates tracebacks from a python log file. Usage: `dev-tracebacks logfile.log`

## Plot word histogram

```history | awk '{print $2}' | dev-histogram ```

## URL Parameter encoding

```seq 4 | dev-urlencode - http://localhost:5000 param```

