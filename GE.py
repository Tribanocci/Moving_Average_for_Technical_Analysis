import pandas as pd
import matplotlib.pyplot as plt



def MA_policy(A_kefalaio, B, wait, reverse, N):
    
    stock=0
    df = pd.read_csv("GE.csv")

    #df1 = pd.read_csv("MSSH.csv", header=None)
    data = df['Close'].head(N)
    df2= pd.DataFrame(data)
    if (reverse):
        df2.loc[:]=df2.iloc[::-1].values


    df2['KMO10']=df2.rolling(window=10).mean()
    df2['KMO20']=df2['Close'].rolling(window=20).mean()
    df2['KMO40']=df2['Close'].rolling(window=40).mean()
    #df2['EWM0.5']=df2['Close'].ewm(com=0.2).mean()

    df2.plot()
    plt.show()

    kefalaio = A_kefalaio
    df2.loc[(df2['Close'] <= df2['KMO10']) | (df2['KMO10'].isnull()), 'larger_than_KMO10?'] = 0
    df2.loc[df2['Close'] > df2['KMO10'], 'larger_than_KMO10?'] =  1
    df2.loc[0, 'shares10'] = kefalaio
    i=1
    while i<len(df2)-wait:
        df2.loc[i, 'shares10'] = kefalaio
        if ((df2.loc[i, 'larger_than_KMO10?'] > df2.loc[i-1, 'larger_than_KMO10?']) and (df2.loc[i:i+wait, 'larger_than_KMO10?'].mean() == 1)):
            df2.loc[i : i+wait, 'shares10'] = kefalaio
            i=i+wait
            stock = stock + (B*kefalaio)/df2.loc[i, 'Close']
            kefalaio=kefalaio*(1-B)
            print("to kefalaio einai  :", kefalaio, "    oi metoxes einai   :", stock)
        elif (df2.loc[i, 'larger_than_KMO10?'] < df2.loc[i-1, 'larger_than_KMO10?'] and (df2.loc[i:i+wait, 'larger_than_KMO10?'].mean() == 0) ):
            df2.loc[i : i+wait, 'shares10'] = kefalaio
            i=i+wait 
            kefalaio=kefalaio+ df2['Close'][i]*stock
            stock = 0
            print("to kefalaio einai  :", kefalaio, "    oi metoxes einai   :", stock)  
        else:
            i=i+1

    kefalaio=kefalaio+df2['Close'][len(df2)-1-wait]*stock
    df2.loc[i : i+wait, 'shares10'] = kefalaio
    print("bgalame kerdiiiiii           ",kefalaio)


    kefalaio = A_kefalaio
    df2.loc[(df2['Close'] <= df2['KMO20']) | (df2['KMO20'].isnull()), 'larger_than_KMO20?'] = 0 
    df2.loc[df2['Close'] > df2['KMO20'], 'larger_than_KMO20?'] = 1 
    df2.loc[0, 'shares20'] = kefalaio
    i=1
    while i<len(df2)-wait:
        df2.loc[i, 'shares20'] = kefalaio
        if ((df2.loc[i, 'larger_than_KMO20?'] > df2.loc[i-1, 'larger_than_KMO20?']) and (df2.loc[i:i+wait, 'larger_than_KMO20?'].mean() == 1)):
            df2.loc[i : i+wait, 'shares20'] = kefalaio
            i=i+wait
            stock = stock + (B*kefalaio)/df2.loc[i, 'Close']
            kefalaio=kefalaio*(1-B)
            print("to kefalaio einai  :", kefalaio, "    oi metoxes einai   :", stock)
        elif (df2.loc[i, 'larger_than_KMO20?'] < df2.loc[i-1, 'larger_than_KMO20?'] and (df2.loc[i:i+wait, 'larger_than_KMO20?'].mean() == 0) ):
            df2.loc[i : i+wait, 'shares20'] = kefalaio
            i=i+wait 
            kefalaio=kefalaio+ df2['Close'][i]*stock
            stock = 0
            print("to kefalaio einai  :", kefalaio, "    oi metoxes einai   :", stock)  
        else:
            i=i+1


    kefalaio=kefalaio+df2['Close'][len(df2)-1-wait]*stock
    df2.loc[i : i+wait, 'shares20'] = kefalaio
    print("bgalame kerdiiiiii           ",kefalaio)



    kefalaio = A_kefalaio
    df2.loc[(df2['Close'] <= df2['KMO40']) | (df2['KMO40'].isnull()), 'larger_than_KMO40?'] = 0 
    df2.loc[df2['Close'] > df2['KMO40'], 'larger_than_KMO40?'] = 1
    df2.loc[0, 'shares40'] = kefalaio
    i=1
    while i<len(df2)-wait:
        df2.loc[i, 'shares40'] = kefalaio
        if ((df2.loc[i, 'larger_than_KMO40?'] > df2.loc[i-1, 'larger_than_KMO40?']) and (df2.loc[i:i+wait, 'larger_than_KMO40?'].mean() == 1)):
            df2.loc[i : i+wait, 'shares40'] = kefalaio
            i=i+wait
            stock = stock + (B*kefalaio)/df2.loc[i, 'Close']
            kefalaio=kefalaio*(1-B)
            print("to kefalaio einai  :", kefalaio, "    oi metoxes einai   :", stock)
        elif (df2.loc[i, 'larger_than_KMO40?'] < df2.loc[i-1, 'larger_than_KMO40?'] and (df2.loc[i:i+wait, 'larger_than_KMO40?'].mean() == 0) ):
            df2.loc[i : i+wait, 'shares40'] = kefalaio
            i=i+wait 
            kefalaio=kefalaio+ df2['Close'][i]*stock
            stock = 0
            print("to kefalaio einai  :", kefalaio, "    oi metoxes einai   :", stock)  
        else:
            i=i+1


    kefalaio=kefalaio+df2['Close'][len(df2)-1-wait]*stock
    df2.loc[i : i+wait, 'shares40'] = kefalaio
    print("bgalame kerdiiiiii           ",kefalaio)

    results = df2[ ['shares10', 'shares20', 'shares40'] ]
    results.plot()
    plt.show()



kefalaio=1000
B=0.6
C=0.05
N=400
wait=10
MA_policy(kefalaio,B,wait,1,N)