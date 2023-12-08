
from Collection import Collection
from PDF_Manager import PDF_Manager
from requests_html import HTMLSession
import sys


link = sys.argv[1]


session = HTMLSession()
col = Collection(session)
recipe_clean = col.genericSearch(link)


#PDF STUFF
path = "./output_dir/"
fileName= recipe_clean["title"].replace(" ", "")
pdf = PDF_Manager(fileName,path_to_output=path)
pdf.set_page_header(recipe_clean["title"])
pdf.set_recipe_ingreds(recipe_clean["ingredList"])
pdf.set_recipe_instruct(recipe_clean["instructlist"])
pdf.save()
print(fileName)