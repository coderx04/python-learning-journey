
# def love_calculator(name1 , name2):
#     word1 = "true"
#     score1 = 0
#     word2 = "love"
#     score2 = 0

#     combined_name = name1 + name2
#     print(combined_name)

#     for letter in combined_name:
#         if letter in word1:
#             score1 += 1
#     print(score1)  

#     for letter in combined_name:
#         if letter in word2:
#             score2 += 1
#     print(score2)

#     print(f"your loves score is {str(score1)+str(score2)}")
    
# love_calculator("Pankaj Gupta","Pooja Saxena")

def calculate_love_score(name1 , name2):
    combined_names = name1 + name2
    lower_name = combined_names.lower()

    t = lower_name.count("t")
    r = lower_name.count("r")
    u = lower_name.count("u")
    e = lower_name.count("e")
    score1 = t+r+u+e
    

    l = lower_name.count("l")
    o = lower_name.count("o")
    v = lower_name.count("v")
    e = lower_name.count("e")
    score2 = l+o+v+e
    
    print(f"your love score is {str(score1)+str(score2)}")

calculate_love_score("AMit Garg", "Himanshu Dhingra")
