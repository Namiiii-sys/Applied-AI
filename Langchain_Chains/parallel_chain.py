from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
model1 = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')
model2 = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = "Generate short notes from the follwoing given text \n{text}",
    input_variables=['text']
)
prompt2 = PromptTemplate(
    template = "Generate a quiz from the follwoing gven text \n {text}",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz into a single document \n -> {notes} and {quiz}",
    input_variables=['notes','quiz'])

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser
final_chain = parallel_chain | merge_chain
print(final_chain.invoke({'text':"""
 The Swachh Bharat Mission (SBM) is India's flagship nationwide cleanliness and sanitation campaign. Evolving from Phase 1’s focus on eliminating open defecation, it currently operates as SBM 2.0. This phase targets "Garbage-Free Cities" and "ODF Plus" villages through total waste processing and water management.Mission Progress & ImpactSanitation Access: Over 12 crore (120 million) individual household toilets have been constructed nationwide, effectively ending open defecation for hundreds of millions.Urban Cleanliness (SBM-Urban): A large majority of cities have achieved ODF+ and ODF++ status. The focus has shifted to processing over 81% of municipal solid waste through composting, bio-methanation, and material recovery.Rural Progress (SBM-Grameen): Over 6 lakh (600,000) villages have achieved Open Defecation Free (ODF) Plus status, heavily incorporating Solid and Liquid Waste Management (SLWM) assets like leach pits and plastic waste management units.Public Health: Studies indicate a direct correlation between SBM and improved public health, noting a sharp reduction in diarrheal deaths and groundwater contamination in ODF areas.
"""}))

final_chain.get_graph().print_ascii()