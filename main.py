from bs_url import *
from refresh import *
from product_data import *
QUERY = 'shoes'

prod_url = save_ids_get_url(QUERY)
refresh_cookie(prod_url)
session = create_session()

with open("file.txt", "r") as f:
    with open("Results.txt", "a") as g:
        count = 1
        for line in f:
            if count==15:
                print("First 15 Items Written")
                break
            line = line.rstrip()
            g.write(generate_data(line,count, session))
            g.write("\n")
            count+=1
        g.close()
    f.close()