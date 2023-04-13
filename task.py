import argparse
import pandas 

revenue_by_each_month_output = {}
revenue_by_each_product_output = {}
revenue_by_each_customer_output = {}

months_dict = {1: "jan", 2: "feb", 3: "mar", 4:"apr", 5: "may", 6: "jun", 7: "jul", 8: "aug", 9: "sep", 10: "oct", 11: "nov", 12: "dec"}

def revenue_by_each_month(data):
    try:
        month_dataframe = data
        month_dataframe['month'] = pandas.to_datetime(data['order_date']).dt.month
        months = month_dataframe['month'].unique()
        for month in months:
            month_details = month_dataframe.query('month == @month')
            revenue_by_each_month_output[months_dict[month]] = (month_details['product_price']*month_details['quantity']).sum()
        return revenue_by_each_month_output
    except Exception as e:
        print("Failled:", str(e))




def revenue_by_each_product(data):
    try:
        products_dataframe = data['product_name'].unique()
        for prod in products_dataframe:
            prod_details = data.query('product_name == @prod')
            revenue_by_each_product_output[prod] = (prod_details['product_price']*prod_details['quantity']).sum()
        return revenue_by_each_product_output
    except Exception as e:
        print("Failled:", str(e))

def revenue_by_each_customer(data):
    try:
        customer_dataframe = data['customer_id'].unique()
        for cust in customer_dataframe:
            cust_details = data.query('customer_id == @cust')
            revenue_by_each_customer_output[cust] = (cust_details['product_price']*cust_details['quantity']).sum()
        return revenue_by_each_customer_output
    except Exception as e:
        print("Failled:", str(e))


def main():
    parser = argparse.ArgumentParser(description="Provide orders.csv file path")
    parser.add_argument('-f','--filename', help='Provide file path', required=True)
    args = parser.parse_args()
    try:
        file_details = pandas.read_csv(args.filename)
        lst = ['cus_1']
        revenue_by_each_month(file_details)
        revenue_by_each_product(file_details)
        revenue_by_each_customer(file_details)
        print("revenue_by_each_month: ", revenue_by_each_month_output)
        print("revenue_by_each_product: ", revenue_by_each_product_output)
        print("revenue_by_each_customer: ", revenue_by_each_customer_output)
        sorted_customers_list = sorted(revenue_by_each_customer_output, key = revenue_by_each_customer_output.get, reverse=True)
        top_customers = 10 
        print("Top 10 customers: ")
        if len(sorted_customers_list) < 10:
            print("only ", len(sorted_customers_list), " customers are there")
            top_customers = len(sorted_customers_list)
        for i in range(0, top_customers):
            print(revenue_by_each_customer_output[sorted_customers_list[i]], " : ", sorted_customers_list[i] )
        
            
    except Exception as e:
        print("Failled:", str(e))


if __name__ == '__main__':
    main()
    
    
