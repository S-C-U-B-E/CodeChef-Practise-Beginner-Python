n =  int(input()) #JOTO GULO PLACE OBDHI ARRAY BHORBI

result_array=[]   #ARRAY INITIALIZE

FIBO_0TH=0
FIBO_1ST=1

PRIME_SURU=1       # JODIO EKHANE 1 ACHE.. WHILE LOOP E DHUKE AAGE +1 HOBE
                   # THEN 2 THEKE 1ST CHECK SURU

for i in range(n): #LOOP BEGINS
    if i%2==0:
        if i == 0:
            result_array.append(FIBO_0TH)       # PROTHOM 2 BAR KONO CALCULATION NEI.
        elif i == 2:
            result_array.append(FIBO_1ST)
        else:
            result_array.append(result_array[i-2]+result_array[i-4])  # PREVIOUS DUTO EVEN PLACE -2 AND -4TH
                                                                      # POSITION E THAKBE

        print("FIBO:i="+str(i)+"  VALUE:"+str(result_array[-1]))    #EI KETH WALA PRINT TA IGNORE MAAR

    else:
        prime_noe = 0          # DHORENILAM NUMBER TA PRIME

        while True:

            PRIME_SURU += 1                # EKBAR PRIME NO. NA PAWA OBDHI ETA BARTE THAKBE

            for j in range(2,PRIME_SURU):  # NORMAL PRIME NO. CHECK KORCHI (2 THEKE SURU KORE .. NUMBER_TA-1 OBDHI CHOLBE)
                if PRIME_SURU%j == 0:      # JODI ONNO KONO NO. DIYE DIVIDE HOE JAE
                    prime_noe = 1          # THEN OTA SOTTI E PRIME NOE
                    break
            if  prime_noe:
                prime_noe = 0               #PRIME NA HOLE.. EI VARIABLE TA ABAR 0
            else:
                result_array.append(PRIME_SURU) # PEYE GELE .... ARRAY TE DHOKABE
                break                           # INFINITE LOOP SESH


            #CAUTION :  TCS E BHUL INFINTE LOOP CHOLLE PROBLEM HOBE ... MONE ACHE TOH ????????

        print("PRIME:i=" + str(i) + "  VALUE:" + str(result_array[-1]))  # EI KETH WALA PRINT TA IGNORE MAAR

print(result_array)

#ANY PROBLEM DEER <3 ?.. FEEL FREE TO CALL ME AT 7908653345.