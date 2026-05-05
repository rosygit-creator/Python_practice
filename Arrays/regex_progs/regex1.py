# numbers from string
import re
input="saturday 12, 231"
# finall finds all matches
ans=re.findall(r"(\d{2})", input)
print(ans)

ans=re.findall(r"\d+", input)
print(ans)

input1="saturdeay 2024-22-22"
ans=re.findall(r"(\d{4})-(\d{2})-(\d{2})", input1)
print(ans)

input2="2024-22-22 1"
pattern = r'(?P<date>\d{4}-\d{2}-\d{2}) (?P<other>.*)'
match = re.match(pattern, input2)

result = match.groupdict()
print(result["date"])
print(result["other"])