try:
    from googlesearch import search
except ImportError:
        print("No Module named 'google' found")

    # to search
query = "scholarships for computer science"

f = open('c:/web_results/results.txt', 'w')
for j in search(query, tld='com', num=5, stop=10, pause=2):
    f.write(j)
    f.write("\n")
f.close()
