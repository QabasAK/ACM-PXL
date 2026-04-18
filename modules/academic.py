import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_pdf_viewer import pdf_viewer
import pandas as pd
import base64

###################################################################################
###################################################################################

def display_algorithms_course_content():

    st.title("Course Overview")
    st.header("Complexity Analysis")
    st.markdown("""
    Understand how the running time of an algorithm grows as input size `n` increases.
    Focus on the dominant term, ignoring constants and lower-order terms.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Big-O")
        st.caption("Upper bound — *“How bad can it get?”*")
        st.latex(r"f(n) = O(g(n)) \\ \exists c, a > 0,\ \forall n \ge a : f(n) \le c \cdot g(n)")

        st.subheader("Little-o")
        st.caption("Strictly less than")
        st.latex(r"\lim_{n \to \infty} \frac{f(n)}{g(n)} = 0")

    with col2:
        st.subheader("Big-Ω")
        st.caption("Lower bound — *“As good as it gets”*")
        st.latex(r"f(n) = \Omega(g(n)) \\ \exists c, a > 0,\ \forall n \ge a : f(n) \ge c \cdot g(n)")

        st.subheader("Little-ω")
        st.caption("Strictly greater than")
        st.latex(r"\lim_{n \to \infty} \frac{f(n)}{g(n)} = \infty")


    with col3:
        st.subheader("Big-Θ")
        st.caption("Tight bound — *“Exactly this fast”*")
        st.latex(r"f(n) = \Theta(g(n)) \\ f(n) = O(g(n))\ \text{and}\ f(n) = \Omega(g(n))")

        st.subheader("Tilde (∼)")
        st.caption("Functions are asymptotically equal")
        st.latex(r"\lim_{n \to \infty} \frac{f(n)}{g(n)} = 1")

    st.markdown("""
    Key properties include reflexivity, scaling, transitivity and symmetry. """) 
    st.markdown("""The real running time depends on more than just asymptotics 
    (hardware, constant factor, practical input) and the worst-case asymptotics can overestimate real performance (useful for determining scalability, not exact timing). 
    """)
    st.markdown("---")
    ###########################################################################################
    st.header("Divide & Conquer")
    st.markdown("Break a problem into smaller subproblems, solve them recursively, and combine the results.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Merge Sort")

        st.markdown("""
    - Recursively divide array, then **merge** in sorted order.
    - **Merge dominates** the cost.
    """)
        st.latex(r"T(n) = 2T\left(\frac{n}{2}\right) + \Theta(n) \\ = \Theta(n\log n)")
        
        st.markdown("""
    - **Merge step**:  
    $\Theta(n)$ compares + extra space $\Theta(n)$  
    - **Best**: ~ $n/2$  
    - **Worst**: $n - 1$
    """)

        st.markdown("**Optimizations:**")
        st.markdown("""
    1. Use **insertion sort** for small arrays  
    2. Use **bottom-up** (iterative) merge sort  
    3. Skip merge if already sorted (natural runs)
    """)

    with col2:
        st.subheader("Quick Sort")

        st.markdown("""
    - Pick pivot, partition array, sort sides  
    - **Partition dominates** the cost
    """)
        st.latex(r"T(n) = 2T\left(\frac{n}{2}\right) + \Theta(n) \\ = \Theta(n\log n)")
        st.latex(r"T(n) = T(n - 1) + \Theta(n) \\ = \Theta(n^2) \text{ (worst)}")

        st.markdown("""
    - **Best case**: pivot splits array evenly  
    - **Worst case**: pivot is min or max  
    """)

        st.markdown("**Optimizations:**")
        st.markdown("""
    1. Use **insertion sort** for small subarrays  
    2. Use **3-way partitioning** for duplicates  
    3. Choose pivot wisely: **median-of-three**, **pseudo-median**
    """)

    with col3:
        st.subheader("Quick Select")

        st.markdown("""
    - **Goal**: Find k-th smallest item (e.g., median)  
    - Uses same partitioning as quick sort
    """)
        st.latex(r"T(n) = T\left(\frac{n}{2}\right) + \Theta(n) = \Theta(n)")
        st.latex(r"T(n) = T(n - 1) + \Theta(n) \\ = \Theta(n^2) \text{ (worst)}")

        st.markdown("""
    - **Best**: Element found right after first partition  
    - **Worst**: Pivot always splits poorly  
    - Faster than full sorting for selection tasks
    """)   
    
    st.markdown("---")
    ###########################################################################################
    st.header("Recurrence Relations")

    st.markdown("Used to analyze the time complexity of recursive algorithms, especially **Divide & Conquer**.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Recursion Tree Method")
        st.latex(r"T(n) = aT\left(\frac{n}{b}\right) + f(n)")

        st.markdown(
            """
        - **Height of tree:**  $\\log_b n$  
        - **Nodes at level i:**  $a^i$  
        - **Work at level i:**  $a^i \\cdot f\\left(\\frac{n}{b^i}\\right)$  
        - **Total work:**  Sum over all levels
        """
        )

        st.markdown("> If problem size decreases by 1 each time → height = $n - 1$")

        st.subheader("Iterative Substitution")
        st.markdown("Keep expanding the recurrence to find a pattern.")
        st.latex(r"""
        \begin{align*}
        T(n) &= c + T(n/2) \\
            &= c + c + T(n/4) \\
            &= \dots \\
            &= c \log n + T(1) \\
            &= \Theta(\log n)
        \end{align*}
        """)    

    with col2:
        st.subheader("Master Theorem")
        st.markdown("For:")
        st.latex(r"T(n) = aT\left(\frac{n}{b}\right) + f(n),\quad a \ge 1,\ b > 1")

        st.markdown("Compare $f(n)$ to $n^{\log_b a}$:")

        st.markdown("**1. Case 1 (Leaf-heavy):**")
        st.latex(r"f(n) = O(n^{\log_b a - \epsilon}) \Rightarrow T(n) = \Theta(n^{\log_b a})")

        st.markdown("**2. Case 2 (Balanced):**")
        st.latex(r"f(n) = \Theta(n^{\log_b a}) \Rightarrow T(n) = \Theta(n^{\log_b a} \cdot \log n)")

        st.markdown("**3. Case 3 (Root-heavy):**")
        st.latex(r"f(n) = \Omega(n^{\log_b a + \epsilon}) \Rightarrow T(n) = \Theta(f(n))")
        st.markdown("Given the regularity condition")
        st.latex(r"a f(n/b) \le c f(n)\quad \text{for some } c < 1")

    st.markdown("---")
    ###########################################################################################

    st.header("Dynamic Programming")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("What is DP?")
        st.markdown("""
    Dynamic Programming is an optimization technique used for recursive problems that have:

    - Overlapping subproblems  
    - Optimal substructure
    """)

    with col2:
        st.subheader("How is it done?")
        st.markdown("""
    Two common approaches:

    - **Memoization** (Top-down with cache)  
    - **Bottom-up** (Tabulation from base cases)
    """)

    with col3:
        st.subheader("When to Use It")
        st.markdown("""
    Use DP when:

    - The same subproblem is solved multiple times  
    - The final solution can be built from solutions of smaller problems
    """)
    st.subheader("Common DP Examples")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**Fibonacci Sequence**")
        st.markdown("""
    - State: `F(n)`  
    - Time: $\\Theta(n)$  
    - Improves from exponential to linear  
        """)

    with col2:
        st.markdown("**Collecting Apples**")
        st.markdown("""
    - State: `max_apples(i, j)`  
    - Time: $\\Theta(NM)$  
    - Choose max of left/up paths  
        """)
    with col3:
        st.markdown("**0-1 Knapsack**")
        st.markdown("""
    - State: `Knapsack(i, W)`  
    - Time: $\\Theta(NW)$ (pseudo-polynomial)  
    - Can backtrack to find items  
        """)

    col_left, col_right = st.columns(2)
    with col_left:
        st.markdown("**Weighted Activity Selection**")
        st.markdown("""
    - State: `optimal(i)`  
    - Time: $\\Theta(N \log N)$  
    - Use `next(i)` to skip overlapping tasks  
        """)

    with col_right:
        st.markdown("**Longest Common Subsequence (LCS)**")
        st.markdown("""
    - State: `LCS(i, j)`  
    - Time: $\\Theta(nm)$  
    - Reconstruct in $O(n + m)$  
        """)

    st.markdown("---")
    ###########################################################################################

    st.header("Greedy Algorithms")
    st.markdown("""
    Greedy algorithms make **locally optimal choices** at each step, aiming for a **globally optimal solution**.  
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Fractional Knapsack")
        st.markdown("""
    - **Strategy**: Take items with **highest value/kg**  
    - **Sort by**: `v[i]/w[i]` descending  
    - **Time**: $\\Theta(n \log n)$  
    - **Optimality**:  
    If a solution skips higher-ratio items, it can be improved so it’s not optimal.
        """)

    with col2:
        st.subheader("Activity Selection")
        st.markdown("""
    - **Strategy**: Pick activity with **earliest finish time**  
    - **Sort by**: Finish time ascending  
    - **Time**: $\\Theta(n \log n)$  
    - **Optimality**:  
    Greedy picks can replace activities in any optimal solution without creating conflict.
        """)

    with col3:
        st.subheader("Interval Partitioning")
        st.markdown("""
    - **Goal**: Minimize number of rooms or colors  
    - **Strategy**: Schedule by **earliest start time**  
    - **Use**: Min-priority queue of room end-times  
    - **Time**: $\\Theta(n \log n)$  
    - **Optimality**:  
    Needs at least `depth` rooms (max overlapping intervals).
        """)

    st.markdown("---")
    ###########################################################################################

    st.header("Graph Algorithms")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        A **graph** is defined by:
        - A set of vertices **V** (nodes)
        - A set of edges **E** (pairs of vertices)
        """)
    with col2:
        st.markdown("""
        Graphs may be:
        - **Directed** or **Undirected**
        - **Weighted** or **Unweighted**
        """)

    st.subheader("Graph Representations")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Adjacency Matrix**")
        st.markdown("""
        - `Matrix[u][v] = 1` (or the weight), `0` (or ∞) otherwise
        - Best for **dense graphs**
        """)
        st.markdown("**Operations:**")
        st.table({
            "Operation": ["isAdjacent(u,v)", "neighbors(v)", "addEdge/removeEdge"],
            "Time Complexity": ["O(1)", "Θ(V)", "O(1)"]
        })

    with col2:
        st.markdown("**Adjacency List**")
        st.markdown("""
    - Stores a list of neighbors for each vertex in the graph
    - Best for **sparse graphs**
    """)
        st.markdown("**Operations:**")
        st.table({
            "Operation": ["isAdjacent(u,v)", "neighbors(v)", "addEdge/removeEdge"],
            "Time Complexity": ["O(deg(v))", "Θ(deg(v))", "O(deg(u))"]
        })

    st.subheader("Traversals")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Breadth-First Search (BFS)**")
        st.markdown("""
        - Explores in layers (level-by-level)
        - Uses a queue
        - Time: Θ(V + E)
        - Applications:
            - Connectivity check
            - Shortest unweighted paths
            - Cycle detection (undirected)
        """)

    with col2:
        st.markdown("**Depth-First Search (DFS)**")
        st.markdown("""
        - Explores as far as possible before backtracking
        - Uses recursion or a stack
        - Time: Θ(V + E)
        - Applications:
            - Connected components
            - Cycle detection (directed)
            - Topological ordering
        """)

    st.subheader("Algorithms")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**Topological Sort**")
        st.markdown("""
        - Linear ordering of a **DAG** where for every edge (u → v), u comes before v
        - Performed via **DFS**, using a stack
        - Applications:
            - Course scheduling
            - Build systems
            - Spreadsheet cell evaluation
        """)

    with col2:
        st.markdown("**Shortest Path – Dijkstra's Algorithm**")
        st.markdown("""
        - Finds shortest paths from source to all nodes
        - Works with **positive edge weights**
        - Uses **greedy relaxation**
        - Time complexity:
            - Binary Heap: O(E log V)
            - Unsorted Array: O(V²)
        - Applications:
            - Navigation systems
            - Network routing
        """)
    with col3:
        st.markdown("**Minimum Spanning Tree – Prim’s Algorithm**")
        st.markdown("""
        - Finds a minimum-weight tree connecting all vertices
        - Greedily picks the lightest edge connecting to the MST
        - Time complexity:
            - Binary Heap: O(E log V)
            - Unsorted Array: O(V²)
        - Based on **Cut Property**: Lightest edge crossing any cut must be in the MST
        """)

    st.markdown("---")
    ###########################################################################################

    st.header("Backtracking - Branch & Bound")
    st.markdown("""
    Brute force explores all possible solutions, which quickly becomes exponential. We need smarter strategies for:

    - **Constraint Satisfaction** (is the solution *valid*?)
    - **Optimization Problems** (is the solution *promising*?)
    """)

    st.subheader("Core Concepts")

    core_data = {
        "Technique": ["Brute Force", "Backtracking", "Branch & Bound"],
        "Key Idea": [
            "Try every combination",
            "Try all *valid* combinations",
            "Try all *promising* combinations"
        ],
        "When it Prunes": [
            "Never",
            "When a partial solution violates a constraint",
            "When potential value < current best"
        ]
    }

    core_df = pd.DataFrame(core_data)
    st.table(core_df)

    st.markdown("""
    All three use a **decision tree** where each node represents a partial solution, and recursion helps explore or prune paths.
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Pseudocode Structure")

        st.code("""
        solve(i):
            if i == N:
                check & return

            solution[i] = 0
            solve(i+1)

            solution[i] = 1
            solve(i+1)
        """, language="cpp")

    with col2:
        st.subheader("Performance Notes")

        # Data for Performance Notes table
        perf_data = {
            "Case": ["Worst Case", "Best Case"],
            "Work Done": ["2^N", "N"],
            "When?": [
                "When everything is valid/promising",
                "When most paths are infeasible early"
            ]
        }

        perf_df = pd.DataFrame(perf_data)
        st.table(perf_df)
        st.markdown("""
        Backtracking adds `isValid()` before going deeper.
        Branch & Bound adds `isPromising()` to prune further.
        """)

    st.markdown("---")
    ###########################################################################################

    st.header("NP-Completeness")
    st.markdown("""
    If a problem’s solution can be **verified quickly**, can it also be **solved quickly**?
    This is the heart of one of the most important open problems in computer science.
    """)

    st.subheader("Reduction")
    st.markdown("""
    A problem **X reduces to Y (X ≤ Y)** if solving Y helps solve X.

    - Used to prove hardness or unsolvability.
    - If Y is known to be hard and **Y reduces to X**, then X is also hard.
    """)

    st.subheader("Optimization vs. Decision Problems")
    col1, col2 = st.columns(2)
    with col1:
        
        st.markdown("""
        - **Optimization:** Find the best solution (e.g., shortest path, fewest colors).
        - **Decision:** Yes/No (e.g., Is there a path shorter than k?).

        Both types reduce to each other in polynomial time.
        """)
    with col2:
        st.markdown("""
        **Example: Traveling Salesman Problem**

        - If you have the **optimization solver**, use it to check answers to decision queries.
        - If you only have the **decision solver**, you can use **binary search** to solve the optimization version.
        """)
    st.subheader("Complexity Classes")

    df_classes = pd.DataFrame({
        "Class": ["P", "NP", "NP-Complete", "NP-Hard"],
        "Definition": [
            "Solvable in polynomial time.",
            "Verifiable in polynomial time (or solvable via nondeterministic TM).",
            "In NP, and every NP problem reduces to it in polynomial time.",
            "At least as hard as NP-Complete; may not be in NP or verifiable."
        ]
    })
    st.table(df_classes)

    st.subheader("Cook-Levin Theorem")
    st.markdown("""
    The **Cook-Levin Theorem** proves that the **SAT problem** is NP-Complete — the first such proof.

    > SAT: Is there a variable assignment that makes a Boolean formula true?
    """)

    st.code(r'''
    Φ = (¬x₁ ∨ x₂ ∨ x₃) ∧ (x₁ ∨ ¬x₂ ∨ x₃) ∧ (¬x₁ ∨ x₂ ∨ x₄)
    ''', language="latex")

    st.markdown("Try all $2^n$ assignments to find a satisfying assignment.")

    st.subheader("Karp's 21 NP-Complete Problems")
    st.markdown("Examples of classic NP-Complete problems:")

    problems = {
        "Problem": [
            "Hamiltonian Cycle",
            "Traveling Salesman Problem",
            "K-Colorable",
            "Bin Packing",
            "Subset Sum",
            "Subset Partition"
        ],
        "Description": [
            "Is there a cycle visiting every vertex once?",
            "Find a circuit that visits all nodes once with minimum cost.",
            "Color graph so that adjacent vertices have different colors.",
            "Pack objects into fewest bins without exceeding capacity.",
            "Is there a subset summing exactly to target value?",
            "Can the set be partitioned into two subsets of equal sum?"
        ]
    }
    st.table(pd.DataFrame(problems))

    st.info("Always review the syllabus to ensure you cover all required topics and examples.")
    
    with st.expander("Course Outcomes"):
        st.markdown("""
        - Apply advanced techniques for complexity analysis of algorithms using mathematical tools
        such as recurrences.
                            
        - Solve algorithmic problems with advanced techniques including divide-and-conquer, greedy,
        dynamic programming, graph algorithms, backtracking and enumeration.
                            
        - Select and apply the right combination of algorithmic methods and data structures for solving
        a problem based on complexity analysis.
                            
        - Implement various algorithms and measure their actual running times.
                """)


###################################################################################
###################################################################################


def display_datastructures_course_content():

    st.title("Course Overview")

    st.header("Asymptotic Analysis")
    st.markdown("""
    - Focuses on the **growth rate** of algorithms, ignoring constants and lower-order terms.
    - Compare algorithms using **Big-O notation** (worst-case)
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        | Order         | Description      |
        |---------------|------------------|
        | O(1)          | Constant         |
        | O(log n)      | Logarithmic      |
        | O(n)          | Linear           |
        | O(n log n)    | Linearithmic     |
        | O(n²), O(n³)  | Polynomial        |
        | O(2ⁿ), O(n!)  | Exponential / Factorial |
    """)
    with col2:
        st.markdown("""
        ```cpp 
                    for(int i=0; i<10; i++)  => O(1) 
            Op(); 

        for(int i=0; i<n; i++)      => O(n) 
            for(int j=0; j<n; j++)  => O(n) 
                Op();               => O(n^2) 

        for(int i=1; i<=n; i*=a)  => O(logn) 
            Op();       
        //If the inner loop depends on the outer loop 
        // => Trace and then find the sum
        ```
        """) 
    st.latex(r"""
        \text{constant }<\text{ logarithmic }<\text{polynomial} < \text{exponential} < \text{factorial} < n^n
    """)

    st.markdown("---")
    ###########################################################################################
    
    st.header("Searching & Sorting")
    st.subheader("Searching Algorithms")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Linear Search**")
        st.code("""cpp
    int search(int a[], int k, int n) {
        for (int i = 0; i < n; i++)
            if (a[i] == k) return i;
        return -1;
    }""", language="cpp")
        st.markdown("Best: O(1) • Worst: O(n)")

        st.markdown("""
        If the array is sorted, we could put another condition to return -1 if the key is less than the current element but the worst case becomes $2n$. """)

    with col2:
        st.markdown("**Binary Search**")
        st.code("""cpp
    int search(int a[], int k, int n) {
        int lo = 0, hi = n-1;
        while (lo <= hi) {
            int mid = lo + (hi-lo)/2;
            if (k == a[mid]) return mid;
            else if (k < a[mid]) hi = mid - 1;
            else lo = mid + 1;
        }
        return -1;
    }""", language="cpp")
        st.markdown("Best: O(1) • Worst: O(log n)")

    st.subheader("Sorting Algorithms")

    col1, col2, col3 = st.columns(3)

    with col1:
    #with st.expander("Selection Sort"):
        st.subheader("Selection Sort")
        st.code("""
    for (int i = 0; i < n-1; i++) {
        int min_idx = i;
        for (int j = i+1; j < n; j++)
            if (a[j] < a[min_idx])
                min_idx = j;
        if (min_idx != i)
            swap(a[i], a[min_idx]);
    }""")
        st.markdown("Time: Always O(n²) | Stable: ❌ | In-place: ✅")

    #with st.expander("Insertion Sort"):
    with col2:
        st.subheader("Insertion Sort")
        st.code("""
    for (int i = 1; i < n; i++) {
        int temp = a[i];
        int j = i-1;
        while (j >= 0 && temp < a[j])
            a[j+1] = a[j];
            j--;
        a[j+1] = temp;
    }""")
        st.markdown("Best: O(n), Worst: O(n²) | Stable: ✅ | In-place: ✅")

    with col3:
    #with st.expander("Bubble Sort"):
        st.subheader("Bubble Sort")
        st.code("""
    for (int i = 0; i < n-1; i++) {
        bool swapped = false;
        for (int j = n-1; j > i; j--)
            if (a[j] < a[j-1])
                swap(a[j], a[j-1]);
                swapped = true;
        if (!swapped) break;
    }""")
        st.markdown("Best: O(n), Worst: O(n²) | Stable: ✅ | In-place: ✅")


    st.markdown("---")
    ###########################################################################################
    
    st.header("Lists")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Singly Linked List")
        st.markdown("""
        Each node has a value and a pointer to the next node. Head points to the first node, tail points to the last node.
        (No backward traversal)
        """)
        st.image(r"images/mermaid-drawing (1).svg", width=1000)

        data = {
    "Operation": [
        "Add to head",
        "Add to tail",
        "Remove head",
        "Remove tail",
        "Contains"
    ],
    "Time": [
        "O(1)",
        "O(n)",
        "O(1)",
        "O(n)",
        "O(n)"
    ]
}

        df = pd.DataFrame(data)

        st.table(df)
    
    with col2:
        st.subheader("Doubly Linked List")
        st.markdown("""
        Each node has a value, a pointer to the next node, and a pointer to the previous node. Head points to the first node, tail to the last.
        """)
        st.image(r"images/mermaid-drawing.svg", width=1000)
        data = {
    "Operation": [
        "Add to head",
        "Add to tail",
        "Remove head",
        "Remove tail",
        "Contains"
    ],
    "Time": [
        "O(1)",
        "O(1)",
        "O(1)",
        "O(1)",
        "O(n)"
    ]
}

        df = pd.DataFrame(data)

        st.table(df)
    
    st.subheader("Ordered List")
    st.markdown("An ordered group of entries that can be represented with lists or arrays. Since it is ordered, data insertion is not up to the user, insertion is allowed but with specific positions.")

    data = {
        "Operation": ["Insert", "Merge", "Remove_Head()", "Remove_Tail()", "Contains"],
        "Time": ["O(n)", "O(m+n)", "O(1)", "O(1)", "O(n)"]
    }
    df = pd.DataFrame(data)
    st.table(df)

    st.markdown("---")
    ###########################################################################################

    st.header("Stacks & Queues")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Stack")
        st.markdown(""" Last In First Out (LIFO) structure. 
        An abstract data type in which the last element inserted (pushed) is the first element to be deleted (popped) and only the last element has direct $O(1)$ access. 

        """)
    with col2:
        st.subheader("Queue")
        st.markdown(""" First In First Out (FIFO) structure.
        An abstract data type in which the first element inserted (enqueued) is the first element to be deleted (dequeued) and only the first and last elements have direct $O(1)$ access. 

        """)

    data = {
        "Structure": ["Stack", "Queue"],
        "Push": ["O(1)", "O(1)"],
        "Pop": ["O(1)", "O(1)"]
    }

    df = pd.DataFrame(data)

    st.table(df)

    st.markdown("---")
    ###########################################################################################

    st.header("Binary Search Trees (BST)")
    st.markdown("""
    Binary Search Trees (BSTs) efficiently implement the **Set ADT**, supporting operations like `insert`, `remove`, and `contains`.
    Each node in a BST has at most two children: left (smaller) and right (greater).
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **BST Properties:**
        - **Depth**: Level of a node.
        - **Height**: Longest path from a node down to a leaf.
        - **Balanced BST**: Ensures height ≈ log(n), maintaining efficiency.
        - **Perfect BST**: Completely filled on all levels.
            """)
    with col2:
        st.markdown("""
        **How to Keep a BST Balanced:**
        - Insert medians recursively or shuffle inputs.
        - Use **AVL Trees** to rebalance after insertions/deletions using **rotations**:
            1. Left-left → Right rotation
            2. Right-right → Left rotation
            3. Mixed → Double rotations
        """)
    st.subheader("Operations Complexity")
    data = {
            "Structure": [
                "(Un/Ordered) List",
                "Unordered Array",
                "Ordered Array",
                "(Balanced) BST"
            ],
            "Insert(val)": ["O(n)", "O(n)", "O(n)", "O(logn)"],
            "Remove(val)": ["O(n)", "O(n)", "O(n)", "O(logn)"],
            "Contains(val)": ["O(n)", "O(n)", "O(logn)", "O(logn)"]
        }
    st.table(pd.DataFrame(data))

    st.subheader("Traversals Overview")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        #### Breadth-First Traversal:
        
        (Level-order) Uses a queue to visit nodes.
        """)

        st.code("""
        Queue<Node<T>*> queue;
        queue.enqueue(root);
        while (!queue.is_empty())
            Node<T>* node = queue.dequeue();
            // visit node
            if (node->left) 
                queue.enqueue(node->left);
            if (node->right) 
                queue.enqueue(node->right);
        """, language='cpp')

    with col2:
        st.markdown("#### Depth-First Traversals:")
        st.markdown("""
    1. **In-order (LCR)** – for sorted output  
    2. **Pre-order (CLR)** – useful for copying  
    3. **Post-order (LRC)** – useful for deletion

    | Traversal | Order | Use Case |  
    |-----------|-------|----------|  
    | In-order  | L C R | Print sorted tree  
    | Pre-order | C L R | Copy tree  
    | Post-order| L R C | Delete tree  

    """)

    with st.expander("Properties of Perfect BSTs"):
        st.markdown(r"""
    - Nodes: $N = 2^{\text{height}+1} - 1$  
    - Height: $\log_2(N+1) - 1$  
    - Leaves: $2^{\text{height}} = \frac{N+1}{2}$  
    - Internal nodes: $\frac{N-1}{2}$
    """)


    st.markdown("---")
    ###########################################################################################

    st.header("Hash Tables")
    st.markdown("""
    Hash Tables implement the **Set ADT** efficiently using a **hash function** to map keys to indices in an array.
    Each index (called a *bucket*) contains a linked list to handle **collisions** — known as **separate chaining**.
    """)

    st.subheader("Hashing for Strings")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("A string hash function using a positional system (base-26):")
        st.code("""
            int sum = 0, R = 1;
            for (int i = str.length() - 1; i >= 0; i--) 
            {
                sum += R * str[i];
                R *= 26;
            }
            return sum % m;
        """, language='cpp')
    with col2:
        st.markdown("""
        - Avoid using only the first character (leads to poor distribution).
        - Avoid summing ASCII values (different strings may yield the same sum).
        - Instead, use a **polynomial rolling hash**:
        """)
        st.code("""
        int sum = 0, R = 33;
        for (char c : val)
            sum = (sum * R + c) % m;
        """, language='cpp')

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Basic Operations")

        st.markdown("""
        **Operations:**
        - `insert(val)` ⇒ `table[hash(val)].add_to_tail(val)`
        - `remove(val)` ⇒ `table[hash(val)].remove(val)`
        - `contains(val)` ⇒ `table[hash(val)].contains(val)`

        **Collision Resolution:**  
        Use **linked list chaining** to handle hash collisions.
        """)
        st.markdown("Hash Tables are ideal for fast insert/search/remove, O(1) on average, but rely on good hash functions and dynamic resizing.")
    with col2:
        st.subheader("Load Factor & Resizing")

        st.markdown("""
        To keep operations efficient, we maintain a good **load factor**:

        - `n` = number of elements  
        - `m` = table size (number of buckets)  
        - **Load Factor** = `n / m`

        To ensure average-case O(1) time:
        1. Keep elements **uniformly distributed**
        2. Resize table:
            - If `n/m ≥ 8` → double the table size
            - If `n/m < 2` and `m > DEFAULT_TABLE_SIZE` → halve the table size
        """)

    st.subheader("Time Complexity")

    data = {
        "Structure": ["Balanced BST", "Hash Table (Avg Case)", "Hash Table (Worst Case)"],
        "Insert(val)": ["O(logn)", "O(1)", "O(1)"],
        "Remove(val)": ["O(logn)", "O(1)", "O(n)"],
        "Search(val)": ["O(logn)", "O(1)", "O(n)"]
    }
    st.table(pd.DataFrame(data))
    st.markdown("Rehashing runs in O(n + m), so it should happen only when necessary.")

    st.markdown("---")
    ###########################################################################################

    st.header("Priority Queues")

    st.markdown("""
    A **priority queue** is a special type of queue where elements are dequeued based on **priority** instead of insertion order. It is typically implemented as a **binary heap**, which satisfies:

    1. **Structure**: Must be a **complete binary tree**  
    2. **Order**: Each node is **not less than** its children (for max-heap)
    """)

    st.subheader("Array Representation")
    col1, col2 = st.columns(2)
    with col1:
        
        st.markdown("""
        A binary heap can be stored in an array using **level-order traversal**.

        - Parent of node at index `i` = `(i - 1) // 2`  
        - Left child = `2 * i + 1`  
        - Right child = `2 * i + 2`
        """)
    with col2:
        st.markdown("""
        Example array representation of a max-heap:
        ```
        [10, 9, 8, 7, 6, 5, 4]
        ```
        - Left child of `10` is `9` (index `1`)
        - Right child of `10` is `8` (index `2`)
        """)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Insertion")

        st.markdown("""
        To insert a value:
        - Add it at the end (maintains structure)
        - **Swim** it up until the heap order is restored

        Worst-case time: `O(logn)`
        """)
    with col2:
        st.subheader("Deletion")

        st.markdown("""
        To remove the max (or min):
        - Swap the root with the last element
        - Remove the last element
        - **Sink** the new root to restore heap order

        Worst-case time: `O(logn)`
        """)

    st.subheader("Time Complexity")

    df = pd.DataFrame({
        "Structure": ["Balanced BST", "Binary Heap"],
        "Insert(val)": ["O(logn)", "O(logn)"],
        "Remove(val)": ["O(logn)", "O(logn)"],
        "Search(val)": ["O(logn)", "O(1)"]
    })
    st.table(df)

    st.markdown("Binary heaps are ideal for priority queues due to their fast insertion and removal with a simple array-based structure.")

    st.info("Always review the syllabus to ensure you cover all required topics and examples.")
    with st.expander("Course Outcomes"):
        st.markdown("""
        - Perform basic time complexity analysis of algorithms.               
        - Analyze and evaluate, experimentally, the running time of algorithms.
        - Select the appropriate combination of data structures and algorithms for solving a problem or implementing an abstract data type.

        - Implement fundamental data structures, as well as algorithms for performing operations on these data structures.
        - Design computer programs that utilize fundamental data structures.
        """)

###################################################################################
###################################################################################

def display_structured_course_content():
    st.title("Course Overview")

    st.header("Basic Syntax, Functions and Memory")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Variables & Data Types")
        st.markdown("""
        - **Variables**: Named storage for data.
        - **Data Types**: Define the kind of data a variable can hold (e.g., int, float, char).
        """)

        st.code("""
        int x; // Integer variable declaration
        x = 10; // Variable assignment
                
        int age = 25;
        float salary = 50.5; //float variable initialization
        char grade = 'A';
        """, language="cpp")
        st.markdown(""" The data types specify the memory size and the operations that can be performed on the data.""")
        st.markdown("""
        ```int x;``` declares a variable `x` of type `int` so it allocates a space in the memory to store an integer.
        ```x = 10;``` assigns the value `10` to `x` so it places the value `10` in the allocated memory space.
        """)
        st.table(pd.DataFrame({
            "Specifier": ["%d", "%f", "%c", "%s"],
            "Description": [
                "Signed integer",
                "Floating number",
                "Single character",
                "String of characters"
            ],
            "Used with": [
                "`int`",
                "`float`, `double`",
                "`char`",
                "`char[]`"
            ]
        }))
    with col2:
        st.subheader("Input/Output Operations")
        st.code("""
        int x;
        printf("Enter the value of x: ");
        scanf("%d", &x);
        printf("Value of x: %d\\n", x); 
        """, language="cpp")
        st.markdown("""
        #### Taking Input from the User:
        """)
        st.code("""
        scanf("%d", &x); 
        """, language="cpp")
        st.markdown("""
        - `scanf` reads formatted input from the standard input (keyboard).
        - `%d` specifies that we expect an integer.
        - `&x` is the address of the variable `x` where the input will be stored.
        """)
        st.markdown("""
        #### Displaying Output to the User:
        """)
        st.code("""
        printf("Value of x: %d\\n", x);
        """, language="cpp")
        st.markdown("""
        - `printf` prints formatted output to the standard output (console).
        - `%d` is a format specifier for integers.
        - `\\n` adds a new line after printing.
        """)


    st.subheader("Functions")
    st.markdown("""
    Functions are **reusable blocks of code** that help make your program modular and easier to understand.
    """)
    col1, col2 = st.columns((58, 48))

    with col1:
        st.markdown("""
        - **Function Definition**: What the function does.
        - **Function Call**: Runs the function by name.
        - **Parameters**: Inputs the function accepts.
        - **Return Type**: What the function gives back.
        """)
    with col2:
        st.code("""
        return_type function_name(parameter_list){
            // what the function does
            return value;
        }
        """, language="cpp")
    
    st.markdown("""
    #### Types of Functions:
    """)
    st.table(pd.DataFrame({
            "Type": ["No parameters, no return", "Parameters, no return", "No parameters, return", "Parameters, return"],
            "Description": [
                "Function does not take any parameters nor return a value.",
                "Function takes parameters but does not return a value.",
                "Function does not take parameters but returns a value.",
                "Function takes parameters and returns a value."
            ],
            "Example": [
                "`void printHello()`",
                "`void printSum(int a, int b)`",
                "`float getNumber()`",
                "`int add(int a, int b)`"
            ]
        }))


    st.markdown("""
    #### Scope of Variables:
    - Variables defined inside a function are **local** to that function.
    - Variables defined outside any function are **global** and can be accessed anywhere in the program.
    
    Local variables are created when the function is called and destroyed when it exits vs. Global variables exist for the lifetime of the program.
    """)
    st.code("""
    void greet() {
        char name[] = "Alice"; 
        printf("Hello, %s!\\n", name); 
    }
    """, language="cpp")

    st.markdown("""
    In the above example, `name` is a local variable defined (i.e. only exists) inside the `greet` function.""")
    

    st.markdown("---")
    ###########################################################################################

    st.header("Conditionals and Loops")
    st.subheader("Conditional Statements")
    col1, col2 = st.columns(2)
    with col1:  
        st.markdown("#### If Statements")
        st.markdown("""
        **If-else statements** are used to make decisions in your code based on certain conditions.
        Syntax: `if` `else if` `else`""")
        st.code("""
        if (condition) {
            // execute if condition is true
        } else if (another_condition) {
            // execute if another_condition is true
        } else if (yet_another_condition) {
            // execute if yet_another_condition is true
        } else {
            // execute if no condition is true
        }
        """, language="cpp")
        st.markdown(""" The first true condition's block will execute, and the rest will be skipped. If no condition is true, the `else` block executes (if present).""")
        st.markdown(""" Use `==` for equality, `!=` for inequality, `<`, `>`, `<=`, and `>=` for comparisons. Avoid using a single `=` as it is an assignment operator.""")

    with col2:
        st.markdown("#### Switch Statements")
        st.markdown("""
        **Switch statements** are used to execute one block of code among many based on the value of a variable.
        Syntax: `switch` `case` `default`""")
        st.code("""
        switch (variable) {
            case value1:
                // execute if variable == value1
                break;
            case value2:
                // execute if variable == value2
                break;
            default:
                // execute if variable doesn't match any case
        }
        """, language="cpp")
        st.markdown(""" Use `break` to exit the switch statement after executing a case. If no `break` is used, it will continue executing the next case (known as "fall-through").""")
    
    st.subheader("Loops")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### For Loop")
        st.markdown("""
        A **for loop** is used to repeat a block of code a specific number of times.
        Syntax: `for`""")
        st.code("""
        for (initialization; condition; step) {
            // code to execute
        }
        """, language="cpp")

        st.markdown("""
        - **Initialization**: Set up a loop variable (e.g., `int i = 0`).
        - **Condition**: Check if the loop should continue (e.g., `i < n`).
        - **Step**: Update the loop variable (e.g., `i++`).
        """)

        st.markdown(""" Loop control keywords include `break` (exit loop) and `continue` (skip to next iteration).""")
    with col2:
        st.markdown("#### While Loop")
        st.markdown("""
        A **while loop** continues to execute as long as a condition is true.
        Syntax: `while`""")
        st.code("""
        while (condition) {
            // code to execute
        }
        """, language="cpp")
        st.markdown("""
        #### Do-While Loop
        A **do-while loop** executes the code block at least once before checking the condition.
        Syntax: `do` `while`""")
        st.code("""
        do {
            // code to execute
        } while (condition);
        """, language="cpp")
    
    st.markdown("""---""")
    ###########################################################################################

    st.header("Arrays, Searches and Sorts")
    st.markdown("""Arrays are collections of elements of the same type, stored in contiguous memory locations. They allow efficient access to elements using indices.
    """)
    st.code("""
    int arr[5]; // Declare an array of integers of size 5
    arr[0] = 10; // Assign value to first element
    arr[1] = 20; // Assign value to second element
            
    int a[3] = {1, 2, 3};
    char word[] = "hi"; // includes null terminator '\\0'
    """, language="cpp")
    st.markdown(""" Notes: Indexing starts at 0, so `arr[0]` is the first element. Out-of-bounds access (e.g., `arr[5]` in a 5-element array) is undefined behavior.""")
    st.markdown(""" Another Note: When calling a function with an array, you can pass the array name without brackets, and it will be treated as a pointer to the first element of the array.
    """)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Searching Algorithms")
        st.markdown("""Searching algorithms find the position of a value in an array.
        """)
        st.code("""
        int search(int arr[], int n, int key) {
            for (int i = 0; i < n; i++) {
                if (arr[i] == key) {
                    return i; // Key found at index i
                }
            }
            return -1; // Key not found
        }
        """, language="cpp")
        st.markdown("""
        The above code structure can be used for any question that requires searching for a value in an array and working on it (whether modify it, return it, etc.).
        """)
    with col2:
        st.subheader("Sorting Algorithms")
        st.markdown("""Sorting algorithms arrange the elements of an array in a specific order (ascending or descending) like bubble sort.
        """)
        st.code("""
        void bubbleSort(int arr[], int n) {
            for (int i = 0; i < n-1; i++) {
                for (int j = 0; j < n-i-1; j++) {
                    if (arr[j] > arr[j+1]) {
                        int temp = arr[j];
                        arr[j] = arr[j+1];
                        arr[j+1] = temp;
                    } // if statement closing bracket
                } // inner loop closing bracket
            } // outer loop closing bracket
        } // function closing bracket
        """, language="cpp")

    st.markdown("""---""")
    ###########################################################################################

    st.header("2D Arrays and Matrices")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""2D arrays (or matrices) are arrays of arrays, allowing storage of data in a grid-like structure. They are useful for representing tables, images, and more.
        """)
        st.code("""
        int matrix[3][4]; // Declare a 2D array (3 rows, 4 columns)
        matrix[0][0] = 1;  // Assign value to first element
        matrix[1][2] = 5;  // Assign value to second element
        """, language="cpp")

    with col2:
        st.markdown(""" To traverse a 2D array, you can use nested loops:
        """)
        st.code("""
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 4; j++) {
                printf("%d ", matrix[i][j]);
            }
            printf("\\n");
        }
        """, language="cpp")

    st.subheader("Calculations on 2D Arrays")
    st.markdown("""You can perform various calculations on 2D arrays, such as finding the sum of all elements, the maximum element, or transposing the matrix.
    """)
    col1, col2 = st.columns(2)  
    with col1:
        st.subheader("Sum & Average of All Elements")
        st.code("""
        int sum = 0;
        int count = 0;
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 4; j++) {
                sum += matrix[i][j];
                count++;
            }
        printf("Sum: %d\\n", sum);
        printf("Average: %.2f\\n", (float)sum / count);
        """, language="cpp")

    with col2:
        st.subheader("Finding Maximum and Minimum Element")
        st.code("""
        int max = matrix[0][0];
        int min = matrix[0][0];
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 4; j++) {
                if (matrix[i][j] > max) max = matrix[i][j];
                if (matrix[i][j] < min) min = matrix[i][j];
            }
        printf("Maximum Element: %d\\n", max);
        printf("Minimum Element: %d\\n", min);
        """, language="cpp")

    st.subheader("Matrix Manipulation")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        with st.expander("#### Row Swapping"):
            st.code("""
            for (int j = 0; j < 4; j++){
                int temp = matrix[row1][j];
                matrix[row1][j] = matrix[row2][j];
                matrix[row2][j] = temp;
            }
            """, language="cpp")
    with col2:
        with st.expander("#### Column Swapping"):
            st.code("""
                for (int i = 0; i < 3; i++){
                    int temp = matrix[i][col1];
                    matrix[i][col1] = matrix[i][col2];
                    matrix[i][col2] = temp;
                }
            """, language="cpp")    
    with col3:
        with st.expander("""#### Transposing Matrix"""):
            st.code("""
                for (int i = 0; i < 3; i++)
                    for (int j = i + 1; j < 4; j++){
                        int temp = matrix[i][j];
                        matrix[i][j] = matrix[j][i];
                        matrix[j][i] = temp;
                    }
            """, language="cpp")
    with col4:
        with st.expander("Row/Column Shifting"):
            st.code("""
            for (int j = cols - 1; j > 0; j--)
                mat[0][j] = mat[0][j - 1];
            mat[0][0] = 0; //placeholder
            """)

    st.markdown(""" ---""")
    ###########################################################################################

    st.header("Recursion and Recursive Array Processing")
    st.markdown("""Recursion is a programming technique where a function calls itself to solve smaller instances of the same problem. It is often used for problems that can be broken down into smaller subproblems.
    """)
    st.code("""
    return_type function_name(params) {
        if (base_case)
            return result;
        else
            return function(smaller_problem);
    }
    """, language="cpp")
    
    st.subheader("Recursion vs. Iteration")
    st.table(pd.DataFrame({
            "Feature": ["Uses", "Control", "Memory", "Performance"],
            "Recursion": [
                "Function calls",
                "Base case & recursive call",
                "Uses call stack for each call",
                "Usually slower due to overhead"
            ],
            "Iteration": [
                "Loops",
                "Loop condition & increment",
                "Used less memory (single stack frame)",
                "Usually faster due to less overhead"
            ]
        }))

    st.subheader("Recursive Array Processing")
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.expander("Print All Elements"):
            st.code("""
            void printArray(int arr[], int n) {
                if (n == 0) return; 
                printf("%d ", arr[n-1]); 
                printArray(arr, n-1); 
            }
            """, language="cpp")
    with col2:
        with st.expander("Sum All Elements"):
            st.code("""
            int sumArray(int arr[], int n) {
                if (n == 0) return 0; 
                return arr[n-1] + sumArray(arr, n-1); 
            }
            """, language="cpp")
    with col3:
        with st.expander("Find Maximum Element"):
            st.code("""
            int maxArray(int arr[], int n) {
                if (n == 1) return arr[0]; 
                return max(arr[n-1], maxArray(arr, n-1)); 
            }
            """, language="cpp")

    st.markdown("""---""")
    ###########################################################################################
    
    st.header("Pointers and Pointer Arithmetic")
    st.markdown("""Pointers are variables that store memory addresses of other variables. They allow direct manipulation of memory and are essential for dynamic memory allocation and data structures.
    """)
    st.code("""
    void pointerExample() {
        int var = 5;
        int *ptr = &var; // Pointer to var
        printf("Value of var: %d", *ptr);
    }
    """, language="cpp")
    st.markdown("""
    - `int *ptr = &var;` declares a pointer `ptr` that points to the address of `var`.
    - `*ptr` dereferences the pointer to access the value stored at that address.
    """)

    st.subheader("Function call by Reference")
    st.markdown("""
    Pointers can be used to pass variables by reference to functions, allowing the function to modify the original variable.

    """)    
    st.code("""
    void modifyValue(int *ptr) {
        *ptr = 10; // Modify the value at the address pointed to by ptr
    }
    
    int x = 5;
    modifyValue(&x); // x is now 10
    """, language="cpp")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Pointers and Strings")
        st.markdown("""
        Strings in C are arrays of characters, and pointers can be used to manipulate them.
        """)

        st.code("""
        void stringExample() {
            char str[] = "Hello";
            char *ptr = str; // Point to first char
            printf("First character: %c", *ptr);
        }
        """, language="cpp")
        st.markdown("""
        - `char *ptr = str;` points to the first character of the string.
        - `*ptr` dereferences the pointer to access the first character.
        """)

    with col2:
        st.subheader("Pointers and Arrays")
        st.markdown("""
        Pointers can be used to access and manipulate arrays.
        """)
        st.code("""
        void arrayExample() {
            int arr[] = {1, 2, 3, 4, 5};
            int *ptr = arr; // Point to first element
            for (int i = 0; i < 5; i++) {
                printf("%d ", *(ptr + i)); 
            }
        }
        """, language="cpp")
        st.markdown("""
        - `int *ptr = arr;` points to the first element of the array.
        - `*(ptr + i)` accesses each element using pointer arithmetic.
        """)
    
    st.table(pd.DataFrame({
            "Concept": ["Declaration", "Initialization", "Dereferencing", "Function by Reference", "Pointer Arithmetic", "Strings and Pointers"],
            "Example": [
                "`int *ptr;`",
                "`ptr = &var;`",
                "`*ptr`",
                "`void foo(int *ptr)`",
                "`*(ptr + i)`",
                "`char *ptr = 'Hi';`"
            ],
            "Notes": [
                "Pointer to int",
                "Store address of var",
                "Access value at address",
                "Use `&` to pass address",
                "Move pointer to next element",
                "C strings use char pointers"
            ]
        }))
    
    
    
    st.info("Always review the syllabus to ensure you cover all required topics and examples.")
    with st.expander("Course Outcomes"):
            st.markdown("""
            - Configure and Navigate within development IDE to edit, compile and execute programs.               
            - Identify and Apply Elements of a computer program, incl. I/O, Loops, Logical Blocks, Functions, Arrays and Pointers as per problem at hand.
            - Use and justify appropriate data types for programming problem.
            - Design structured programs with effective algorithms using a combination of standard and User-defined constructs.
            - Explain solution to professor or committee to highlight design choices and justify technical decisions.
            """)

###################################################################################
###################################################################################

def display_OOP_course_content():
    st.title("Course Overview")

    st.header("Functions, Scope and Overloading")
    col1, col2 = st.columns((60,40))
    with col1:
        st.markdown("""
        - **Call by Value** A copy of the argument is passed.
        - **Call by Reference** The actual variable is passed using references (`&`).
        - **Call by Address** A pointer to the variable is passed.
        """)
    with col2: 
        st.code("""
        void square(int x); // Call by Value
        void square(int &x); // Call by Reference
        void square(int *x); // Call by Address
        """, language="cpp")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Function Overloading")
        st.markdown("Same function name with different parameter types or counts.")
        st.code("""
        int add(int a, int b);
        float add(float a, float b);
        """, language="cpp")
        st.markdown("It allows multiple functions with the same name but different parameter lists (number or type of parameters) in the same scope.")
    with col2:
        st.subheader("Variable Scope & Default Parameters")
        st.markdown("Default parameters allow to not send a specific variable while using the value in the signature.")
        st.code("void greet(string name = \"User\");", language="cpp")
        st.markdown("""
        - **Local**: Inside block/function
        - **Global**: Outside any function
        - **Static**: Retains value between calls
        """)
    st.subheader("Single-Dimensional Array Operations")
    st.markdown("""
    - Declare: int arr[10];
    - Loop through: for (int i = 0; i < size; i++)
    - Common operations:
        Sum
        Average
        Min/Max
        Sorting/searching
    """)

    st.markdown("""---""")
    ##########################################################

    st.header("Classes and Objects -- Intro")
    st.markdown("Each class consists of data members and member functions that can be used with that class.")
    col1, col2 = st.columns(2)
    with col1:
        st.code("""
        class Student {
        private:
            string name;
        public:
            void setName(string n);
            string getName();
        };
        """, language="cpp")
        
        st.subheader("Member Functions")
        st.markdown("""
        (Include Setters & Getters which helps in applying encapsulation and data hiding, avoiding unnecessary or malicious access)
        - Can have default parameters
        - Can take object parameters
        """)
        st.subheader("Destructor")
        st.markdown('''
        A destructor cleans up when an object goes out of scope or is deleted. It's often used to free memory or close files.
        
        - Same name as the class but with a ~ prefix.
        - No parameters, no return type.
        - Automatically called when the object is destroyed.
        
        ```cpp
        class A {
        public:
            ~A() {
                cout << "Destructor called!";
            }
        };
        ```
        If inheritance is involved, the base class constructor runs first then the derived class constructor. When destroyed, derived class destructor runs first then base class destructor.

        ''')

        st.subheader("Interface Implementation")
        st.markdown('''
        ```cpp
        // in .h file
        class MyClass {
        public:
            void show(); //function signature
        };
        //in `.cpp` file:
        void MyClass::show() { //scope resolution
            cout << "Showing...";
        }
        ```
        ''')
    with col2:
        st.subheader("Constructors")
        st.markdown("""
        A **constructor** is a special function that automatically runs when an object is created. Its purpose is to **initialize the object**.
        
        - Same name as the class.
        - No return type (not even `void`).
        - Can be overloaded (multiple constructors with different parameters).  

        #### Types of Constructors:

        1. **Default Constructor**
        ```cpp
        class A {
        public:
            A() {
                cout << "Default constructor";
            }
        };  
        ```
        2. **Parameterized Constructor**
        To initialise an object with specific values provided as arguments.
        ```cpp
        class A {
            int x;
        public:
            A(int value) {
                x = value;
            }
        };    
        ```
        3. **Initializer List**
        ```cpp
        class A {
            int x;
        public:
            A(int value) : x(value) { }
        };
        ```
        4. **Copy Constructor**
        It creates a new object as a copy of existing, It takes a reference to an object of the same class as its parameter.
        ```cpp
        class A {
            int x;
        public:
            A(const A &obj) {
                x = obj.x;
            }
        };
        ```        
        """)

    st.markdown("""---""")

    st.header("Classes and Objects -- Advanced")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Constant Members")
        st.markdown("""
        Constant objects can only call constant member functions.
        """)
        st.code("""
        class MyClass {
            const int id;
            void print() const;
        };
        """)
    with col2:
        st.subheader("Static Members")
        st.markdown("""
        
        """)
        st.code("""
        class MyClass {
            static int count;
            static void showCount();
        };
        """)
    
    st.subheader("Composition")
    st.code("""
    class Engine {
    public:
        void start();
    };

    class Car {
        Engine e; // "Has-a" relationship
    };
    """)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Objects & Dynamic Memory")
        st.code("""
        Student *s = new Student();
        delete s;
        """)
    with col2:
        st.subheader("'this' Pointer")
        st.code("""
        void setName(string name) {
            this->name = name;
        }
        """)
    with col3:
        st.subheader("Friend Functions")
        st.code("""
        class MyClass {
            friend void show(MyClass obj);
        };
        """)

    st.markdown("""---""")

    st.header("Inheritance")
    col1, col2 = st.columns(2)
    with col1:
        st.code("""
    class Shape {
    public:
        void draw() { cout << "Drawing shape\\n"; }
    protected:
        int color;
    private:
        int id;
    };

    class Circle : public Shape {
    public:
        void drawCircle() { cout << "Drawing circle\\n"; }
        void setColor(int c) { color = c; }
    };
    """, language="cpp")
        st.markdown(""" **Public Inheritance**:
    - Public members of `Shape` remain public in `Circle`
    - Protected members remain protected (accessible within `Circle`)
    - Private members (`id`) are **not inherited**
        """) 

        st.markdown("""
        **Constructor & Destructor Calls**  
        - Base class constructor runs **first**, then derived constructor.  
        - Derived destructor runs **first**, then base destructor.
        """)

    with col2:
        st.subheader("Quick Review")
        st.markdown("""
    **What is Inheritance?**  
    Inheritance allows a class (derived) to inherit properties and behavior from another class (base), enabling:

    - **Code reuse**: Write common code once in base class.  
    - **Hierarchical relationships**: Model 'is-a' relationships (e.g., Circle is a Shape).  
    - **Extensibility**: Extend or override base class functionality.

    **Types of Inheritance**  
    - Single, Multiple, Multilevel, Hierarchical, Hybrid.

    **Access Specifiers Impact**  
    - `public` inheritance: public & protected members keep access.  
    - `protected` inheritance: public & protected members become protected.  
    - `private` inheritance: public & protected members become private.
    """)

    st.markdown("""---""")
    st.header("Polymorphism")

    st.markdown("""
    Polymorphism in C++ allows the same function or operator to behave differently based 
    on the type or object it's applied to. It enables flexibility and code reuse in OOP.
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
    ### Types of Polymorphism
    - **Compile-Time (Static)** – Decided by the compiler.  
    Examples: **Function overloading**, **Operator overloading**.
    - **Run-Time (Dynamic)** – Decided at program execution using **virtual functions** 
    and **pointers/references to base classes**.
    """)
    with col2:
        st.markdown("""
    ### Key Benefits
    - **Flexibility** – One interface, multiple implementations.  
    - **Code Reuse** – Same code can work with different types.  
    - **Extensibility** – Easily add new classes without changing existing code.
    """)
    st.code("""
class Shape {
public:
    virtual void draw() { cout << "Drawing shape\\n"; }
};

class Circle : public Shape {
public:
    void draw() { cout << "Drawing circle\\n"; }
};

Shape* s = new Circle();
s->draw(); // "Drawing circle"
""", language='cpp')

    st.markdown("---")

    st.header("Operator Overloading")
    st.markdown("""
    a feature in C++ that allows programmers to redefine the way operators work for user-defined types (such as classes and structs).
    It enables objects to be manipulated using familiar operators (`+`, `-`, `==`, `[]`, etc.) in a natural and intuitive way.
    """)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - Readability & Maintainability -- Code using obejcts looks like built-in type operations.
        - Custom Behavior -- Extend existing operators to work with complex data types.
        - Encapsulation -- Keep implementation details hidden while offering clear interfaces.
        """)
    with col2:
        st.code("""
        // Instead of c1.add(c2)
        Complex c1(2, 3), c2(1, 4);
        Complex c3 = c1 + c2;
        """)
    
    with col1:
        st.table(pd.DataFrame({
            "Operation" : ["Arithmetic", "Relational", "Logical", "Assignment", "Inc/Dec,", "Indexing", "Input/Output"],
            "Operators": ["`+`, `-`, `*`, `/`, `%`", "`==`, `!=`, `<`, `>`, `<=`, `>=`", "`&&`, `||`, `!`", "`=`, `+=`, `-=`", "`++`, `--`", "`[]`, `()`, `->`, `*`", "`<<`, `>>`"] 
        }))
    
    with col2:
        st.markdown("""
        - At least one operand must be a user-defined type.
        - Cannot create new operators—only redefine existing ones.
        - Some operators cannot be overloaded: `.:`, `.*`, `::`, `sizeof`, `typeid`, `? :`
        - Overloaded operators do not change precedence or associativity.
        - Overloading should follow expected semantics to avoid confusion.
        """)
    
    st.subheader("Implementation")
    col1, col2 = st.columns((35, 65))
    with col1: 
        st.markdown("""
        Operators are overloaded by defining them as:
        1. **Member functions** such that it operates on the calling object 
        2. **Non-member friend function** such that it allows symmetry between operands.
        """)
    with col2:
        st.code("""
        class Complex {
            double real, imag;
        public:
            Complex(double r=0, double i=0) : real(r), imag(i) {}
            Complex operator+(const Complex &other) const {
                return Complex(real + other.real, imag + other.imag);
            }
        };
        """)
    st.markdown("Make sure to keep operator meaning consistent with built-in types. Prefer member functions when the left-hand operand is the class type.")

    st.info("Always review the syllabus to ensure you cover all required topics and examples.")
    with st.expander("Course Outcomes"):
            st.markdown("""
            - Analyze user’s programming requirements to identify their components.          
            - Write functional, error-free programs using basic OO concepts including Constructors/Destructors and Arrays of Objects.
            - Apply intermediate OO Concepts including Composition, Consts, Statics and Pointers.
            - Write computer programs with advanced OO Concepts incl. Dynamic Memory, Inheritance and Polymorphism.
            - Evaluate and Contrast different design options in terms of effectiveness and efficiency.
            """)

###################################################################################
###################################################################################

def display_intro2CS_course_content():
    st.title("Introduction to Computer Science")

    # -------------------------
    st.header("Introduction to Computer Systems")
    st.subheader("Turing Model")
    st.markdown("""
        - Defines a computer as a **data processor** (input → process → output).
    """)
    col1, col2, col3 = st.columns((3, 4, 3))
    with col2:
        st.image("images/Turing_Machine_Model_Davey_2012.jpg", caption="Turing Machine")
    st.markdown("""
        - A black box model: accepts input data, processes it, and produces output.
        - Problems:
            - Too general, doesn't specify what operations can be performed.
            - Could describe specific-purpose machines (e.g. temperature controller).
        """)
    st.subheader("Programmable Data Processors")
    st.markdown("""
        - Adds the concept of a **program** to the Turing model.
        - Program = set of instructions that tells the computer what to do with data.
        - Output depends on **both input data and the program**.
        """)
    st.subheader("Von Neumann Model")
    col1, col2 = st.columns((6, 4))
    with col2:
        st.image("images/PW-2012-12-review-Campbell-Kelly-1.jpg", caption="Von Neumann's Computer")
    with col1:
        st.markdown("""
        - Stores both **data and program in memory**.
        - Divides the computer into:
            1. **Memory** — stores programs and data during processing
            2. **Arithmetic Logic Unit (ALU)** — performs arithmetic and logical operations
            3. **Control Unit** — directs memory, ALU, and I/O subsystem
            4. **Input/Output Subsystem** — interfaces with external world
        - Executes using the **fetch-decode-execute cycle**.
        """)

    st.markdown("---")

    # -------------------------
    st.header("Number Systems")
    st.subheader("Positional vs Non-Positional")
    st.markdown("""
    - **Non-positional**: Value does not depend on position (e.g. Roman numerals)
    - **Positional**: Value depends on position and base (radix)
    """)
    st.latex(r"n = \sum (digit \times base^{position})")

    st.subheader("Common Bases")
    st.table(pd.DataFrame({
        "System": ["Decimal (10)", "Binary (2)", "Octal (8)", "Hexadecimal (16)", "Ternary (3)"],
        "Symbols": ["0-9", "0-1", "0-7", "0-9, A-F", "0-2"],
        "Example": [
            "224.5 = 2×10² + ... + 0.5",
            "(1101)₂ = 1×2³+1×2²+0×2¹+1×2⁰ = 13",
            "(2AE)₁₆ = 2×16²+10×16¹+14×16⁰ = 686",
            "(1256)₈ = 1×8³+2×8²+5×8¹+6×8⁰",
            "(1202)₃ = 1×3³+2×3²+0×3¹+2×3⁰"
        ]
    }))

    with st.expander("Conversions"):
        st.markdown("""
        - **Any base → Decimal**: Sum digit × base^position
        - **Decimal → Any base**:
            - Integer: Repeated division by base (collect remainders bottom-up)
            - Fraction: Multiply by base repeatedly (collect integer parts)
        - **Binary ↔ Hex**: 4 bits = 1 hex digit
        - **Binary ↔ Octal**: 3 bits = 1 octal digit
        - **Octal ↔ Hex**: Convert via binary
        """)

    st.markdown("---")

    # -------------------------
    st.header("Data Storage")
    st.markdown("All data is stored as **bits** (0/1). A mix of different types is called multimedia.")
    st.subheader("Storing Numbers")
    st.markdown("""
    - **Unsigned**: positive values only, max = 2^n - 1  
    - **Sign & Magnitude**: leftmost bit = sign  
    - **Two’s Complement**: allows negatives, leftmost bit weighted negative
    """)
    st.subheader("Storing Text")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - **ASCII**: 7 bits (128 symbols)  
        """)
        st.image("images/ASCII_Table_(suitable_for_printing).svg.png", caption="ASCII Table")
    with col2:
        st.markdown("""
        - **Unicode**: 32 bits (4+ billion symbols, multiple languages)
        """)
        st.image("images/Blue-punch-card-front-horiz_top-char-contrast-stretched.png", caption="EPCDIC punched card for IBM in 50s/60s")
    st.subheader("Storing Audio")
    st.markdown("""
    - Analog → digital via **sampling → quantization → encoding**  
    - Bit rate = sampling rate × bit depth (bits/sample)
    """)
    st.image("images/image-removebg-preview (2) (1).png", caption="Audio to bits Conversion")
    st.subheader("Storing Images")
    st.markdown("""
    - **Raster (bitmap)**: grid of pixels, high resolution = large size  
    - **Vector**: mathematical shapes, scalable, smaller size  
    - **Color depth** = bits/pixel (e.g. 24-bit = 2²⁴ colors)
    """)
    col1, col2, col3 = st.columns((3, 4, 3))
    with col2:
        st.image("images/GUID-CC2D28F9-B2CF-47AF-80BE-3CA13E04E596-web.gif", caption="Raster Bitmap")

    st.markdown("---")

    # -------------------------
    st.header("Data Operations")
    st.subheader("Logic Gates")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("#### AND - Clear")
        st.image("images/image (1).png", caption="AND Gate")
        and_table = pd.DataFrame({
            "A": [0, 0, 1, 1],
            "B": [0, 1, 0, 1],
            "out": [0, 0, 0, 1]
        })
        st.markdown(and_table.to_html(index=False), unsafe_allow_html=True)
    with col2:
        st.markdown("#### OR - Set")
        st.image("images/image (2).png", caption="OR Gate")
        or_table = pd.DataFrame({
            "A": [0, 0, 1, 1],
            "B": [0, 1, 0, 1],
            "out": [0, 1, 1, 1]
        })
        st.markdown(or_table.to_html(index=False), unsafe_allow_html=True)
    with col3:
        st.markdown("#### NOT - Invert")
        st.image("images/image (3).png", caption="NOT Gate")
        not_table = pd.DataFrame({
            "A": [0, 1],
            "out": [1, 0]
        })
        st.markdown(not_table.to_html(index=False), unsafe_allow_html=True)
    with col4:
        st.markdown("#### XOR - Flip")
        st.image("images/image (4).png", caption="XOR Gate")
        xor_table = pd.DataFrame({
            "A": [0, 0, 1, 1],
            "B": [0, 1, 0, 1],
            "out": [0, 1, 1, 0]
        })
        st.markdown(xor_table.to_html(index=False), unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Masking")
        st.markdown("""
        When you want to change one single bit.
        1. If you want to clear one bit => AND with 0
        2. If you want to set one bit => OR with 1
        3. If you want to toggle (if 1 then clear or if 0 then set) => XOR with 1
        """)
        
    with col2:
        st.subheader("Arithmetic")
        st.markdown("""
        For both addition and subtraction, convert any negative number to its two's complement form.
        
        0 + 0 = 0
                    
        1 + 0 = 1
                    
        1 + 1 = 0 (carry 1)
                    
        1 + 1 + 1 (carry) = 1 (carry 1
        """)
    st.markdown("---")

    # -------------------------
    st.header("Computer Organization")
    st.subheader("CPU Components")
    col1, col2, col3 = st.columns((1, 8, 1))
    with col2:
        st.image("images/image (5).png", caption="CPU Components")
    st.markdown("""
    - **ALU**: arithmetic and logic operations  
    - **Registers**: fast temporary storage  
    - **Control Unit**: fetch-decode-execute instructions
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Memory")
        st.markdown("""
        - **Registers > Cache > RAM > Disk** (speed hierarchy)
        - **RAM** is volatile, **ROM** is non-volatile
        - Addressing: log₂(N) bits for N memory locations
        """)
    with col2:
        st.subheader("I/O Subsystem")
        st.markdown("""
        - Allows communication with external world
        - Includes storage devices, printers, keyboards, etc.
        """)

    st.markdown("---")

    # -------------------------
    st.header("Computer Networks")
    st.subheader("TCP/IP Protocol Suite")
    col1, col2 = st.columns((3, 4))
    with col2:
        st.image("images/image (6).png", caption="TCP/IP Model")
    with col1:
        st.markdown("""
        - **Application** → user-facing software  
        - **Transport** → TCP (reliable) / UDP (fast, unreliable)  
        - **Network** → IP addressing, routing  
        - **Data Link** → node-to-node delivery  
        - **Physical** → bits as signals on media
        """)
        st.subheader("Network Types")
        st.markdown("""
        - **LAN**: local, small scale, privately owned  
        - **WAN**: wide scale, often leased
        """)

    st.markdown("---")

    # -------------------------
    st.header("Software Engineering")
    col1, col2 = st.columns((3, 5))
    with col2:
        st.image("images/image-removebg-preview (3).png", caption="SDLC Phases")
    with col1:
        st.subheader("SDLC Models")
        st.markdown("""
        - **Waterfall**: linear, one phase at a time  
        - **Incremental**: build in steps, test and add features iteratively
        """)
        st.subheader("Phases")
        st.markdown("""
        - **Analysis** → what to do  
        - **Design** → how to do it  
        - **Implementation** → code  
        - **Testing** → verify correctness  
        - **Documentation** → user/system docs
        """)

    st.markdown("---")

    # -------------------------
    st.header("Security Fundamentals")
    
    col1, col2 = st.columns((4,8))
    with col2:
        st.subheader("Goals")
        st.table(pd.DataFrame({
            "Goal": ["Confidentiality", "Integrity", "Availability"],
            "Description": [
                "Prevent unauthorized access",
                "Ensure data not altered in transit",
                "Ensure systems are usable when needed"
            ],
            "Example Attack": ["Snooping", "Modification", "Denial of Service"]
        }))
    with col1:
        st.image("images/image (7).png", caption="CIA Triad")
    
    st.subheader("Techniques")
    st.markdown("""
        - **Cryptography** (symmetric, asymmetric, hashing)  
        - **Steganography** (hide information)
        - **Digital signatures, MACs** for authentication
        """)

    st.markdown("---")

    # -------------------------
    st.header("Programming Foundations (C)")
    st.code("""
    #include <stdio.h> 

    int main() {
        printf("Hello, World!\\n");  
        return 0;                  
    }
    """, language="c")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Variables & Data Types")
        st.markdown("""
        - **Variables**: Named storage for data.
        - **Data Types**: Define the kind of data a variable can hold (e.g., int, float, char).
        """)

        st.code("""
        int x; // Integer variable declaration
        x = 10; // Variable assignment
                
        int age = 25;
        float salary = 50.5; //float variable initialization
        char grade = 'A';
        """, language="cpp")
        st.markdown(""" The data types specify the memory size and the operations that can be performed on the data.""")
        st.markdown("""
        ```int x;``` declares a variable `x` of type `int` so it allocates a space in the memory to store an integer.
        ```x = 10;``` assigns the value `10` to `x` so it places the value `10` in the allocated memory space.
        """)
        st.table(pd.DataFrame({
            "Specifier": ["%d", "%f", "%c", "%s"],
            "Description": [
                "Signed integer",
                "Floating number",
                "Single character",
                "String of characters"
            ],
            "Used with": [
                "`int`",
                "`float`, `double`",
                "`char`",
                "`char[]`"
            ]
        }))
    with col2:
        st.subheader("Input/Output Operations")
        st.code("""
        int x;
        printf("Enter the value of x: ");
        scanf("%d", &x);
        printf("Value of x: %d\\n", x); 
        """, language="cpp")
        st.markdown("""
        #### Taking Input from the User:
        """)
        st.code("""
        scanf("%d", &x); 
        """, language="cpp")
        st.markdown("""
        - `scanf` reads formatted input from the standard input (keyboard).
        - `%d` specifies that we expect an integer.
        - `&x` is the address of the variable `x` where the input will be stored.
        """)
        st.markdown("""
        #### Displaying Output to the User:
        """)
        st.code("""
        printf("Value of x: %d\\n", x);
        """, language="cpp")
        st.markdown("""
        - `printf` prints formatted output to the standard output (console).
        - `%d` is a format specifier for integers.
        - `\\n` adds a new line after printing.
        """)

    st.header("Conditionals and Loops")
    st.subheader("Conditional Statements")
    col1, col2 = st.columns(2)
    with col1:  
        st.markdown("#### If Statements")
        st.markdown("""
        **If-else statements** are used to make decisions in your code based on certain conditions.
        Syntax: `if` `else if` `else`""")
        st.code("""
        if (condition) {
            // execute if condition is true
        } else if (another_condition) {
            // execute if another_condition is true
        } else if (yet_another_condition) {
            // execute if yet_another_condition is true
        } else {
            // execute if no condition is true
        }
        """, language="cpp")
        st.markdown(""" The first true condition's block will execute, and the rest will be skipped. If no condition is true, the `else` block executes (if present).""")
        st.markdown(""" Use `==` for equality, `!=` for inequality, `<`, `>`, `<=`, and `>=` for comparisons. Avoid using a single `=` as it is an assignment operator.""")

    with col2:
        st.markdown("#### Switch Statements")
        st.markdown("""
        **Switch statements** are used to execute one block of code among many based on the value of a variable.
        Syntax: `switch` `case` `default`""")
        st.code("""
        switch (variable) {
            case value1:
                // execute if variable == value1
                break;
            case value2:
                // execute if variable == value2
                break;
            default:
                // execute if variable doesn't match any case
        }
        """, language="cpp")
        st.markdown(""" Use `break` to exit the switch statement after executing a case. If no `break` is used, it will continue executing the next case (known as "fall-through").""")
    
    st.subheader("Loops")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### For Loop")
        st.markdown("""
        A **for loop** is used to repeat a block of code a specific number of times.
        Syntax: `for`""")
        st.code("""
        for (initialization; condition; step) {
            // code to execute
        }
        """, language="cpp")

        st.markdown("""
        - **Initialization**: Set up a loop variable (e.g., `int i = 0`).
        - **Condition**: Check if the loop should continue (e.g., `i < n`).
        - **Step**: Update the loop variable (e.g., `i++`).
        """)

        st.markdown(""" Loop control keywords include `break` (exit loop) and `continue` (skip to next iteration).""")
    with col2:
        st.markdown("#### While Loop")
        st.markdown("""
        A **while loop** continues to execute as long as a condition is true.
        Syntax: `while`""")
        st.code("""
        while (condition) {
            // code to execute
        }
        """, language="cpp")
        st.markdown("""
        #### Do-While Loop
        A **do-while loop** executes the code block at least once before checking the condition.
        Syntax: `do` `while`""")
        st.code("""
        do {
            // code to execute
        } while (condition);
        """, language="cpp")
     
    st.subheader("Algorithm Flowcharts")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("images/image-removebg-preview (4).png", caption="Start/End Symbol", width=100)
    with col2:
        st.image("images/image-removebg-preview (5).png", caption="Process Symbol", width=100)
    with col3:
        st.image("images/image-removebg-preview (6).png", caption="Input/Output Symbol", width=100)
    with col4:
        st.image("images/image-removebg-preview (7).png", caption="Decision Symbol", width=100)

    #pdf_viewer("C:\\Users\\walki\\Downloads\\1553956439.pdf", width=700)
    pdf_path = "images/1553956439.pdf"

    with open(pdf_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")

    pdf_display = f"""
    <iframe src="data:application/pdf;base64,{base64_pdf}" 
            width="700" height="300" 
            style="border: none;">
    </iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)
    

    st.info("Always review the syllabus to ensure you cover all required topics and examples.")
    with st.expander("Course Outcomes"):
            st.markdown("""
            - Compare and convert decimal numbers to other systems and perform basic operations on them.
            - Explain the components, history and purpose of computers.
            - Be able to discuss and explain basic definitions of computer science.
            - Select and declare suitable variables for data input and output.
            - To develop good programming skills and to develop problem-solving skills via C-programming language.
            """)

###################################################################################
###################################################################################