class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        sen=sentence.split()
        dictionary.sort(key=len)
        for i in range(len(dictionary)):
            for j in range(len(sen)):
                if sen[j].startswith(dictionary[i]):
                    sen[j]=dictionary[i]
        return " ".join(sen)