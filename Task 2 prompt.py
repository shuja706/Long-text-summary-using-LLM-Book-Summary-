Prompt = """
you are an expert to write personalized study plans for students!  You are given each students profile in csv file named students and it 
has following columns - Name,Field_of_study, Year_of_study,List_of_subjects,Preferred_Learning_Styles,Personal_Objectives,Challenges,Extracurricular_activities   \n\n
Your task is to thoroughly analyze the wide range of individuals data and write study plan considering each student needs an 
aspiration along with their academic requirements. \n\n
Study plan should also be according to individual students academic performance in different subjects, and as per their learning preferences (ie.. visual, kinesthetic, auditory), extracurricular activities, and distinct personal objectives or challenges (such as preparing for a specific exam or overcoming a learning difficulty).
'''{profiles}'''
"""
