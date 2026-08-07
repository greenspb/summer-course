import requests
import os

#Problem 1 - Basic Recursion
def recursive_squares(n: int) -> list[int]:
    if n
    if n == 1:
        return [n**2]
    if n > 1:
        return recursive_squares(n-1) + [n**2] 

def palindrome_checker(string: str) -> bool:
    if len(string) == 0 or len(string) == 1:
        return True
    if string[0] != string[-1]:
            return False
    else:
        return palindrome_checker(string[1:-1])

def length(my_list: list) -> int:
    try:
        my_list[-1]
    except IndexError as e:
        return 0
    if my_list[:-1] == []:
        return 1
    else:
        return length(my_list[:-1]) + 1


def flatten(list_: list) -> list:
    if isinstance(list_, int):
        return [list_]
    if len(list_) == 0:
        return []
    if len(list_) == 1:
        if isinstance(list_[0], list): 
            return flatten(list_[0])
        else:
            return list_
    return flatten(list_[:-1]) + flatten(list_[-1])

#Problem 2 - Multiple Recursion
def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)
    
def count_ways(n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 1
    return count_ways(n-2) + count_ways(n-1) 

def grid_paths(m: int, n: int) -> int:
    #Solve from endpoint (m-1, n-1) and work backwards summing (m-2,n-1) and (m-1,n-2) 
    if m == 1 or n == 1:  #Can move both down or right. Use both previous answers.
        return 1
    return grid_paths(m-1, n) + grid_paths(m, n-1) 
     
#Skip challenge.

#Problem 3 - Basic HTTP Requests
BASE_URL = 'https://jsonplaceholder.typicode.com'

def get_user(user_id: int) -> dict:
    suffix = f'/users/{user_id}'
    response = requests.get(url=BASE_URL+suffix)
    if response.status_code != 200:
        return {}
    return response.json()

def create_user(name: str, job: str) -> dict:
    suffix = '/users'
    response = requests.post(url=BASE_URL+suffix, json={"name": name, "job": job})
    if response.status_code != 201:
        return {}
    return response.json()

def update_user(user_id: int, name: str, job: str) -> dict:
    suffix = f'/users/{user_id}' 
    response = requests.put(url=BASE_URL+suffix, json={"name": name, "job": job})
    if response.status_code != 200:
        return {}
    return response.json()

def delete_user(user_id: int) -> bool:
    suffix = f'/users/{user_id}' 
    response = requests.delete(url=BASE_URL+suffix)
    if response.status_code == 200:
        return True
    else:
        return False

#Challenge
def get_users_page(page: int) -> list[dict]:
    response = requests.get(url=f'https://reqres.in/api/users?page={page}', headers={"x-api-Key": 'free_user_3Ha7WMScPCiJTOq9sMk7exbNzJc'})
    if response.status_code != 200:
        return {}
    return response.json()['data']

def partial_update_user(user_id: int, updates: dict) -> dict:
    response = requests.patch(url=f'https://reqres.in/api/users/{user_id}', headers={"x-api-Key": 'free_user_3Ha7WMScPCiJTOq9sMk7exbNzJc'}, json=updates)
    if response.status_code != 200:
        return {}
    return response.json()

#Problem 4 - Authenticated REST APIs

#Use a .env file to set environment variable for TMDB_API_TOKEN.
#echo TMDB_API_TOKEN=your_actual_token_here > .env
#echo  Python/Weekly\ Problem\ Sets/.env >> ../../.gitignore
#pip install python-dotenv
# import os
# from dotenv import load_dotenv
# # Automatically loads key-value pairs from .env into os.environ
# load_dotenv()
# # Specify the name of your environment variable
# token_env = "TMDB_API_TOKEN"
# token = os.getenv(token_env)
# if not token:
#     print(f"Missing token. Set environment variable: {token_env}")
# token = token.strip()

os.getenv("TMDB_API_KEY")

def search_movie(api_key: str, query: str) -> dict:
    url = 'https://api.themoviedb.org/3/search/movie'
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url=url, headers=headers, params={'query': query})
    if response.status_code != 200:
        return {}
    try:
        return response.json()['results'][0]
    except:
        return {}

#echo  Python/Weekly\ Problem\ Sets/.env >> ../../.gitignore
#pip install python-dotenv
# import os
# from dotenv import load_dotenv    
# load_dotenv()  # Automatically loads key-value pairs from .env into os.environ 
# token_env = "GH_API_TOKEN"  # Specify the name of your environment variable
# token = os.getenv(token_env)
# if not token:
#     print(f"Missing token. Set environment variable: {token_env}")
# token = token.strip()

def get_github_user(token: str, username: str) -> dict:
    url = f'https://api.github.com/users/{username}'
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url=url, headers=headers, params={'username': username})
    if response.status_code != 200:
        return {}
    return response.json()

def create_gist(token: str, description: str, filename: str, content: str) -> str:
    url = f'https://api.github.com/gists' 
    headers = {"Authorization": f"Bearer {token}"}
    json = {
        "description": description,
        "public": True,
        "files": {
            filename: {
                "content": content
            }
        }
    }
    response = requests.post(url=url, headers=headers, json=json)
    if response.status_code != 201:
        return {}
    return response.json()['id']

def delete_gist(token: str, gist_id: str) -> bool:
    url = f'https://api.github.com/gists/{gist_id}' 
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(url=url, headers=headers)
    if response.status_code != 204:
        return False
    return True


if __name__=='__main__':
    import pytest

    PROBLEM_NUMBER = 4

    if PROBLEM_NUMBER == 1:
        def test_recursive_squares():
            assert recursive_squares(1) == [1]
            assert recursive_squares(2) == [1, 4]
            assert recursive_squares(3) == [1, 4, 9]

        def test_palindrome_checker():
            assert palindrome_checker('')
            assert palindrome_checker('a')
            assert palindrome_checker('aa')
            assert palindrome_checker('ab') == False
            assert palindrome_checker('aaa') == True
            assert palindrome_checker('aab') == False
            assert palindrome_checker('bacon') == False
            assert palindrome_checker('radar') == True 

        def test_length():
            assert length([]) == 0
            assert length([1]) == 1
            assert length([1, 2]) == 2
            assert length([1, 2, 3]) == 3

        def test_flatten():
            assert flatten([]) == []
            assert flatten([1]) == [1]
            assert flatten([[1]]) == [1]
            assert flatten([1, 1]) == [1, 1]
            assert flatten([1, [1]]) == [1, 1]
            assert flatten([1, [2, 3], [4], 5]) == [1, 2, 3, 4, 5]

    if PROBLEM_NUMBER == 2:

        def test_fibonacci():
            assert fibonacci(0) == 0
            assert fibonacci(1) == 1
            assert fibonacci(2) == 1
            assert fibonacci(3) == 2
            assert fibonacci(4) == 3
            assert fibonacci(5) == 5
            assert fibonacci(6) == 8
            assert fibonacci(7) == 13
            assert fibonacci(8) == 21

        def test_count_ways():
            assert count_ways(0) == 1
            assert count_ways(1) == 1
            assert count_ways(2) == 2
            assert count_ways(3) == 3
            assert count_ways(4) == 5

        def test_grid_paths():
            assert grid_paths(1, 1) == 1
            assert grid_paths(2, 2) == 2
            assert grid_paths(2, 2) == 2
            assert grid_paths(2, 2) == 2
            assert grid_paths(3, 3) == 6
            i = 5
            assert grid_paths(i, 1) == 1
            assert grid_paths(1, i) == 1

    if PROBLEM_NUMBER == 3:

        def test_get_user():
            assert get_user(0) == {}
            assert get_user(1)
            assert get_user(10)
            assert get_user(11) == {}

        def test_create_user():
            assert create_user('John Doe', 'Developer') == {"name": "John Doe", "job": "Developer", "id": 11}

        def test_update_user():
            assert update_user(2, 'Jane Smith', 'Manager') == {"name": "Jane Smith", "job": "Manager", "id": 2}

        def test_delete_user():
            assert delete_user(2) == True

        def example_usage():
            # GET a user
            user = get_user(2)
            print(f"User: {user['name']} ({user['email']})")

            # POST to create a user
            new_user = create_user("John Doe", "Developer")
            print(f"Created user with ID: {new_user['id']}")

            # PUT to update a user
            updated = update_user(2, "Jane Smith", "Manager")
            print(f"Updated: {updated}")

            # DELETE a user
            success = delete_user(2)
            print(f"Deleted: {success}")

        def test_get_users_page():
            assert get_users_page(1)
            assert get_users_page(2)
            assert get_users_page(3) == []

        def test_partial_update_user():
            assert partial_update_user(2, {"job": "Senior Developer"})

    if PROBLEM_NUMBER == 4:
        def test_search_movie():
            import os
            from dotenv import load_dotenv    
            load_dotenv()  # Automatically loads key-value pairs from .env into os.environ 
            token_env = "TMDB_API_TOKEN"  # Specify the name of your environment variable
            token = os.getenv(token_env)
            if not token:
                print(f"Missing token. Set environment variable: {token_env}")
            token = token.strip()
            assert search_movie(token, "Inception")

        def test_get_github_user():
            #echo GH_API_TOKEN=your_actual_token_here > .env
            #echo  Python/Weekly\ Problem\ Sets/.env >> ../../.gitignore
            #pip install python-dotenv
            import os
            from dotenv import load_dotenv    
            load_dotenv()  # Automatically loads key-value pairs from .env into os.environ 
            token_env = "GH_API_TOKEN"  # Specify the name of your environment variable
            token = os.getenv(token_env)
            if not token:
                print(f"Missing token. Set environment variable: {token_env}")
            token = token.strip()
            assert problem_set.get_github_user(token, "torvalds")

        def test_create_gist():
            #echo GH_API_TOKEN=your_actual_token_here > .env
            #echo  Python/Weekly\ Problem\ Sets/.env >> ../../.gitignore
            #pip install python-dotenv
            import os
            from dotenv import load_dotenv    
            load_dotenv()  # Automatically loads key-value pairs from .env into os.environ 
            token_env = "GH_API_TOKEN"  # Specify the name of your environment variable
            token = os.getenv(token_env)
            if not token:
                print(f"Missing token. Set environment variable: {token_env}")
            token = token.strip()
            assert create_gist(token, "Test gist", "hello.py", "print('Hello')")

        def test_delete_gist():
            #echo GH_API_TOKEN=your_actual_token_here > .env
            #echo  Python/Weekly\ Problem\ Sets/.env >> ../../.gitignore
            #pip install python-dotenv
            import os
            from dotenv import load_dotenv    
            load_dotenv()  # Automatically loads key-value pairs from .env into os.environ 
            token_env = "GH_API_TOKEN"  # Specify the name of your environment variable
            token = os.getenv(token_env)
            if not token:
                print(f"Missing token. Set environment variable: {token_env}")
            token = token.strip()
            gist_id = create_gist(token, "Test gist", "hello.py", "print('Hello')")
            assert delete_gist(token, gist_id)

        def example_usage():
            from dotenv import load_dotenv  
            load_dotenv()
            TMDB_API_KEY = os.getenv("TMDB_API_TOKEN")
            GITHUB_TOKEN = os.getenv("GH_API_TOKEN")

            # Search for a movie
            movie = search_movie(TMDB_API_KEY, "The Matrix")
            print(f"Title: {movie['title']}, Year: {movie['release_date'][:4]}")

            # Get GitHub user info
            user = get_github_user(GITHUB_TOKEN, "octocat")
            print(f"{user['name']} has {user['public_repos']} public repos")

            # Create and delete a gist
            gist_id = create_gist(GITHUB_TOKEN, "My test gist", "test.txt", "Hello World!")
            print(f"Created gist: https://gist.github.com/{gist_id}")
            success = delete_gist(GITHUB_TOKEN, gist_id)
            print(f"Deleted: {success}")

        #example_usage()