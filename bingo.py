import sys
import random

word_file = sys.argv[1]
num_cards = int(sys.argv[2])

sys.stderr.write("File=" + word_file + "\tN=" + str(num_cards) + "\n")
f = open(word_file, "r")
words = f.readlines()
words = [w.strip() for w in words]
if len(words) < 24:
    sys.stderr.write("Error: Word file to short :D " + str(len(words)) + " words.\n")
    sys.exit()

print ("<html><head><title>Bingo Cards</title></head>")
print ("<body>")

i = 0
while i < num_cards:
    card = []
    j = 0
    for j in range(0, 24):
        n = random.randint(0, len(words) - 1)
        while n in card:
            n = random.randint(0, len(words) - 1)
        card.append(n)
    card = [words[n] for n in card]
    card.insert(12, "<b>BINGO</b>")
    i += 1
    
    if (1 == (i % 2)) and (i > 1):
        print ("<h3 align=\"center\" style=\"page-break-before: always\">",)
    else:
        print ("<h3 align=\"center\">",)
    print ("NeverW8<br>Bingo</h3>")
    print ("<table border=\"1\" cellpadding=\"5\" align=\"center\">")
    for r in range(0, 5):
        print ("<tr>")
        for c in range(0, 5):
            print ("<td align=\"center\" width=\"100\">" + card[(r * 5) + c] + "</td>")
        print ("</tr>")
    print ("</table>")
    print ("<p align=\"center\"><b>This is a comment:</b> Something</p>")
    if 1 == (i % 2):
        print ("</body></html>")
