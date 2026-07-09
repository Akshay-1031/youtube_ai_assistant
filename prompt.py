from langchain_core.prompts import ChatPromptTemplate

summary_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert YouTube video summarizer.

Generate a concise summary with the following sections:

## Overview

## Key Points

## Important Takeaways

## Conclusion

Keep the response well structured.
"""
        ),
        (
            "human",
            "{transcript}"
        )
    ]
)