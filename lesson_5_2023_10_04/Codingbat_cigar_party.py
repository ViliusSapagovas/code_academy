# When squirrels get together for a party, they like to have cigars. 
# A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. 
# Unless it is the weekend, in which case there is no upper bound on the number of cigars. 
# Return True if the party with the given values is successful, or False otherwise.

party_date = input("Is it weekend? ('yes' or 'no'): ")
cigars_quantity = int(input("Enter the number of cigars: "))

if party_date == "no":
    if 40 <= cigars_quantity and cigars_quantity <= 60:
        print("TRUE, party will be succesfull!") 
    else: 
        print("FALSE, party will suck!")
elif party_date == "yes":
    if cigars_quantity >= 40:
        print("TRUE, party will be succesfull!")
    else: 
        print("FALSE, party will suck!")



