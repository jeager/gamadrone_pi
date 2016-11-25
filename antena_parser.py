def get_num_antena_1(line):
    return line[11:13]

def get_num_antena_2(line):
    return line[25:27]

def get_num_antena_3(line):
    return line[39:41]

def parse_antena_1():
    i = 10
    for x in range(0, 11):
        with open("antena_1_medicoes/antena_1_" + str(i) + "m.txt", "r+") as f:
            fo = open("antena_1_medicoes/antena_1_" + str(i) + "_parsed.txt", "wb") 
            for line in f:
                if 'antena_1' in line:
                    fo.write(str(get_num_antena_1(line)))
                    fo.write("\n")
        i = i + 5


def parse_antena_2():
    i = 10
    for x in range(0, 11):
        with open("antena_2_medicoes/antena_2_" + str(i) + "m.txt", "r+") as f:
            fo = open("antena_2_medicoes/antena_2_" + str(i) + "_parsed.txt", "wb") 
            for line in f:
                if 'antena_2' in line:
                    fo.write(str(get_num_antena_2(line)))
                    fo.write("\n")
        i = i + 5

def parse_antena_3():
    i = 10
    for x in range(0, 11):
        with open("antena_3_medicoes/antena_3_" + str(i) + "m.txt", "r+") as f:
            fo = open("antena_3_medicoes/antena_3_" + str(i) + "_parsed.txt", "wb") 
            for line in f:
                if 'antena_3' in line:
                    fo.write(str(get_num_antena_3(line)))
                    fo.write("\n")
        i = i + 5

def main():
   parse_antena_3()
        
if __name__ == "__main__": main()
