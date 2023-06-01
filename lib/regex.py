import re

my_pattern = r"([A-Z][,' a-z]+[.]|[A-Z][,' a-z]+[,][ ][a-z]+[?])"
my_regex = re.compile(my_pattern)
