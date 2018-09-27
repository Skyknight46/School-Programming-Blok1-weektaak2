#!usr/bin/env/python3

#1 Bug collector
def opdracht1():
    
    def main():
        global bug
        bug = []
        global dag
        dag = 1
        tellen (bug, dag)
    def tellen(bug, dag):
        
        for i in range(5):
            bug += [int(input("Geef het aantal bugs gevonden op dag " + str(dag) + " "))]
            dag += 1
            
    main()
    print("Het totaal aantal verzamelde bugs is:",sum(bug))

#3 Lap times
def opdracht3():
    totallaptimes = []
    for n in range(int(input("Geef het aantal rondes die gerend zijn: "))):
        laptimes = int(input("Geef de tijd voor ronde " + str(n+1)+ " in minuten "))
        totallaptimes.append(laptimes)
    print(sum(totallaptimes))
    print("Het snelste rondje was",min(totallaptimes), "minuten")
    print("Het langzaamste rondje was", max(totallaptimes), "minuten")
    print("De gemiddelde rondetijd is: ", round(sum(totallaptimes)/len(totallaptimes), 2), "minuten")


#12 Calculating the factorial of a Number

def opdracht12():
    nummer = int(input("Geef een nummer waarvan je de faculteit wilt weten\n"))
    factorial = 1
    times = 1
    for t in range(nummer):
        factorial = (factorial * times)
        times +=1
        print(factorial)
    
opdracht1()
opdracht3()
opdracht12()
