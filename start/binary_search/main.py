from binary_iterative import binary_iterative_f
from binary_recursive import binary_recursive_f
from binary_search_left import binary_search_left_f
from binary_search_right import binary_search_right_f

def main():
    a = [1,2,2,2,3,5,8,13]
    print(f"Our massive: {a}")
    for x in [2, 4, 13]:
        print(f"Search index number: {x}")
        print(f"Index from binary_iterative: {binary_iterative_f(a, x)}")
        print(f"Index from binary_recursive: {binary_recursive_f(a, x, 0, len(a)-1)}")
        # print(f"Index from binary_search_left: {binary_search_left_f(a, x)}")
        # print(f"Index from binary_search_right: {binary_search_right_f(a, x)}")
        print()
        
if __name__ == "__main__":
    main()