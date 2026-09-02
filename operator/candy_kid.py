# Calculate how many candies each kid gets
# and how many candies are left over

candy_given = int(input("Enter the number of candies: "))
total_kid = int(input("Enter the total number of kids: "))

# // gives the whole-number quotient
# It tells us how many candies each kid receives
candy_per_kid = candy_given // total_kid

# % gives the remainder
# It tells us how many candies are left after equal distribution
remaining_candy = candy_given % total_kid

print(f"Candies per kid: {candy_per_kid}")
print(f"Remaining candies: {remaining_candy}")