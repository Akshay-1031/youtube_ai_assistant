from langchain_core.runnables import (
    RunnableLambda,
    RunnableBranch,
)

from langchain_core.messages import (
    HumanMessage,
    ToolMessage,
)

import json

from agent import llm_with_tools
from tools import tool_mapping

def execute_tool(tool_call):
    """Execute single tool call and return ToolMessage"""

    try:
        result = tool_mapping[tool_call["name"]].invoke(
            tool_call["args"]
        )

        content = (
            json.dumps(result)
            if isinstance(result, (dict, list))
            else str(result)
        )

    except Exception as e:

        content = f"Error: {str(e)}"

    return ToolMessage(
        content=content,
        tool_call_id=tool_call["id"]
    )


def process_tool_calls(messages):
    """Recursive tool call processor"""

    last_message = messages[-1]

    tool_messages = [

        execute_tool(tc)

        for tc in getattr(
            last_message,
            "tool_calls",
            []
        )

    ]

    updated_messages = messages + tool_messages

    next_ai_response = llm_with_tools.invoke(
        updated_messages
    )

    return updated_messages + [

        next_ai_response

    ]


def should_continue(messages):
    """Check if another iteration is required"""

    last_message = messages[-1]

    return bool(

        getattr(
            last_message,
            "tool_calls",
            None
        )

    )

def _recursive_chain(messages):
    """Recursively process tool calls until completion"""

    if should_continue(messages):

        new_messages = process_tool_calls(
            messages
        )

        return _recursive_chain(
            new_messages
        )

    return messages


recursive_chain = RunnableLambda(
    _recursive_chain
)

universal_chain = (

    RunnableLambda(

        lambda x: [

            HumanMessage(
                content=x["query"]
            )

        ]

    )

    |

    RunnableLambda(

        lambda messages:

        messages + [

            llm_with_tools.invoke(
                messages
            )

        ]

    )

    |

    recursive_chain

)
