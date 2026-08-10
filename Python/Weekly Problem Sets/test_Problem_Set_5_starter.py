import pytest
import importlib
problem_set = importlib.import_module('Problem Set 5 starter')

PROBLEM_NUMBER = 4

if PROBLEM_NUMBER == 1:
    def test_recursive_squares():
        assert problem_set.recursive_squares(1) == [1]
        assert problem_set.recursive_squares(2) == [1, 4]
        assert problem_set.recursive_squares(3) == [1, 4, 9]

    def test_palindrome_checker():
        assert problem_set.palindrome_checker('')
        assert problem_set.palindrome_checker('a')
        assert problem_set.palindrome_checker('aa')
        assert problem_set.palindrome_checker('ab') == False
        assert problem_set.palindrome_checker('aaa') == True
        assert problem_set.palindrome_checker('aab') == False
        assert problem_set.palindrome_checker('bacon') == False
        assert problem_set.palindrome_checker('radar') == True

    def test_length():
        assert problem_set.length([]) == 0
        assert problem_set.length([1]) == 1
        assert problem_set.length([1, 2]) == 2
        assert problem_set.length([1, 2, 3]) == 3

    def test_flatten():
        assert problem_set.flatten([]) == []
        assert problem_set.flatten([1]) == [1]
        assert problem_set.flatten([[1]]) == [1]
        assert problem_set.flatten([1, 1]) == [1, 1]
        assert problem_set.flatten([1, [1]]) == [1, 1]
        assert problem_set.flatten([1, [2, 3], [4], 5]) == [1, 2, 3, 4, 5]

if PROBLEM_NUMBER == 2:

    def test_fibonacci():
        assert problem_set.fibonacci(0) == 0
        assert problem_set.fibonacci(1) == 1
        assert problem_set.fibonacci(2) == 1
        assert problem_set.fibonacci(3) == 2
        assert problem_set.fibonacci(4) == 3
        assert problem_set.fibonacci(5) == 5
        assert problem_set.fibonacci(6) == 8
        assert problem_set.fibonacci(7) == 13
        assert problem_set.fibonacci(8) == 21

    def test_count_ways():
        assert problem_set.count_ways(0) == 1
        assert problem_set.count_ways(1) == 1
        assert problem_set.count_ways(2) == 2
        assert problem_set.count_ways(3) == 3
        assert problem_set.count_ways(4) == 5

    def test_grid_paths():
        assert problem_set.grid_paths(1, 1) == 1
        assert problem_set.grid_paths(2, 2) == 2
        assert problem_set.grid_paths(2, 2) == 2
        assert problem_set.grid_paths(2, 2) == 2
        assert problem_set.grid_paths(3, 3) == 6
        i = 5
        assert problem_set.grid_paths(i, 1) == 1
        assert problem_set.grid_paths(1, i) == 1

if PROBLEM_NUMBER == 3:
    def test_get_user():
        assert problem_set.get_user(0) == {}
        assert problem_set.get_user(1)
        assert problem_set.get_user(10)
        assert problem_set.get_user(11) == {}

    def test_create_user():
        assert problem_set.create_user('John Doe', 'Developer') == {"name": "John Doe", "job": "Developer", "id": 11}

    def test_update_user():
        assert problem_set.update_user(2, 'Jane Smith', 'Manager') == {"name": "Jane Smith", "job": "Manager", "id": 2}

    def test_delete_user():
        assert problem_set.delete_user(2) == True

    def test_get_users_page():
        assert problem_set.get_users_page(1)
        assert problem_set.get_users_page(2)
        assert problem_set.get_users_page(3) == []

    def test_partial_update_user():
        assert problem_set.partial_update_user(2, {"job": "Senior Developer"})

if PROBLEM_NUMBER == 4:

    def test_search_movie():
        #echo TMDB_API_TOKEN=your_actual_token_here > .env
        #echo  Python/Weekly\ Problem\ Sets/.env >> ../../.gitignore
        #pip install python-dotenv
        import os
        from dotenv import load_dotenv    
        load_dotenv()  # Automatically loads key-value pairs from .env into os.environ 
        token_env = "TMDB_API_TOKEN"  # Specify the name of your environment variable
        token = os.getenv(token_env)
        if not token:
            print(f"Missing token. Set environment variable: {token_env}")
        token = token.strip()
        assert problem_set.search_movie(token, "Inception")

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
        assert problem_set.create_gist(token, "Test gist", "hello.py", "print('Hello')")
    
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
        gist_id = problem_set.create_gist(token, "Test gist", "hello.py", "print('Hello')")
        assert problem_set.delete_gist(token, gist_id) 