import requests
from bs4 import BeautifulSoup
import json


class Tags:

    def getTagData(self):
        requestedPage = requests.get("https://stackoverflow.com/questions")
        pageHTML = BeautifulSoup(requestedPage.text, "html.parser")
        tagDiv = pageHTML.select(".js-gps-related-tags")
        tagDict = {}
        languageTags = []
        languageCount = []

        for tag in tagDiv:
            for tagText in tag.select('.post-tag'):
                languageTags.append(tagText.getText())
            for tagCount in tag.select('.item-multiplier-count'):
                languageCount.append(tagCount.getText())

        tagDict = {languageTags[i]: languageCount[i] for i in range(len(languageTags))}

        tagDataInJson = json.dumps(tagDict)

        return tagDataInJson
