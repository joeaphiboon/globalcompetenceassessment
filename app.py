import streamlit as st
import random

# Define the questions and options for the self-assessment questionnaire
attitude_cq_questions = [
    "I am open to changing my opinions based on new information or perspectives from other cultures.",
    "I feel a sense of responsibility to take action on global issues, even in small ways.",
    "I value diversity and see it as a strength in teams and communities.",
    "I appreciate similarities and differences between my own and other cultures.",
    "I feel confident in my ability to interact with people from different cultural backgrounds.",
    "I am conscious of how my cultural background influences my interactions with people from different cultures.",
    "I adjust my cultural knowledge when interacting with people from an unfamiliar culture.",
    "I am aware of how I apply my cultural knowledge in cross-cultural interactions.",
    "I know the legal and economic systems of other cultures.",
    "I know the rules (e.g., vocabulary, grammar) of other languages.",
    "I know the cultural values and religious beliefs of other cultures.",
    "I enjoy interacting with people from different cultures.",
    "I am confident that I can socialize with locals in an unfamiliar cultural environment.",
    "I am sure I can deal with the stresses of adjusting to a new culture.",
    "I change my verbal behavior (e.g., accent, tone) when a cross-cultural interaction requires it.",
    "I use pause and silence differently to suit different cross-cultural situations.",
    "I vary the rate of my speaking when a cross-cultural situation requires it."
]

attitude_cq_options = ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]

# Define the case studies and their questions
case_studies = [
    {
        "title": "Cultural Misunderstanding",
        "description": "You are working on an international team project with colleagues from Japan, Brazil, and Germany. During a video conference, your Japanese colleague seems reluctant to disagree with ideas proposed by senior team members, even when you know he has concerns. Your Brazilian teammate speaks animatedly and interrupts others frequently. The German team member appears frustrated by the lack of strict adherence to the agenda and meeting end time.",
        "questions": [
            {
                "question": "How would you adapt your communication style to work effectively with each colleague?",
                "options": [
                    "I would not change my communication style at all",
                    "I would try to speak more formally with everyone",
                    "I would adapt my style somewhat for each colleague based on their cultural norms",
                    "I would research each culture's communication norms and adapt my style accordingly for each colleague"
                ]
            },
            {
                "question": "What strategies would you propose to improve team dynamics and collaboration?",
                "options": [
                    "I would insist everyone follow my preferred meeting style",
                    "I would suggest we rotate meeting styles each time",
                    "I would propose finding a middle ground that accommodates everyone's styles",
                    "I would facilitate a discussion on cultural differences and collectively develop team norms"
                ]
            }
        ]
    },
    {
        "title": "Global Issue Analysis",
        "description": "Your company is considering expanding operations to a developing country with a history of political instability and human rights concerns. However, the country also has a large youth population, growing middle class, and government incentives for foreign investment. You've been asked to analyze the opportunities and risks.",
        "questions": [
            {
                "question": "What key factors would you prioritize in your analysis?",
                "options": [
                    "Only economic factors like market size and incentives",
                    "Economic factors and some basic political considerations",
                    "Economic, political, and social factors",
                    "Comprehensive analysis of economic, political, social, and ethical factors"
                ]
            },
            {
                "question": "How would you approach the ethical considerations of this expansion?",
                "options": [
                    "Ethics are not relevant to business decisions",
                    "Consider ethics only if required by company policy",
                    "Balance ethical concerns with business opportunities",
                    "Prioritize ethical considerations and propose ways to positively impact the local community"
                ]
            }
        ]
    },
    {
        "title": "Sustainable Development Project",
        "description": "You are part of an international team working on a sustainable development project in a rural area of a developing country. The project aims to implement clean water solutions and improve agricultural practices. However, some local community members are resistant to changing traditional methods.",
        "questions": [
            {
                "question": "How would you approach understanding the local cultural context and concerns?",
                "options": [
                    "Implement the project as planned without considering local input",
                    "Have a brief meeting with local leaders to inform them of the project",
                    "Conduct surveys and hold community meetings to gather input",
                    "Immerse in the community, learn about local traditions, and co-design solutions with locals"
                ]
            },
            {
                "question": "How would you balance implementing new technologies with respecting local traditions?",
                "options": [
                    "Insist on using only the new technologies as they are objectively better",
                    "Try to convince locals to adopt new methods but fall back on traditional ones if resisted",
                    "Blend new technologies with traditional methods where possible",
                    "Work with the community to evolve traditional methods, incorporating new technologies in culturally appropriate ways"
                ]
            }
        ]
    },
    {
        "title": "Multicultural Marketing Campaign",
        "description": "Your company is launching a new product globally and you're tasked with developing a marketing campaign for multiple countries including the United States, Japan, Brazil, and Saudi Arabia.",
        "questions": [
            {
                "question": "How would you ensure the campaign is culturally appropriate for each market?",
                "options": [
                    "Use the same campaign in all markets to maintain brand consistency",
                    "Make minor adjustments to the US campaign for each market",
                    "Create separate campaigns for each country based on cultural research",
                    "Collaborate with local teams in each country to co-create culturally resonant campaigns"
                ]
            },
            {
                "question": "What methods would you use to test the effectiveness and cultural appropriateness of the campaign before launch?",
                "options": [
                    "Rely on the judgment of the marketing team",
                    "Conduct basic market research in each country",
                    "Use focus groups with members of each target culture",
                    "Employ a combination of focus groups, local expert consultations, and small-scale pilot tests in each market"
                ]
            }
        ]
    }
]

def calculate_cq_score(answers):
    return sum(answers)

def get_cq_breakdown(answers):
    return {
        "Attitudes": sum(answers[:5]),
        "Metacognitive CQ": sum(answers[5:8]),
        "Cognitive CQ": sum(answers[8:11]),
        "Motivational CQ": sum(answers[11:14]),
        "Behavioral CQ": sum(answers[14:17])
    }

def classify_global_competence(score, max_score):
    percentage = (score / max_score) * 100
    if percentage >= 80:
        return "High global competence"
    elif percentage >= 60:
        return "Moderate global competence"
    elif percentage >= 40:
        return "Developing global competence"
    else:
        return "Low global competence"

def shuffle_scenario_options(case_studies):
    shuffled_cases = []
    for case in case_studies:
        shuffled_case = case.copy()
        shuffled_case['questions'] = []
        for question in case['questions']:
            shuffled_question = question.copy()
            shuffled_options = question['options'].copy()
            random.shuffle(shuffled_options)
            shuffled_question['shuffled_options'] = shuffled_options
            shuffled_case['questions'].append(shuffled_question)
        shuffled_cases.append(shuffled_case)
    return shuffled_cases

def main():
    st.title("Global Competence Assessment")
    
    if 'stage' not in st.session_state:
        st.session_state.stage = 'self_assessment'
    
    if 'shuffled_options' not in st.session_state:
        st.session_state.shuffled_options = shuffle_scenario_options(case_studies)

    if st.session_state.stage == 'self_assessment':
        st.header("Self-Assessment Questionnaire")
        attitude_cq_answers = []
        for i, question in enumerate(attitude_cq_questions):
            answer = st.radio(f"{i+1}. {question}", attitude_cq_options, key=f"attitude_cq_{i}")
            attitude_cq_answers.append(attitude_cq_options.index(answer) + 1)
        
        if st.button("Submit Self-Assessment"):
            st.session_state.attitude_cq_answers = attitude_cq_answers
            st.session_state.stage = 'case_studies'
            st.rerun()

    elif st.session_state.stage == 'case_studies':
        st.header("Case Studies")
        case_study_answers = []
    
        for i, case in enumerate(st.session_state.shuffled_options):
            st.subheader(f"Case Study {i+1}: {case['title']}")
            st.write(case['description'])
            case_answers = []
            for j, question in enumerate(case['questions']):
                answer = st.radio(f"{j+1}. {question['question']}", question['shuffled_options'], key=f"case_{i}_q_{j}")
                case_answers.append(case_studies[i]['questions'][j]['options'].index(answer) + 1)
            case_study_answers.append(case_answers)

        if st.button("Submit Case Studies"):
            st.session_state.case_study_answers = case_study_answers
            st.session_state.stage = 'results'
            st.rerun()

    elif st.session_state.stage == 'results':
        st.header("Results")
        
        tab1, tab2 = st.tabs(["Scores", "Score Calculation Details"])
        
        with tab1:
            attitude_cq_score = calculate_cq_score(st.session_state.attitude_cq_answers)
            case_study_scores = [calculate_cq_score(answers) for answers in st.session_state.case_study_answers]
            
            st.subheader("Self-Assessment Score")
            max_attitude_score = len(attitude_cq_questions) * 5
            st.write(f"Your Attitude and CQ Score: {attitude_cq_score} out of {max_attitude_score}")
            
            cq_breakdown = get_cq_breakdown(st.session_state.attitude_cq_answers)
            st.subheader("Cultural Intelligence Breakdown")
            for cq_type, score in cq_breakdown.items():
                max_score = 25 if cq_type == "Attitudes" else 15
                st.write(f"{cq_type}: {score} out of {max_score}")
            
            st.subheader("Case Study Scores")
            total_case_study_score = sum(case_study_scores)
            max_case_study_score = len(case_studies) * 8  # 2 questions per case study, 4 points max per question
            for i, score in enumerate(case_study_scores):
                st.write(f"Case Study {i+1} Score: {score} out of 8")
            
            total_score = attitude_cq_score + total_case_study_score
            max_score = max_attitude_score + max_case_study_score
            st.subheader("Total Score")
            st.write(f"Your Total Global Competence Score: {total_score} out of {max_score}")
            st.write(f"Overall Classification: {classify_global_competence(total_score, max_score)}")
        
        with tab2:
            st.subheader("Score Calculation Details")
            st.write("Self-Assessment scoring:")
            st.write("- Attitudes: 5 questions, each scored 1-5, total 25 points")
            st.write("- Metacognitive CQ: 3 questions, each scored 1-5, total 15 points")
            st.write("- Cognitive CQ: 3 questions, each scored 1-5, total 15 points")
            st.write("- Motivational CQ: 3 questions, each scored 1-5, total 15 points")
            st.write("- Behavioral CQ: 3 questions, each scored 1-5, total 15 points")
            st.write(f"Total possible score: {max_score} points")

        if st.button("Restart Test"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

if __name__ == "__main__":
    main()
