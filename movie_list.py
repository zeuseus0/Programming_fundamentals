# Initial list of favorite movies
favorite_movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight", "Pulp Fiction"]

print("Current favorite movies:")
for movie in favorite_movies:
    print("-", movie)

# Add a movie
new_movie = input("\nEnter a movie to add to your favorites: ").strip()
if new_movie:
    favorite_movies.append(new_movie)
    print(f"'{new_movie}' has been added.")
else:
    print("No movie was added.")

# Remove a movie
remove_movie = input("\nEnter a movie to remove from your favorites: ").strip()
if remove_movie in favorite_movies:
    favorite_movies.remove(remove_movie)
    print(f"'{remove_movie}' has been removed.")
else:
    print(f"'{remove_movie}' is not in your favorites list.")

# Sort and print  list
favorite_movies.sort()
print("\nYour updated and sorted favorite movies list:")
for movie in favorite_movies:
    print("-", movie)
