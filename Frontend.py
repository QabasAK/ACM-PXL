import streamlit as st
from streamlit_option_menu import option_menu 
from modules.academic import display_algorithms_course_content, display_datastructures_course_content, display_structured_course_content, display_intro2CS_course_content, display_OOP_course_content
from core.chatbot import run_chatbot
from core.rag_engine import RAG_DSA, RAG_aLGO
from modules.training import explaining_training_levels
from modules.survival import survival_guide_page


PRIMARY   = "#2D6599AE"  
PRIMARYBold   = "#2D6599FF" 
SECONDARY = "#FDF6EC"  
BOT_BG    = "#D5E8F6"  
USER_BG   = PRIMARY
FONT      = "VT323"

image = "images/Association_for_Computing_Machinery_(ACM)_logo.svg.png"
pxl = "images/1.png"

st.set_page_config(
    page_title="PXL - ACM Chatbot",
    page_icon=pxl,
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("PXL - ACM Chatbot")
st.markdown("""
 <div style='text-align: justify'> Welcome to the ACM Chapter Chatbot! This is PXL, here to assist you with your academic needs, training programs, events, and more. Whether you are navigating your programming courses, seeking information about competitive programming, or just want to chat about your day, PXL is here to help! Please select one of the options below to get started.
</div>""", unsafe_allow_html=True)

st.sidebar.image("images/ChatGPT Image Jun 25, 2025, 01_40_07 AM.png" ,use_container_width=True)
st.logo(image, size="large", link="https://psutsc.acm.org/", icon_image=image)

st.markdown("""
    <style>
    .sidebar-title {
        font-weight: bold;
        font-size: 2rem;
        margin-bottom: 0.5rem;
        text-align: center;
    }
    .sidebar-footer {
        font-size: 1rem;
        color: #888;
        text-align: justify;
    }
    .sidebar-txt {
        margin-top: 0.3rem;
        margin-bottom: 0.3rem;
        font-size: 1rem;
        color: #888;
        text-align: justify;
    }
    </style>
""", unsafe_allow_html=True)

if 'current_page' not in st.session_state:
    st.session_state.current_page = "MAIN PAGE"
if 'category' not in st.session_state:
    st.session_state.category = None

with st.sidebar:
    if "current_page" not in st.session_state:
        st.session_state.current_page = "MAIN PAGE"

    st.markdown('<div class="sidebar-title">ACM Student Chapter @ PSUT</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-txt">PXL Chatbot is designed for our ACM chapter to make academic help, event information, and training resources more accessible to students.</div>', unsafe_allow_html=True)

    
    selected = option_menu(
        menu_title="Navigation",
        options=["MAIN PAGE", "SURVIVAL GUIDE", "FAQ", "ABOUT"],
        icons=["house", "book", "question-circle", "info-circle"],
        default_index=0,
        menu_icon="cast",
        orientation="vertical",
        styles={

            "container": {"padding": "0.2rem","background-color": "white","border-radius": "0", "margin-top": "0.5rem", "margin-bottom": "0", "divider": "1px solid #e6e6e6"},  
            "icon": {"font-size": "1rem"},
            "nav-link": {"font-size": "0.75rem", "--hover-color":"#c2e7d9", "font-weight": "bold","text-align":
                "left", "color": PRIMARY, "margin": "0.1rem 0", "padding": "0.1rem 1rem", "border-radius": "4px"},
            "nav-link-selected": {"color": "white", "font-weight": "bold", "background-color": "#264d3c"},
            "menu-title": {"font-size": "1rem", "font-weight": "bold", "color": PRIMARYBold, "margin-bottom": "0", "display": "block", "divider": "#262730"},
            "menu-icon": {"font-size": "1rem"},
            "divider": {"margin": "0.5rem 0", "border-top": "1px solid black", "opacity": "0.1"},
        }
    )
    st.session_state.current_page = selected

    st.markdown('<div class="sidebar-footer">If you spot an error, have a fun feature request or helpful resources, reach out to my email <a href=mailto:qabaskaissi@gmail.com>qabaskaissi@gmail.com</a> :) </div>', unsafe_allow_html=True)

if st.session_state.current_page == "MAIN PAGE":
    st.header(f"How can PXL help you today?")

    if 'category' not in st.session_state:
        st.session_state.category = None

    def set_category(cat):
        st.session_state.category = cat

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.button("I am taking a programming course this semester and I need help with it",
                    key="btn_acad",
                    on_click=set_category, args=("academic",))
    with col2:
        st.button("Tell me more about problem solving, CP and the ACM training programs",
                    key="btn_train",
                    on_click=set_category, args=("training",))
    with col4:
        st.button("I am bored, I want to chat with PXL about my day, studies or hobbies",
                    key="btn_chat",
                    on_click=set_category, args=("chat",))
    with col3:
        st.button("I am looking for fun ACM events and activities happening this semester",
                    key="btn_events",
                    on_click=set_category, args=("events",))

    if st.session_state.category == "academic":
        st.write("You selected: Academic Help")
        option = st.selectbox(
            "What programming course are you taking?",
            ("Select the Course",
                "11102 - Introduction to Computer Science",
                "11103 - Structured Programming",
                "11206 - Object-Oriented Programming",
                "11212 - Data Structures and Introduction to Algorithms",
                "11313 - Algorithms Design and Analysis")
        )
        if option != "Select the Course":
            st.success(f"You selected: {option}")

        if option == "11102 - Introduction to Computer Science":
            display_intro2CS_course_content()
            st.text_input("Enter your question about Introduction to Computer Science:", key="intro_query")
            if st.session_state.intro_query:
                #response = RAG_aLGO(st.session_state.intro_query) ##############
                #st.write("Response:", response)
                st.caption("Stay Tuned :)")
                
        elif option == "11103 - Structured Programming":
            display_structured_course_content()
            st.text_input("Enter your question about Structured Programming:", key="structured_query")
            if st.session_state.structured_query:
                #response = RAG_aLGO(st.session_state.structured_query)  ###############
                #st.write("Response:", response)
                st.caption("Stay Tuned :)")
        
        elif option == "11206 - Object-Oriented Programming":
            display_OOP_course_content()
            st.text_input("Enter your question about Object-Oriented Programming:", key="oop_query")
            if st.session_state.oop_query:
                #response = RAG_aLGO(st.session_state.oop_query)
                #st.write("Response:", response)
                st.caption("Stay Tuned :)")
        
        elif option == "11212 - Data Structures and Introduction to Algorithms":
            display_datastructures_course_content()
            st.text_input("Enter your question about Data Structures and Introduction to Algorithms:", key="data_structures_query")
            if st.session_state.data_structures_query:
                response = RAG_DSA(st.session_state.data_structures_query)
                st.write("Response:", response)

        elif option == "11313 - Algorithms Design and Analysis":
            display_algorithms_course_content()
            st.text_input("Enter your question about Algorithms Design and Analysis:", key="algorithms_query")
            if st.session_state.algorithms_query:
                response = RAG_aLGO(st.session_state.algorithms_query)
                st.write("Response:", response)
            
    elif st.session_state.category == "training":
        st.write("You selected: Training Programs")
        explaining_training_levels()

    elif st.session_state.category == "chat":
        st.write("You selected: Chat with PXL")
        st.info("Send us your favorite PXL message at acm-club@std.psut.edu.jo :3")
        run_chatbot()

    elif st.session_state.category == "events":
        st.write("You selected: Events and Activities")
        st.write("What kind of ACM events or activities are you interested in?")
    
##############################################################################################################################
elif st.session_state.current_page == "SURVIVAL GUIDE":
    st.header("Survival Guide")
    survival_guide_page()


##############################################################################################################################
elif st.session_state.current_page == "FAQ":
    st.header("Frequently Asked Questions")

    st.subheader("ACM Chapters - FAQs")
    with st.expander("What is an ACM Student Chapter?"):
        st.write("An ACM chapter is a university-based group of students dedicated to advancing computing knowledge and practice.")
    
    with st.expander("Are ACM chapters connected globally?"):
        st.write("Yes. All chapters are affiliated with ACM HQ (USA) and are part of a worldwide academic and industry network.")

    with st.expander("Can PSUT students collaborate with other ACM chapters?"):
        st.write("Absolutely. Cross-university events and collaborations are highly encouraged—especially for national/regional competitions, workshops, and research.")
    
    st.subheader("ACM @ PSUT - FAQs")
    with st.expander("What is the ACM Chapter at PSUT?"):
        st.write("ACM PSUT is the official student chapter of the Association for Computing Machinery at Princess Sumaya University for Technology. We promote technical excellence, community building, and innovation in computing.")
    
    with st.expander("Who can join the ACM Chapter at PSUT?"):
        st.write("All PSUT students interested in computing, technology, and innovation are welcome to join. Membership is free and open to all disciplines.")
    
    with st.expander("What activities does the ACM Chapter at PSUT organize?"):
        st.write("We organize competitive programming contests, training sessions, tech talks, workshops, and social events to foster a vibrant computing community at PSUT.")
    
    with st.expander("How can I get involved with the ACM Chapter at PSUT?"):
        st.write("Fill out our member form, attend events regularly, and apply when we open leadership/team positions each year. Follow us on social media and join our mailing list to stay updated!")

    st.subheader("CP and Training - FAQs")
    with st.expander("What is competitive programming?"):
        st.write("Competitive programming is solving well-defined problems under time constraints using code. It sharpens problem-solving, algorithms, and coding speed—essential for interviews and tech careers.")
    with st.expander("Do I need to be good at math to start CP?"):
        st.write("Not necessarily. While math helps, CP focuses more on logical thinking and algorithmic problem-solving. Many successful programmers started with basic math skills and improved through practice.")
    
    with st.expander("What is the difference between CP and general problem solving?"):
        st.write("Competitive programming is a structured form of problem solving with time limits and specific rules. General problem solving can be more open-ended and creative, without strict constraints.")
    
    with st.expander("What kind of trainings does ACM PSUT offer?"):
        st.write("We offer training sessions on algorithms, data structures, problem-solving techniques, and competitive programming strategies. These are designed to help students improve their skills and prepare for competitions as well as university courses.")

    with st.expander("Are the trainings beginner-friendly?"):
        st.write("Yes! We categorize trainings into beginner, intermediate, and advanced levels.")

    st.subheader("ACM PXL - FAQs")
    with st.expander("What is ACM PXL?"):
        st.write("ACM PXL is the official mascot of the ACM Chapter at PSUT. It represents the spirit of innovation, collaboration, and community within the chapter.")

    with st.expander("What can PXL help me with?"):
        st.write("PXL can assist with academic queries, training programs, events, and general inquiries related to the ACM Chapter at PSUT. It's designed to make information more accessible and provide a friendly interface for engaging with the chapter's resources.")

    with st.expander("How is PXL built?"):
        st.write("PXL is a fully student-developed AI system built using open-source, lightweight, and cost-effective tools:")
        st.table([
            ["Frontend UI", "Streamlit", "Interactive web app for students to chat with PXL. Clean, fast, and embeddable."],
            ["Local LLM Inference", "Ollama", "Runs local LLMs without needing cloud APIs."],
            ["Programming Language", "Python", "For backend logic and integration"],
            ["RAG (Retrieval-Augmented Generation)", "LangChain / LlamaIndex", "Connects user queries to indexed documents (lecture notes, PDFs, slides)."],
            ["File Preprocessing", "PyPDF2, pdfplumber", "Extracts and preprocesses academic PDFs for chunking and tagging."]
        ])

    with st.expander("Can I contribute to PXL?"):
        st.write("Absolutely. PXL is meant to be community-driven. Whether you're into:")
        st.write("- NLP / AI pipelines")
        st.write("- Frontend development")
        st.write("- Document indexing and tagging")
        st.write("- UI/UX for student tools")

    ##############################################################################################################################
elif st.session_state.current_page == "ABOUT":
    col1, col2 = st.columns(2)
    with col2:
        st.header("About PXL")
        st.markdown(""" <div style='text-align: justify'>
        PXL is the official mascot of the ACM Chapter at PSUT, first designed by Layan Faqhawi during the 2023/2024 academic year. 
        Its playful and welcoming design quickly made it a symbol of the chapter. In 2024/2025, Layan Faqhawi and Massa Al-Qamhawi brought PXL to life as a physical object, 
        making it a central part of chapter culture.
        </div>""", unsafe_allow_html=True)

        col11, col12, col22 = st.columns([0.2, 0.3, 0.2]) 
        with col12:
            st.image("images/ChatGPT_Image_Jul_2__2025__04_59_13_AM-removebg-preview.png")

        st.markdown(""" <div style='text-align: justify'>
        This website extends that spirit into the digital world. The chatbot is here to help students navigate academic life, 
        stay updated on events, and find quick answers to their questions.
        </div>""", unsafe_allow_html=True)

        st.subheader("PXL Chatbot")
        st.markdown(""" <div style='text-align: justify'>
        The PXL Chatbot is built using a combination of technologies to ensure an interactive user experience. Key components include:

- **Streamlit**: A framework for building web applications in Python, used for creating the chatbot interface.
- **Langchain**: A library for developing applications powered by language models.
- **Ollama**: A platform providing access to large language models, used for generating responses in the chatbot.
    </div>""", unsafe_allow_html=True)

        st.markdown("""
For each course in the main page, a custom RAG (Retrieval-Augmented Generation) pipeline is built using LlamaIndex to index lecture notes, slides, and other resources.
""")
        st.graphviz_chart("""
digraph {
    rankdir=UD;
    fontsize=8;
    nodesep=0.3;
    ranksep=0.3;

    // Global style
    graph [bgcolor=transparent];
    node [shape=box, style="square", fontsize=8, fontcolor=white, color=transparent, fillcolor="#1e1e1e"];
    edge [color=gray, fontcolor=white];

    subgraph cluster_index {
        label="Indexing Phase\\n(Offline)\\ndone once per course";
        fontsize=10;
        fontcolor=white;
        color=lightblue;

        A1 [label="Raw Documents\\n(PDFs, Notes, Slides)"];
        A2 [label="Chunking\\n(400–600 tokens + overlap)"];
        A3 [label="Embedding Model\\n(nomic-embed-text)"];
        A4 [label="Vector DB\\n(Indices)"];

        A1 -> A2 -> A3 -> A4;
    }

    subgraph cluster_query {
        label="Query Phase\\n per question";
        fontsize=12;
        fontcolor=white;
        color=white;

        B1 [label="Student Query"];
        B2 [label="Embed Query\\n(nomic-embed-text)"];
        B3 [label="Vector DB Search\\n(similarity_top_k=5)"];
        B6 [label="LLM\\n(phi4-mini)"];

        B1 -> B2 -> B3 -> B6;
    }

    // Connection between phases
    A4 -> B3 [style=dashed, label="stored embeddings"];
}
""", use_container_width=True)  


    with col1:
        st.header("About ACM ")
        st.markdown(""" <div style='text-align: justify'>
        The Association for Computing Machinery (ACM) is the world's largest scientific and educational computing society, dedicated to advancing computing as a science and profession.
        Founded in 1947, ACM brings together computing professionals, educators, and students to share knowledge, collaborate on research, and promote the advancement of computing technology.
        </div>""", unsafe_allow_html=True)
        st.markdown(""" <div style='text-align: justify'>
        Over the decades, ACM has grown into a global network with 100,000+ members in academia and industry, fostering collaboration and innovation across every field of computing—from theoretical computer science and algorithms, to AI, software engineering, human-computer interaction, and more.
        ACM provides resources, networking opportunities, and professional development for computing professionals and students worldwide.
        </div>""", unsafe_allow_html=True)

        st.image("images/specs_products_acm_releasedAssets_images_acm-logo-1-ad466e729c8e2a97780337b76715e5cf.png")

        st.subheader("ACM @ PSUT")
        st.markdown(""" <div style='text-align: justify'>
        The ACM Chapter at Princess Sumaya University for Technology (PSUT) is a student-led club dedicated to promoting computer science and technology among students.        
        The chapter organizes various events, competitions, and training programs to enhance students' skills in programming, problem-solving, and competitive programming.
        The chapter also serves as a platform for students to connect, collaborate, and share knowledge in the field of computer science.
        </div>""", unsafe_allow_html=True)
        st.markdown(""" <div style='text-align: justify'>
        The ACM PSUT Student Chapter was established in May 2014, launching with its first interactive event, The Coding Marathon, which continues to be an annual tradition to this day.  
        Since then, the chapter has grown into one of the most accomplished and active ACM chapters in the region.
        </div>""", unsafe_allow_html=True)

        st.image("images/arab-collegiate-programming-championship-1500x470.png")

        st.markdown("""
        Over the years, PSUT teams have achieved historic victories in international competitions:
        - In 2019, PSUT made history at the Africa and Arab Collegiate Programming Contest (ACPC) by securing both 1st and 2nd place.
        - Our teams have consistently ranked in the top 10 globally at IEEEXtreme, including 4th place worldwide in 2019 and 1st place worldwide in 2020 and 2022.
        - Multiple PSUT teams have proudly represented Jordan at the prestigious ICPC World Finals, beginning with our first qualification in 2014.
        """)
        
        st.markdown(""" <div style='text-align: justify'>
        In addition to competitive programming, the chapter has led initiatives like the Ramadan Coding Marathon, Tech-Talks, Coding Nights, and the Codability outreach program for school students.  
        Our alumni have gone on to excel in big tech companies, research, and academia, and many remain active contributors to the computing community.
        </div>""", unsafe_allow_html=True)
        

    st.markdown(""" <div style='text-align: center; font-size: 1.5rem; margin-top: 1rem;'>
    Special thanks to the amazing ACM team, supervisors, trainers, and volunteers who continue to support this club non-stop!
    </div>""", unsafe_allow_html=True)

    st.divider()
    st.caption("This chatbot is a work in progress and is not affiliated with any organization. It is intended for educational and informational purposes only. The responses provided by the chatbot are generated based on the input received and may not always be accurate or up-to-date. Use at your own discretion.")



