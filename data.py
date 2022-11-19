import pandas as pd
from seat import *

ticket_number = 0
df = pd.read_excel("USDOT_Consumer_Airfare_2007-2017-1.xlsx")
df = df.head(10000)

def Data_creation(number_of_data=30,df=df):
    Sample_data = df[["Year","City1","City2","Average Fare"]].sample(number_of_data)
    seat = Seats()
    Sample_data["Classes"] = [i for i in range(number_of_data)]
    Sample_data["Window"] = [i for i in range(number_of_data)]
    Sample_data["Seat Number"] = [i for i in range(number_of_data)]
    Sample_data["Date"] = [i for i in range(number_of_data)]
    Sample_data["Time"] = [i for i in range(number_of_data)]

    global ticket_number
    prev_ticket = ticket_number

    for i in range(0,number_of_data):
        hold_list = seat.price_config(Sample_data["Average Fare"].iloc[i])
        Sample_data["Average Fare"].iloc[i] = hold_list[0]
        Sample_data["Classes"].iloc[i] = hold_list[1]
        Sample_data["Window"].iloc[i] = hold_list[2]
        Sample_data["Date"].iloc[i] = seat.random_date(Sample_data["Year"].iloc[i])
        Sample_data["Time"].iloc[i] = seat.random_time()
        Sample_data["Seat Number"].iloc[i] = seat.seat_number_config()
        ticket_number += 1

    Sample_data["Ticket Number"] = [i for i in range(prev_ticket+1,ticket_number+1)]
    Sample_data = Sample_data.drop(["Year"],axis=1)
    return Sample_data

Sample_data = Data_creation()
