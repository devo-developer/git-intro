# Find the Parent from a dictionary
class Search:
    dataList = [
        {'id': 1, 'parent': 0},
        {'id': 2, 'parent': 0},
        {'id': 3, 'parent': 0},
        {'id': 4, 'parent': 1},
        {'id': 5, 'parent': 4},
        {'id': 6, 'parent': 5}
    ]
# function to search parent

    def findParent(self, item):
        for dic in range(len(self.dataList)):
            if self.dataList[dic].get("id") == item:
                print(str(self.dataList[dic].get("id")) +
                      " => "+str(self.dataList[dic].get("parent")))
                self.findParent(self.dataList[dic].get("parent"))


# create object and call the function


def main():
    dat = Search()
    dat.findParent(int(input('Enter Child : ')))


main()
