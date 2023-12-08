import textwrap
import warnings
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas

#reportlab guide
#https://www.reportlab.com/docs/reportlab-userguide.pdf
class PDF_Manager:
    def __init__(self,filename,space_under_title=30,space_between_ingreds = 20,space_between_instructs=20,title_size=16,section_size=10,font_size=8,path_to_output="./"):
        if path_to_output =="./":
            #warnings.warn("No path given, will generate pdf in current directory")
            pass
        self.path_to_output=path_to_output

        if(len(filename) > 4):

            if(filename[-4:] != ".pdf"):
                self.filename = filename + ".pdf"

            else:
                self.filename = filename
        else:
            self.filename = filename + ".pdf"


        #making the file
        self.height = 11.69 * inch

        self.width = 8.27* inch
        self.c = canvas.Canvas(self.path_to_output+self.filename)


        self.space_between_ingreds = space_between_ingreds
        self.space_under_title = space_under_title
        self.space_between_instructs = space_between_instructs
        self.title_size = title_size
        self.section_size = section_size
        self.text_size=font_size



    def set_page_header(self,title="TEST MESSAGE",y=50):
        # y = 108  # wherever you want your text to appear
        self.c.setFont("Helvetica-Bold",self.title_size)
        self.c.drawCentredString(self.width / 2.0, self.height - y, title)
        #self.c.setFont("Helvetica",self.section_size)

    def set_recipe_ingreds(self,ingreds,y = 50):
        lowerBy = y + self.space_under_title
        self.c.setFont("Helvetica-Bold", self.section_size)
        self.c.drawCentredString(self.width/2.0,self.height-lowerBy,"Ingredients")
        lowerBy += self.space_between_ingreds
        self.c.setFont("Helvetica", self.text_size)
        for ingred in ingreds:
            self.c.drawCentredString(self.width/2,self.height-lowerBy,ingred)
            lowerBy += self.space_between_ingreds

        self.final_ingred_pxl = lowerBy
        #print(self.final_ingred_pxl)



    def set_recipe_instruct(self,instructList):

        self.final_ingred_pxl += self.space_between_instructs
        self.c.setFont("Helvetica-Bold", self.section_size)
        self.c.drawCentredString(self.width / 2.0, self.height - self.final_ingred_pxl, "Instructions")
        self.final_ingred_pxl += self.space_between_ingreds
        length = 75  # chars per line

        curr_spot = self.final_ingred_pxl

        instructIdx = 1
        self.c.setFont("Helvetica", self.text_size)
        for instruct in instructList:

            wraps = textwrap.wrap(instruct, length)
            for x in range(len(wraps)):
                if (x == 0):
                    self.c.drawCentredString(self.width / 2, self.height - curr_spot,
                                             str(instructIdx) + ") " + wraps[x])
                else:
                    self.c.drawCentredString(self.width / 2, self.height - curr_spot, wraps[x])

                curr_spot += self.space_between_instructs

            curr_spot += self.space_between_instructs
            if (curr_spot > 600):
                self.c.showPage()
                self.c.setFont("Helvetica", self.text_size)
                curr_spot = 50

            instructIdx += 1

    def add_watermark(self):
        #something here to denote where this came from
        pass
    def save(self):
        self.add_watermark()
        self.c.showPage()
        self.c.save()




