# Think of additional classes, attributes, 
# or methods we could use to improve our 
# streaming service. Consider some of the 
# principles we discussed today. Fall down the rabbit 
# hole that is APIs and pull back some tasty information. 
# You can complete this at the bottom of today's 
# lecture or in your code editor of choice.


#pip install request
class tv_maze():
    def __init__(self, name, quality, region):
        self.name = name
        self.region = region
        self.quality = quality

class Tv_update():
    def tv_Install(self,):
        r = request.get(f"https://api.tvmaze.com/{self.name.lower()}")
