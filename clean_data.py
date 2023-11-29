import pandas as pd
import numpy as np

def clean_main(month):
    # path need to be changed
    big_file_dir = "/Users/elychen/Desktop/CS448B_Final_Project/Code_Data/Airbnb_big_data/Jul_23_listings.csv"
    summary_file_dir = "/Users/elychen/Desktop/CS448B_Final_Project/Code_Data/Airbnb_summary_data/" + str(month) + "_listings.csv"

    df_big = pd.read_csv(big_file_dir)
    df_small = pd.read_csv(summary_file_dir)

    columns_missing = []
    for col in df_big.columns:
        if col not in df_small.columns:
            columns_missing.append(col)
    print(columns_missing)

    print(df_small)
    target_df = add_columns(df_big, df_small)
    print(target_df)

    remake_csv(target_df, month)

def add_columns(source_df, target_df):
    needed_columns = ['host_response_time', 'host_response_rate', 'host_acceptance_rate', 'host_is_superhost',
                      'host_has_profile_pic', 'host_identity_verified', 'property_type', 'accommodates', 'beds', 'number_of_reviews_l30d',  
                      'review_scores_rating', 'review_scores_accuracy', 'review_scores_cleanliness', 'review_scores_checkin', 
                      'review_scores_communication', 'review_scores_location', 'review_scores_value', 'instant_bookable']
    
    res_df = target_df.copy()
    for i in range(len(needed_columns)):
        res_df[needed_columns[i]] = source_df[needed_columns[i]]
    
    # drop column for name
    res_df = res_df.drop("name", axis="columns")

    res_df["est_revenue_l30d_prorated"] = res_df["minimum_nights"] * res_df["number_of_reviews_l30d"] / res_df["accommodates"] * 12 * res_df["price"]
    print(res_df["est_revenue_l30d_prorated"])

    return res_df

def remake_csv(df, month):
    filepath = "/Users/elychen/CS448B_Final_Project_Ely/CS448B_Final_Project/data_cleaned/" + str(month) + "_cleaned_listings_new.csv"
    df.to_csv(filepath, index=False)

month = 7
clean_main(month)