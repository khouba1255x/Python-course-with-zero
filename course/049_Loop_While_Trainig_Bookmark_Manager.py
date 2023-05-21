# ----------------------------
# -- Loop => While Training --
# -- Simple Bookmark Manage --
# ----------------------------

# Empty List To Fill Later
myFavouriteWebs = []

# Maximum Allowed Websites
maximumWebs = 5

while maximumWebs > 0 :
    
    print("=" * 40)
    # Input the new website
    web = input("Website Name Without https:// : ")
    
    # Add The New Website To The List 
    myFavouriteWebs.append(f"https://{web.strip().lower()}")
    
    # Decrease One Number From Allowed Websites
    maximumWebs -= 1
    
    # Print The Add Message
    print(f"Website Added, {maximumWebs} Places Left")
    
    # Print The List
    print(myFavouriteWebs)
    
else : 
    print("Bookmark is Full , You Cant add more")
   
# Check If List Is Not Empty
if len(myFavouriteWebs) > 0 :
    
    # Sort The List 
    myFavouriteWebs.sort()
    
    index = 0
    
    print("Printing The List Of Websites in Your Bookmark")
    
    while index < len(myFavouriteWebs) :
        print(myFavouriteWebs[index])
        index += 1
