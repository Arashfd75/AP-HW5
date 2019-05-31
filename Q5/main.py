import os

class fileManage:
    def __init__(self, name, address):
        self.address = address
        self.name = name

    def create_dir(self):
        os.chdir(self.address)
        dir_list = os.listdir()
        flag = True
        for i in dir_list:
            if i == self.name:
                flag = False
                break
        if flag == True:
            os.mkdir(self.name)
            print("Directory " , self.name ,  " Created ")
        else:    
            print("Directory " , self.name ,  " already exists")

    def create_file(self):
        os.chdir(self.address)
        dir_list = os.listdir()
        flag = True
        for i in dir_list:
            if i == self.name:
                flag = False
                break
        if flag == True:
            os.mknod(os.path.join(self.address,self.name))
            print("File " , self.name ,  " Created ")
        else:    
            print("File " , self.name ,  " already exists")
        
    def delete(self):
        os.chdir(self.address)
        dir_list = os.listdir()
        flag = True
        for i in dir_list:
            if i == self.name:
                flag = False
                break
        if flag == True:
            print("File " , self.name ,  " not exists ")
        else:
            os.remove(os.path.join(self.address,self.name))    
            print("File " , self.name ,  " deleted ")
        
    def find(self):
        result = []
        for root, dirs, files in os.walk(self.address):
            if self.name in files:
                result.append(os.path.join(root, self.name))
        i = 1
        for item in result:
            print(i, ': ', item)
            i = i + 1

def main(): 
    
    while(1):     
        #IN = input("Please Enter My Duty: ")
        IN = input("""Please Enter My Duty \n Enter Q to Quit:  """)
        if IN == 'q' or IN == 'Q' :
            break
        func = IN.split('(')[0]
        pos1 = IN.find('(')
        pos2 = IN.find(',')
        pos3 = IN.find(')')
        name = IN[pos1 + 1 :pos2]
        address = IN[pos2 + 1 :pos3]
        f1 = fileManage(name, address)
        func = str(func)
        if func == 'create_dir':
            f1.create_dir()
        elif func == 'create_file':
            f1.create_file()
        elif func == 'delete':
            f1.delete()
        elif func == 'find':
            f1.find()
    
if __name__ == "__main__":
    main()