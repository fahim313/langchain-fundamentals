from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate(
    
    template=("""
Write a professional email.

Receiver: {receiver}

Purpose: {purpose}

Details:
{details}

Generate only the email.
"""),
input_variables=["receiver","purpose","details"],
validate_template=True
)

prompt.save("02-prompts/02-dynamic_prompts/save_prompts/email_prompt.json")