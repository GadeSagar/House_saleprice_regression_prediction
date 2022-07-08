def outliers(df):
    con = []
    for i in df.columns:
        if(df[i].dtypes != "object"):
            con.append(i)
    outliers = []
    for i in con:
        outliers.extend(list(df[df[i]>3].index))
        outliers.extend(list(df[df[i]<-3].index))
    from numpy import unique
    return list(unique(outliers))

def catconsep(df):
    cat = []
    con = []
    for i in df.columns:
        if(df[i].dtypes == "object"):
            cat.append(i)
        else:
            con.append(i)
    return cat,con


def standardize(df):
    import pandas as pd
    cat,con = catconsep(df)
    from sklearn.preprocessing import StandardScaler
    ss = StandardScaler()
    X1 = pd.DataFrame(ss.fit_transform(df[con]),columns=con)
    return X1

def replacer(df):
    cat,con = catconsep(df)
    for i in con:
        x = df[i].mean()
        df[i]=df[i].fillna(x)

    for i in cat:
        x = df[i].mode()[0]
        df[i]=df[i].fillna(x)
        
        
def preprocessing(df):
    cat,con = catconsep(df)
    X1 = standardize(df)
    import pandas as pd
    X2 = pd.get_dummies(df[cat])
    Xnew = X1.join(X2)
    return Xnew