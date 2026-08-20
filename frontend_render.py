def frontend_render_formater(state: AgentState) -> FrontendResponse:
    """
    In production this should be SSE attrach with make_decision but since in this psudo code, I will use the one time response.
    Return the final structured JSON payload to the frontend.

    """

    response = state["final_response"]

    # type 1 response
    if state.get("sql_result") is None:
        return {
            "text": response["text"]
        }

    # type 2 response
    return {
        "text": response["text"],
        "data": (state["sql_result"]),
        "visualization_type": response["visualization_type"]
    }