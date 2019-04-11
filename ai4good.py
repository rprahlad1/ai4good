def university(original_table, school_name, degree, education_flag=1):
    if type(degree) == list:
        df = pd.DataFrame()
        for deg in degree:
            instance = original_table.loc[((original_table["Education"] == deg)) 
                                     & ((original_table["Company"] == school_name)) 
                                     & (original_table["Education_Flag"] == education_flag)]
            df = pd.concat([df, instance], ignore_index=True)
        return df
    return original_table.loc[((original_table["Education"] == degree)) 
                                     & ((original_table["Company"] == school_name)) 
                                     & (original_table["Education_Flag"] == education_flag)].reset_index()

    