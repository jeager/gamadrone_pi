#coding=utf8

def get_num_antena_1(line):
    """
    Descrição:
    Função que retorna apenas os números
    referentes às medições da antena 1 
    nas strings apresentadas. 
    Parâmetro:
    line - linhas dos arquivos txt.
    """
    return line[11:13]

def get_num_antena_2(line):
    """
    Descrição:
    Função que retorna apenas os números
    referentes às medições da antena 2 
    nas strings apresentadas. 
    Parâmetro:
    line - linhas dos arquivos txt.
    """
    return line[25:27]

def get_num_antena_3(line):
    """
    Descrição:
    Função que retorna apenas os números
    referentes às medições da antena 3 
    nas strings apresentadas. 
    Parâmetro:
    line - linhas dos arquivos txt.
    """
    return line[39:41]

def parse_antena_1():
    """
    Descrição:
    Função que abre os arquivos txt da antena 1 e 
    sobrescreve o mesmo arquivo apenas com os números 
    das medições utilizando o método get_num_antena_1().
    """
    i = 10
    for x in range(0, 11):
        with open("antena1/antena_1_" + str(i) + "m.txt", "r+") as f:
            fo = open("antena1/antena_1_" + str(i) + "_parsed.txt", "wb") 
            for line in f:
                if 'antena_1' in line:
                    fo.write(str(get_num_antena_1(line)))
                    fo.write("\n")
        i = i + 5


def parse_antena_2():
    """
    Descrição:
    Função que abre os arquivos txt da antena 2 e 
    sobrescreve o mesmo arquivo apenas com os números 
    das medições utilizando o método get_num_antena_2().
    """
    i = 10
    for x in range(0, 11):
        with open("antena2/antena_2_" + str(i) + "m.txt", "r+") as f:
            fo = open("antena2/antena_2_" + str(i) + "_parsed.txt", "wb") 
            for line in f:
                if 'antena_2' in line:
                    fo.write(str(get_num_antena_2(line)))
                    fo.write("\n")
        i = i + 5

def parse_antena_3():
    """
    Descrição:
    Função que abre os arquivos txt da antena 3 e 
    sobrescreve o mesmo arquivo apenas com os números 
    das medições utilizando o método get_num_antena_3().
    """
    i = 10
    for x in range(0, 11):
        with open("antena3/antena_3_" + str(i) + "m.txt", "r+") as f:
            fo = open("antena3/antena_3_" + str(i) + "_parsed.txt", "wb") 
            for line in f:
                if 'antena_3' in line:
                    fo.write(str(get_num_antena_3(line)))
                    fo.write("\n")
        i = i + 5

def main():
    parse_antena_1()
    parse_antena_2()
    parse_antena_3()
        
if __name__ == "__main__": main()
