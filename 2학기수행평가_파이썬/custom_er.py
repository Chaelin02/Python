import pickle

class Customer():
    def __init__(self, coustom_er):
        self.coustom_er = coustom_er


    def save(self, data):
        with open(self.filename, "wb") as f:
            pickle.dump(data, f)


    def load(self):      #load한 다음에 그 데이터를 내보내줘야 하니까 return 씀
         try:
            with open(self.filename, "rb") as f:
                data = pickle.load(f)
         except FileNotFoundError:
             raise FileNotFoundError
         return data