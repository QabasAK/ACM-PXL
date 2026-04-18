import streamlit as st
import random

def survival_guide_page():
    st.markdown("""
    A practical toolkit for thriving in university life academically, socially, and professionally.  
    Curated by your ACM PXL community.
    """)

    col1, col2 = st.columns(2)

    with col1:
    # -------------------
    # Break the Ice
    # -------------------
        with st.expander("Break the Ice", expanded=True):
            st.write("""
            Tips to meet people and build your network:
            - Join student clubs (especially ACM) to meet like-minded peers.
            - Attend university events and welcome sessions.
            - Introduce yourself to classmates before or after lectures.
            - Volunteer for organizing events or competitions.
            """)

            if st.button("Suggest me a social tip"):
                tips = [
                    "Sit in a new spot in class and introduce yourself to those around you.",
                    "Invite classmates to a casual study group before exams.",
                    "Attend a guest lecture and talk to the speaker afterward.",
                    "Ask someone about their favorite course or professor."
                ]
                st.info(random.choice(tips))

            st.markdown("**Resources:**")
            st.markdown("""
            - [ACM PSUT Chapter](https://www.facebook.com/ACM.PSUT)
            - [Campus Event Calendar](#)
            - [Clubs @ PSUT](#)
            """)

    with col2:
        # -------------------
        # Academic Help
        # -------------------
        with st.expander("Academic Help (Exams and Courses)", expanded=True):
            st.write("""
            Strategies for academic success:
            - Use past papers and mock exams for practice.
            - Join or form study groups.
            - Visit professors’ office hours for clarification.
            - Use learning platforms like Khan Academy, Coursera, and EdX.
            - Plan your revision schedule well before exams.
            """)

            if st.button("Suggest me a study tip"):
                tips = [
                    "Teach the topic to someone else — if you can explain it, you know it.",
                    "Use the Pomodoro Technique to stay focused.",
                    "Summarize lecture notes at the end of each week.",
                    "Practice recalling information without looking at notes."
                ]
                st.info(random.choice(tips))

            st.download_button(
                label="Download Exam Prep Checklist",
                data="1. Gather notes\n2. Collect past papers\n3. Create study schedule\n4. Practice under timed conditions",
                file_name="exam_prep_checklist.txt"
            )

            st.markdown("**Resources:**")
            st.markdown("""
            - [Khan Academy](https://www.khanacademy.org/)
            - [Coursera](https://www.coursera.org/)
            - [EdX](https://www.edx.org/)
            """)

    with col2:
        # -------------------
        # SDS (Software Development Skills)
        # -------------------
        with st.expander("SDS (Software Development Skills)", expanded=True):
            st.write("""
            Improve your software development abilities:
            - Learn version control (Git & GitHub).
            - Practice algorithms and data structures (LeetCode, HackerRank).
            - Build projects to apply what you learn.
            - Participate in hackathons and coding competitions.
            - Contribute to open-source.
            """)

            if st.button("Suggest me a coding tip"):
                tips = [
                    "Break problems into smaller sub-problems before coding.",
                    "Read others’ code on GitHub to learn new patterns.",
                    "Document your code as you write it.",
                    "Focus on writing readable code before optimizing."
                ]
                st.info(random.choice(tips))

            st.markdown("**Resources:**")
            st.markdown("""
            - [LeetCode](https://leetcode.com/)
            - [HackerRank](https://www.hackerrank.com/)
            - [GitHub Learning Lab](https://lab.github.com/)
            - [First Contributions](https://firstcontributions.github.io/)
            """)

    with col1:
        # -------------------
        # Interview Preparation
        # -------------------
        with st.expander("Interview Preparation", expanded=True):
            st.write("""
            How to prepare for technical and behavioral interviews:
            - Practice coding problems daily.
            - Prepare answers for common behavioral questions.
            - Review your projects and be ready to discuss them.
            - Research the company before interviews.
            - Practice mock interviews.
            """)

            if st.button("Suggest me an interview tip"):
                tips = [
                    "Always clarify the problem statement before starting to code.",
                    "Think aloud during coding interviews.",
                    "Prepare a few stories about challenges you've overcome.",
                    "Research the company’s tech stack before the interview."
                ]
                st.info(random.choice(tips))

            st.markdown("**Resources:**")
            st.markdown("""
            - [Pramp](https://www.pramp.com/) - Free mock interviews
            - [Interviewing.io](https://interviewing.io/)
            - [Glassdoor](https://www.glassdoor.com/)
            """)

