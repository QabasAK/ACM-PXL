import streamlit as st

def explaining_training_levels():
    st.title("ACM Problem Solving Trainings")
    st.markdown("""
    <div style='text-align: justify'> The ACM Problem Solving Trainings are designed to help students enhance their algorithmic thinking and coding skills. The trainings are structured into different levels, each focusing on specific topics and techniques.
    </div>""", unsafe_allow_html=True)

    st.markdown("""
    <style>
    .announcement {
        backdrop-filter: blur(12px);
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.25);
        border-radius: 5px;
        padding: 1rem 1.5rem;
        margin-top: 1rem;
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);
    }

    .announcement h2 {
        margin: 0 0 0.25rem 0;
        font-size: 1.6rem;
        color: #ffffff;
    }

    .announcement h3 {
        margin: 0 0 0 0;
        font-size: 1.25rem;
        color: #ffffff;
        font-weight: normal;
    }

    .announcement p {
        margin: 0.25rem 0;
        font-size: 1rem;
        line-height: 1.5;
        color: #e0e0e0;
    }
    </style>

    <div class="announcement">
        <h2>📣 Summer 2025 Trainings:</h2>
        <h3>Level 1 — Introduction to Problem Solving</h3>
        <p><strong>Every Saturday</strong> — Check our weekly email updates for time and location</p>
        <p><strong>Trainers:</strong> Abdallah Barakat & Gaith Zakaria</p>
        <p><strong>Upcoming Topic:</strong> stuff to be added</p>
    </div>
""", unsafe_allow_html=True)




    st.subheader("Training Levels")
    st.markdown("""
    <div style='text-align: justify'> The levels are as follows:
    <ul>
        <li><strong>Level 0:</strong> Programming Basics in C++</li>
        <li><strong>Level 1:</strong> Introduction to Problem Solving</li>
        <li><strong>Level 2:</strong> Competitive Programming</li>
    </ul>
    </div>""", unsafe_allow_html=True)

    st.markdown("#### Curriculum")
    tab1, tab2, tab3 = st.tabs(["📘 Level 0", "📗 Level 1", "📙 Level 2"])

    with tab1:
        st.markdown("""
        #### Level 0 syllabus

        ##### Week 0:
        - Introduction to problem solving
        - Hello world
        - How does the computer understand code (compilation)

        ##### Week 1:
        - Explain Hello world in more detail
        - Output using cout
        - Variables and data types
        - Input using cin

        ##### Week 2:
        - Operators:
            - Assignment (=, +=, -=, etc)
            - Arithmetic (+, =, *, /, %)
            - Relational (<, <=, >, >=, ==, !=)
            - Logical (&&, ||, !)
        - If, if-else statements
        - Problems

        ##### Week 3:
        - Loops:
            - While
            - Do...while*
            - For
            - Nesting
        - Problems

        ##### Week 4:
        - Scope
        - Complexity basics
        - Problems

        ##### Week 5:
        - Problems

        ##### Week 6:
        - Arrays
        - Strings
        - Problems

        ##### Week 7:
        - Functions
        - Built-in functions*
        - Problems

        ##### Week 8:
        - Problems
        """)

    with tab2:
        st.markdown("""
        #### Suggested Topics & Structure for Level 1
        - Implementation (2 weeks)
            - Brute Force
            - Greedy
            - Sort
            - Search
            - Frequency Array
            - Prefix/Suffix Sum
        - STLs (2 weeks)
            - Vector
            - Pair
            - Stack
            - Queue
            - Iterators
            - Set
            - Map and Unordered_map
            - Priority Queue
        - Complete Search & Recursion (1 week)
        - Binary Search & Two Pointers (1 week)
        - Graphs (1 weeks)
        """)

    with tab3:
        st.markdown("""
        #### Suggested Topics for Level 2
        - Ad-hoc
        - Binary Search (on answer)
        - Bitmasks (Optional)
            - Bit Operation Tricks
            - Subsets and others
        - Number Theory
            -  GCD/LCM/Euclidean Algorithm (Optional)
            - Primes and Sieve (Optional)
            - Binary Exponentiation (Optional)
            - Euler Theorem, Fermat’s little theorem (modular inverse), division under mod (1 week)
        - Combinatorics (Optional)
        - DP I (1 week)
            - DP Mindset 
            - Thinking in states, Complete search and Memoization thinking
                - Knapsack
                - Robot up down
                - LCS
        - Graph Theory I (2 weeks)
            - Shortest Path (Dijkstra, Floyd, Bellman, …, etc)
            - Topological Sort
            - DSU (Union-Find)
            - Minimum Spanning Tree
        - Game Theory (1 week)
            - Nim Game
            - Grundy Numbers
        - Range Queries I (2 weeks)
            - Fenwick Tree
            - Sqrt Decomposition
            - Segment Tree
                - Lazy and others
        - String algorithms I (2 weeks)
            - KMP
            - Trie
        - Geometry (2 weeks)
            - Polygons
            - Convex Hull
            - Sweep Line
        - Graph Theory II (2 weeks)
            - Least Common Ancestor
            - DFS Tree (Bridges and Articulation Points)
            - Strongly Connected Components
        - DP II (2 weeks)
            - Bitmask
            - Digit
            - …
        - Range Queries II (2 weeks)
            - Sparse Table
            - Mo’s Algorithms
        - String algorithms II (2 weeks)
            - Hashing (Rabin-Karp)
            - Manacher algorithm & Z-function
        """)

        