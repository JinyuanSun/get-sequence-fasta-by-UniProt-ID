import argparse
import urllib.request
parser = argparse.ArgumentParser(description='a code to write a fasta by a given list')
parser.add_argument("-i", '--input', help="input a list file")
parser.add_argument("-o", '--output', help="output file name")
args = parser.parse_args()

inf = args.input
ouf = args.output

ofile = open(ouf, "w")

with open(inf) as f:
    data = f.read().splitlines()
    for i in range(len(data)):
        urls = "http://www.uniprot.org/uniprot/" + data[i] + ".fasta"
        import urllib.request
        response = urllib.request.urlopen(urls).read()
        html = response.decode('utf-8')
        ofile.write(html)
ofile.close()

