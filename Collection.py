import warnings
#Add support for
#Serious Eats

#spruce eats
#taste of home
#food netword
#NYT (may need subscript)
#tastesbetterforomscratch
class Collection:
    def __init__(self,sess):
        self.session=sess

    def info(self):
        pass
        #print("Welcome to ")

    def genericSearch(self,link):
        #in this check if link contains alexanderiacooks, allrecipes, etc
        if "alexandracooks" in link:
            retVal =  self.alexandraCooks(link)
        elif "allrecipes" in link:
            retVal = self.allrecipes(link)
        elif "delish" in link:
            #recomend not using
            retVal = self.delish(link)
        elif "marleysmenu" in link:
            retVal = self.marleysmenu(link)

        retVal["link"] = link
        return retVal

    def marleysmenu(self,link):
        page = self.session.get(link)
        title = page.html.find(".elementor-heading-title")[0].text
        ingreds = page.html.find(".wprm-recipe-ingredients")
        instruct = page.html.find(".wprm-recipe-instructions")
        data = {"ingreds": ingreds[0].text, "instruct": instruct[0].text}  # this data is not clean
        #print(data)
        cleaned = self.cleanData("marleysmenu",data)
        cleaned["title"] = title
        return cleaned


    def alexandraCooks(self, link):
        page = self.session.get(link)
        title = page.html.find(".post-title")[0].text
        #print(title)
        ingreds = page.html.find(".tasty-recipes-ingredients")
        # print(ingreds[0].text)
        instruct = page.html.find(".tasty-recipes-instructions")
        # print(instruct[0].text)
        data = {"ingreds": ingreds[0].text, "instruct": instruct[0].text}  # this data is not clean
        #return data
        cleaned = self.cleanData('alexandracooks',data)
        cleaned["title"] = title

        return cleaned

    def allrecipes(self, link):
        page = self.session.get(link)
        title = page.html.find("#article-heading_1-0")[0].text

        ingreds = page.html.find("#mntl-structured-ingredients_1-0")
        # print(ingreds[0].text)
        instruct = page.html.find("#recipe__steps_1-0")
        data = {"ingreds": ingreds[0].text, "instruct": instruct[0].text}
        cleaned = self.cleanData("allrecipes",data)
        cleaned["title"] = title
        return cleaned
        #return {"ingreds": ingreds[0].text, "instruct": instruct[0].text}  # this data is not clean







    def delish(self, link):
        #as of Nov 11 2023 this can pass the paywall
        #support for delish is really bad
        warnings.warn("Warning! Support for delish is very poor. There is a high likelyhood this fails")
        page = self.session.get(link)
        title = page.html.find(".css-2l10x9")[0].text
        ingreds = page.html.find(".ingredient-lists")
        #print(ingreds[0].text)

        instruct = page.html.find(".directions")
        #print(instruct[0].text)

        data = {"ingreds": ingreds[0].text, "instruct": instruct[0].text}  # this data is not clean and looks different than the others, especially the ingreds
        cleaned = self.cleanData("delish",data)
        cleaned["title"] = title
        return cleaned

    def tastesbetterfromscratch(self,link):
        pass

    def cleanData(self,target,data):
        retVal = {}
        if target == 'alexandracooks':

            ingredsList = data["ingreds"].split("\n")
            for elem in ingredsList:
                if elem == 'Ingredients' or elem == 'Cook Mode Prevent your screen from going dark':
                    ingredsList.remove(elem)

            instructList = data['instruct'].split('\n')
            if instructList[0] == 'Instructions':
                instructList.remove('Instructions')



        elif target == 'allrecipes':

            ingredsList = data["ingreds"].split("\n")
            #print(ingredsList)
            instructList = data["instruct"].split("\n")


            for elem in ingredsList:
                if elem == "Ingredients":
                    ingredsList.remove(elem)

            for elem in instructList:
                if elem == "Directions" or elem == "Dotdash Meredith Food Studios" or elem =="DOTDASH MEREDITH FOOD STUDIOS":
                    instructList.remove(elem)

        elif target == "delish":
            #print("Getting here")
            ingredsList =  data["ingreds"].split("\n")
            instructList = data["instruct"].split("\n")
            #instructList.remove(0)
            #instructList.remove(1)
            for elem in ingredsList:
                if ".css" in elem:
                    ingredsList.remove(elem)

            for elem in instructList:
                #print(elem)
                if "css" in str(elem) or "Step" in elem:
                    #print("CSS IN")
                    instructList.remove(elem)

            #print(instructList)

        elif target == "marleysmenu":
            ingredsList = data["ingreds"].split("\n▢")
            instructList = data["instruct"].split("\n")





        retVal["ingredList"] = ingredsList
        retVal["instructlist"] = instructList

        return retVal
