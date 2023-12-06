import pandas as pd
import matplotlib.pyplot as plt



def csv_to_df(filename, reverse):
    df = pd.read_csv(filename)
    #data = df['Close'].head(300)
    #date = df['Date'].head(300)
    #df2= pd.DataFrame(data, index=date)
    if (reverse):
        df.loc[:]=df.iloc[::-1].values
    return df
    



def MA_policy(A_kefalaio, B, wait, reverse, N,k,filepath):
    
    stock=0
    df = pd.read_csv(filepath)

    #df1 = pd.read_csv("MSSH.csv", header=None)
    if N == 0:
        N=len(df)
    data = df[['Date', 'Close']].head(N)
    df2= pd.DataFrame(data)
    if (reverse):
        df2.loc[:]=df2.iloc[::-1].values
    print(len(df2))
    #-----TITLES of columns (variable_name)---------------------
    share_1 = 'MA = ' + str(k)
    share_2 = 'MA = ' + str(2*k)
    share_3 = 'MA = ' + str(3*k)
    #---------
    share_1_ma = 'MA = ' + str(k)
    share_2_ma = 'MA = ' + str(2*k)
    share_3_ma = 'MA = ' + str(3*k)
    #===============================================================    

    df2[share_1_ma]=df2['Close'].rolling(window=k).mean()
    df2[share_2_ma]=df2['Close'].rolling(window=2*k).mean()
    df2[share_3_ma]=df2['Close'].rolling(window=3*k).mean()
    df_input = df2[[ 'Date', 'Close', share_1_ma, share_2_ma, share_3_ma]]
    #df2['EWM0.5']=df2['Close'].ewm(com=0.2).mean()

    #df2.plot()
    #plt.show()

    kefalaio = A_kefalaio
    df2.loc[(df2['Close'] <= df2[share_1_ma]) | (df2[share_1_ma].isnull()), 'larger_than_KMO10?'] = 0
    df2.loc[df2['Close'] > df2[share_1_ma], 'larger_than_KMO10?'] =  1
    df2.loc[0, share_1] = kefalaio
    i=1
    while i<(len(df2)-wait):
        df2.loc[i, share_1] = kefalaio
        if ((df2.loc[i, 'larger_than_KMO10?'] > df2.loc[i-1, 'larger_than_KMO10?']) and (df2.loc[i:i+wait, 'larger_than_KMO10?'].mean() == 1)):
            df2.loc[i : i+wait, share_1] = kefalaio
            i=i+wait
            stock = stock + (B*kefalaio)/df2.loc[i, 'Close']
            kefalaio=kefalaio*(1-B)
            print("to kefalaio einai  :", kefalaio, "    oi metoxes einai   :", stock)
        elif (df2.loc[i, 'larger_than_KMO10?'] < df2.loc[i-1, 'larger_than_KMO10?'] and (df2.loc[i:i+wait, 'larger_than_KMO10?'].mean() == 0) ):
            df2.loc[i : i+wait, share_1] = kefalaio
            i=i+wait 
            kefalaio=kefalaio+ df2['Close'][i]*stock
            stock = 0
            print("to kefalaio einai  :", kefalaio, "    oi metoxes einai   :", stock)  
        else:
            i=i+1

    kefalaio=kefalaio+df2['Close'][len(df2)-1-wait]*stock
    df2.loc[i : i+wait, share_1] = kefalaio
    print("bgalame kerdiiiiii           ",kefalaio)


    kefalaio = A_kefalaio
    df2.loc[(df2['Close'] <= df2[share_2_ma]) | (df2[share_2_ma].isnull()), 'larger_than_KMO20?'] = 0 
    df2.loc[df2['Close'] > df2[share_2_ma], 'larger_than_KMO20?'] = 1 
    df2.loc[0, share_2] = kefalaio
    i=1
    while i<(len(df2)-wait):
        df2.loc[i, share_2] = kefalaio
        if ((df2.loc[i, 'larger_than_KMO20?'] > df2.loc[i-1, 'larger_than_KMO20?']) and (df2.loc[i:i+wait, 'larger_than_KMO20?'].mean() == 1)):
            df2.loc[i : i+wait, share_2] = kefalaio
            i=i+wait
            stock = stock + (B*kefalaio)/df2.loc[i, 'Close']
            kefalaio=kefalaio*(1-B)
            print("to kefalaio einai  :", kefalaio, "    oi metoxes einai   :", stock)
        elif (df2.loc[i, 'larger_than_KMO20?'] < df2.loc[i-1, 'larger_than_KMO20?'] and (df2.loc[i:i+wait, 'larger_than_KMO20?'].mean() == 0) ):
            df2.loc[i : i+wait, share_2] = kefalaio
            i=i+wait 
            kefalaio=kefalaio+ df2['Close'][i]*stock
            stock = 0
            print("to kefalaio einai  :", kefalaio, "    oi metoxes einai   :", stock)  
        else:
            i=i+1


    kefalaio=kefalaio+df2['Close'][len(df2)-1-wait]*stock
    df2.loc[i : i+wait, share_2] = kefalaio
    print("bgalame kerdiiiiii           ",kefalaio)



    kefalaio = A_kefalaio
    df2.loc[(df2['Close'] <= df2[share_3_ma]) | (df2[share_3_ma].isnull()), 'larger_than_KMO40?'] = 0 
    df2.loc[df2['Close'] > df2[share_3_ma], 'larger_than_KMO40?'] = 1
    df2.loc[0, share_3] = kefalaio
    i=1
    while i<len(df2)-wait:
        df2.loc[i, share_3] = kefalaio
        if ((df2.loc[i, 'larger_than_KMO40?'] > df2.loc[i-1, 'larger_than_KMO40?']) and (df2.loc[i:i+wait, 'larger_than_KMO40?'].mean() == 1)):
            df2.loc[i : i+wait, share_3] = kefalaio
            i=i+wait
            stock = stock + (B*kefalaio)/df2.loc[i, 'Close']
            kefalaio=kefalaio*(1-B)
            print("to kefalaio einai  :", kefalaio, "    oi metoxes einai   :", stock)
        elif (df2.loc[i, 'larger_than_KMO40?'] < df2.loc[i-1, 'larger_than_KMO40?'] and (df2.loc[i:i+wait, 'larger_than_KMO40?'].mean() == 0) ):
            df2.loc[i : i+wait, share_3] = kefalaio
            i=i+wait 
            kefalaio=kefalaio+ df2['Close'][i]*stock
            stock = 0
            print("to kefalaio einai  :", kefalaio, "    oi metoxes einai   :", stock)  
        else:
            i=i+1


    kefalaio=kefalaio+df2['Close'][len(df2)-1-wait]*stock
    df2.loc[i : i+wait, share_3] = kefalaio
    print("bgalame kerdiiiiii           ",kefalaio)

    results = df2[ ['Date', share_1, share_2, share_3] ]

    results.set_index('Date', inplace=True)
    df_input.set_index('Date', inplace=True)
    print(results.head())
    #results.plot()
    #plt.show()
    return results,df_input



#kefalaio=1000
#B=0.6
#C=0.05
#N=400
#wait=10
#k=10
#MA_policy(kefalaio,B,wait,1,N,k)
#MA_policy(1000,0.6,8,1,300,10,"GE.csv")