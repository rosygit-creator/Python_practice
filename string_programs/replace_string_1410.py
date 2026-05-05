
#  https://leetcode.com/problems/html-entity-parser/description/

def countchar(input):
    d = {
    '&quot;': '"',
    '&apos;': "'",
    '&amp;': "&",
    "&gt;": '>',
    "&lt;": '<',
    "&frasl;": '/',
    }

    for k, v in d.items():
        if k in input:
            input=input.replace(k, v)
            # print(input)
    return input

# ans=countchar("and I quote: &quot;...&quot;")
ans=countchar("x &gt; y &amp;&amp; x &lt; y is always false")
print(ans)