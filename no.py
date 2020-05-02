import array
import string
class pizza:
    Max = 0;
    n = 0;
    def pizzaOrder(Max,n):
        array = [];
        array = n[0];  
        Max = Max
        a = [];
        score = 0;
        i = len(array) - 1;
        y = 0;
        while(i>=0):
            solution = [];
            j = i;
            add= 0;
            while(j>=0):
                temp = array[j];
                if(add+temp < Max):
                    add = add+temp;
                    solution.append(j);
                elif(add+temp == Max):
                    add = add + temp;
                    solution.append(j);
                j = j -1;
            if(score < add):
                score = add;
                a = solution;
                a.reverse();
                
                
            if(len(a) == len(n)):
                test1 = False;
            i = i -1;
        return a;


    def filename(string):
        print("Working");
        f = open(string+".in","r");
        Max, n = [int(x) for x in next(f).split()];
        Input = [];
        if(f.mode == "r"):
            for line in f:
                Input.append([int(x) for x in line.split()])
            print(Input);
            f.close();
        else:
            print("something went wrong");
        return Max,Input;

    def fileOutput(array,string):
        f = open(string+".out","w+");
        #f.write('{}'.formate(len(array)))
        f.write(str(len(array)) + '\n');
        for x in array:
            f.write(str(x) + " ");

        #f.write(str(array))
        f.close();
   
        
string = ["a_example","b_small","c_medium","d_quite_big","e_also_big"]
for x in string:
    r1,r2 = pizza.filename(x);
    print(r1,r2)
    p = pizza.pizzaOrder(r1,r2);
    print(p)
    pizza.fileOutput(p,x)
    



